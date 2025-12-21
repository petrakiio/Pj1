import os
import bcrypt
import conn
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from pathlib import Path

load_dotenv()

# --- Configurações Iniciais ---
CHAVE_FILE = Path("chave.key")
ARQUIVO_LOCAL = Path("hash.txt")

def inicializar_fernet():
    if CHAVE_FILE.is_file():
        chave = CHAVE_FILE.read_bytes()
    else:
        chave = Fernet.generate_key()
        CHAVE_FILE.write_bytes(chave)
    return Fernet(chave)

fernet = inicializar_fernet()
logado = False
usuario_logado_gmail = None

# --- Funções de Banco de Dados (Nuvem) ---

def cadastrar_usuario(nome, gmail, senha_limpa):
    """Cria um novo usuário com senha hashed."""
    try:
        salt = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha_limpa.encode('utf-8'), salt)
        
        cursor = conn.db.cursor()
        table = os.getenv("DB_TABLE")
        
        sql = f"INSERT INTO {table}(nome, gmail, senha) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, gmail, senha_hash.decode('utf-8')))
        conn.db.commit()
        return True
    except Exception as e:
        print(f"❌ Erro ao cadastrar: {e}")
        return False

def login_usuario(nome, senha_digitada):
    """Verifica credenciais e retorna o gmail se sucesso."""
    try:
        cursor = conn.db.cursor()
        table = os.getenv("DB_TABLE")
        sql = f"SELECT gmail, senha FROM {table} WHERE nome = %s"
        cursor.execute(sql, (nome,))
        user = cursor.fetchone()
        
        if user and bcrypt.checkpw(senha_digitada.encode('utf-8'), user[1].encode('utf-8')):
            return user[0]
        return None
    except Exception as e:
        print(f"❌ Erro no login: {e}")
        return None
def ver_senhas_online(gmail):
    """Busca a senha criptografada no banco e a exibe descriptografada."""
    try:
        cursor = conn.db.cursor()
        table = os.getenv("DB_TABLE")
        sql = f"SELECT Senhas FROM {table} WHERE gmail = %s"
        cursor.execute(sql, (gmail,))
        resultado = cursor.fetchone()

        if resultado and resultado[0]:
            senha_crip = resultado[0]
            senha_limpa = fernet.decrypt(senha_crip.encode()).decode()
            print(f"\n☁️  Sua senha salva na nuvem: {senha_limpa}")
        else:
            print("\n☁️  Nenhuma senha encontrada na nuvem para este usuário.")
            
    except Exception as e:
        print(f"❌ Erro ao buscar na nuvem: {e}")

def salvar_na_nuvem(senha_secreta, gmail):
    """Salva uma senha criptografada na coluna 'Senhas' do banco."""
    try:
        senha_crip = fernet.encrypt(senha_secreta.encode()).decode()
        cursor = conn.db.cursor()
        table = os.getenv("DB_TABLE")
        sql = f"UPDATE {table} SET Senhas = %s WHERE gmail = %s"
        cursor.execute(sql, (senha_crip, gmail))
        conn.db.commit()
        print("✅ Senha sincronizada na nuvem!")
    except Exception as e:
        print(f"❌ Erro ao salvar na nuvem: {e}")

# --- Funções de Armazenamento Local ---

def salvar_local(senha_secreta):
    """Criptografa e anexa uma senha ao arquivo txt."""
    try:
        senha_crip = fernet.encrypt(senha_secreta.encode()).decode()
        with open(ARQUIVO_LOCAL, "a", encoding="utf-8") as f:
            f.write(senha_crip + "\n")
        print("✅ Senha salva localmente em hash.txt!")
    except Exception as e:
        print(f"❌ Erro ao salvar local: {e}")

def listar_senhas_locais():
    """Lê, descriptografa e exibe as senhas do arquivo txt."""
    if not ARQUIVO_LOCAL.is_file():
        print("📭 Nenhum arquivo local encontrado.")
        return

    print("\n--- Suas Senhas Locais ---")
    with open(ARQUIVO_LOCAL, "r") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                try:
                    descriptografada = fernet.decrypt(linha.encode()).decode()
                    print(f"🔑 {descriptografada}")
                except:
                    print("⚠️ Erro ao descriptografar uma linha (Chave incompatível).")

# --- Loop Principal ---

while True:
    status = f"🟢 [LOGADO: {usuario_logado_gmail}]" if logado else "🔴 [DESLOGADO]"
    print(f"\n{status}")
    print("1 - Cadastrar Novo Usuário")
    print("2 - Login / Logout")
    print("3 - Salvar Senha Local")
    print("4 - Salvar Senha na Nuvem")
    print("5 - Ver Senhas Locais")
    print("6 - Ver Senhas na nuvem")
    print("0 - Sair")
    
    escolha = input("\nEscolha uma opção: ")

    if escolha == '1':
        n = input("Nome: ")
        g = input("Gmail: ")
        s = input("Senha: ")
        if cadastrar_usuario(n, g, s):
            print("✨ Usuário criado! Agora faça login.")

    elif escolha == '2':
        if logado:
            logado = False
            usuario_logado_gmail = None
            print("👋 Logout efetuado.")
        else:
            n = input("Nome: ")
            s = input("Senha: ")
            email = login_usuario(n, s)
            if email:
                logado = True
                usuario_logado_gmail = email
                print(f"✅ Bem-vindo, {n}!")
            else:
                print("❌ Nome ou senha incorretos.")

    elif escolha == '3':
        s_local = input("Digite a senha para guardar localmente: ")
        salvar_local(s_local)

    elif escolha == '4':
        if not logado:
            print("⚠️ Você precisa estar logado para usar a nuvem.")
        else:
            s_nuvem = input("Digite a senha para guardar na nuvem: ")
            salvar_na_nuvem(s_nuvem, usuario_logado_gmail)

    elif escolha == '5':
        listar_senhas_locais()
    elif escolha == '6':
        if not logado:
            print("⚠️ Você precisa estar logado para ver os dados da nuvem.")
        else:
            ver_senhas_online(usuario_logado_gmail)

    elif escolha == '0':
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")