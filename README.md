# 🖥️ Monitoramento de Logs com Alertas

Este projeto em Python simula um sistema de monitoramento de logs de servidor, detectando erros, gerando relatórios e enviando alertas por e‑mail. Ideal para aplicações de DevOps, suporte técnico e segurança da informação.

---

## 📦 Funcionalidades

- ✅ Leitura de logs a partir de arquivo `.log`
- 🔍 Detecção de erros com base em palavras-chave (`ERROR`)
- 📊 Geração de relatórios em `.txt` e `.csv`
- 📧 Envio automático de alertas por e‑mail via [SendGrid](https://sendgrid.com)
- 🧠 Classificação de falhas usando expressões regulares

---
monitoramento_logs/
├── monitor.py                    # Código principal
├── utils.py                        # Funções auxiliares
├── logs/
│   └── servidor.log        # Arquivo de log simulado
├── relatorios/
│   ├── erros.txt              # Relatório em texto
│   └── erros.csv              # Relatório em CSV
└── .env                # Chave da API SendGrid (não versionado)

---

## ⚙️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Niprotel4987/monitoramento_logs.git
   cd monitoramento_logs

---

