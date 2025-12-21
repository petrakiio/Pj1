import os
from dotenv import load_dotenv
import conn
load_dotenv()

logado = None

# --- Funções ---
def cadastrar(nome,gmail,senha):
    try:
        cursor = conn.cursor
        table = os.getenv("DB_TABLE")
        sql = f"INSERT INTO {table} (nome, gmail, senha) VALUES (%s, %s, %s)"
        cursor.execute(sql,(nome,gmail,senha))
        conn.commit()
    except Exception as err:
        return False
    finally:
        conn.close()
        return True



opção = int(input("Fazer login para salvar os dados no banco?\n 1-Sim ou 1-Não"))

while True:
    if opção == 1:
        nome = input("Me diga seu nome:")
        senha = input("Me diga sua senha:")
        gmail = input("Me diga seu gmail:")
        retorno =  cadastrar(nome,gmail,senha)
        if not retorno:
            print("Cadastro falhou")
        else:
            print("Cadastro feito")
            logado = True
    elif opção == 2:
        print("Seu Dados seram salvos em arquivo txt local")
    else:
        opção2 = int(input("Deseja Sair?\n 1-Sim ou 2-Não"))
        if opção2 == 1:
            print("Fechando...")
            break
        elif opção2 == 2:
            print("Selecione uma opção valida por favor")
        else:
            print("Me diga uma opção valida por favor")

