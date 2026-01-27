<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Security-Cryptography-red?style=for-the-badge&logo=pre-commit&logoColor=white" alt="Cryptography">
  <img src="https://img.shields.io/badge/Database-Hybrid-blue?style=for-the-badge&logo=postgresql&logoColor=white" alt="Database">
</div>

<h1 align="center">🔐 SentinelVault: Gerenciador Híbrido</h1>

<p align="center">
  <strong>Solução robusta de armazenamento de credenciais com criptografia de ponta e arquitetura flexível.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/petrakiio/NOME_DO_REPOSITORIO?style=flat-square" alt="Last Commit">
  <img src="https://img.shields.io/badge/Encryption-Fernet_128bit-green?style=flat-square" alt="Fernet">
  <img src="https://img.shields.io/badge/Auth-Bcrypt-orange?style=flat-square" alt="Bcrypt">
</p>

---

### 🛡️ Engenharia de Segurança
O **SentinelVault** não é apenas um banco de dados de senhas; é um estudo prático de defesa cibernética aplicada:

* **Proteção de Login:** Implementação de **Bcrypt** com salt dinâmico, tornando o sistema resistente a ataques de *Rainbow Tables* e Força Bruta.
* **Criptografia Simétrica (Fernet):** Todas as credenciais são encriptadas antes do armazenamento. Mesmo que o banco de dados ou o arquivo local seja invadido, os dados permanecem ilegíveis sem a chave mestra.
* **Persistência Híbrida:** Flexibilidade total para o usuário escolher entre **Local Vault** (offline em .txt criptografado) ou **Cloud Vault** (MySQL/PostgreSQL).
* **Zero Hardcoded Credentials:** Uso estrito de `python-dotenv` para garantir que nenhuma chave de acesso seja exposta no código-fonte.

---

### 🚀 Funcionalidades
- [x] **Auth System:** Login e cadastro seguro de usuários.
- [x] **Offline Mode:** Armazenamento local protegido por arquivo de chave física (`chave.key`).
- [x] **Cloud Sync:** Sincronização inteligente baseada no identificador do usuário logado.
- [x] **CLI Interativa:** Interface via linha de comando otimizada para agilidade.

---

### 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.10+
* **Segurança:** `Bcrypt` (Hash) e `Cryptography.Fernet` (Cipher).
* **Infraestrutura:** `python-dotenv` e `Pathlib` para gestão de arquivos.

---

### ⚙️ Configuração Rápida

1. **Dependências:**
   ```bash
   pip install cryptography bcrypt python-dotenv
