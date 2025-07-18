# 🔐 Rotina de Criptografia de Senhas para Arquivo `.env`

Este projeto implementa uma rotina segura de **criptografia e descriptografia de variáveis sensíveis** como senhas, tokens e chaves de acesso, evitando o armazenamento em texto plano no arquivo `.env`.

> ⚠️ Objetivo: Garantir a **confidencialidade de credenciais** e melhorar o nível de maturidade em segurança da aplicação, mantendo compatibilidade com práticas DevOps modernas.

---

## 🧰 Tecnologias Utilizadas

- Python 3.10+
- [cryptography (Fernet)](https://cryptography.io)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📁 Estrutura do Projeto

```bash
projeto/
│
├── encryptor.py          # Utilitário para criptografar valores
├── secret.key            # Chave secreta para criptografia simétrica (NÃO versionar)
├── .env                  # Arquivo de variáveis de ambiente com senha criptografada
├── main.py               # Script que carrega e descriptografa a senha
└── README.md             # Este arquivo
