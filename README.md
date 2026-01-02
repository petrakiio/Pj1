🔐 SentinelVault: Gerenciador Híbrido de Senhas
O SentinelVault é uma solução robusta de segurança desenvolvida em Python para o armazenamento seguro de credenciais. O sistema opera de forma híbrida, permitindo que o usuário escolha entre o armazenamento local criptografado ou a sincronização em nuvem via banco de dados.

🛡️ Diferenciais de Segurança
Hash de Autenticação: Utiliza bcrypt com salt dinâmico para garantir que as senhas de login nunca sejam armazenadas em texto simples.

Criptografia Simétrica (Fernet): Todas as senhas salvas são encriptadas com chaves de 128 bits antes de tocarem o disco ou o banco de dados.

Arquitetura Híbrida: Integração com banco de dados MySQL/PostgreSQL (via variáveis de ambiente) e persistência local em arquivos .txt.

Segurança de Variáveis: Uso de python-dotenv para proteger credenciais de acesso ao banco de dados.

🚀 Funcionalidades
Cadastro e Login: Sistema de autenticação de usuários seguro.

Vault Local: Armazenamento offline protegido por chave local (chave.key).

Vault Online: Sincronização em nuvem baseada no Gmail do usuário logado.

Interface CLI: Menu interativo para gerenciamento ágil.

🛠️ Tecnologias Utilizadas
Python 3.10+

Bcrypt: Para hashing de senhas.

Cryptography (Fernet): Para encriptação de dados.

Dotenv: Para gestão de variáveis de ambiente.

Pathlib: Para manipulação segura de caminhos de arquivos.

⚙️ Como configurar
Configure seu banco de dados no arquivo .env.

Instale as dependências: pip install cryptography bcrypt python-dotenv

Execute o sistema: python sentinel_vault.py
