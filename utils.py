import os
import csv
import re
import smtplib
from email.mime.text import MIMEText

def verificar_erro(linha_log):
    return "ERROR" in linha_log

def contar_erros(lista_logs):
    return [log for log in lista_logs if verificar_erro(log)]

def exportar_erros_txt(erros, caminho="relatorios/erros.txt"):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        for erro in erros:
            f.write(erro + "\n")

def exportar_erros_csv(erros, caminho="relatorios/erros.csv"):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Erro"])
        for erro in erros:
            writer.writerow([erro])

def enviar_alerta(erros, limite=3):
    if len(erros) >= limite:
        corpo = f"Foram encontrados {len(erros)} erros:\n" + "\n".join(erros)
        msg = MIMEText(corpo)
        msg["Subject"] = "🚨 Alerta de Erros no Servidor"
        msg["From"] = "seuemail@gmail.com"
        msg["To"] = "destinatario@gmail.com"

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login("seuemail@gmail.com", "sua_senha_de_app")
                server.send_message(msg)
        except smtplib.SMTPAuthenticationError:
            print("⚠️ Falha na autenticação SMTP. Verifique o e-mail e a senha de app.")

def detectar_falhas_regex(logs):
    padroes = {
        "Banco de Dados": r"ERROR.*banco de dados",
        "Autenticação": r"ERROR.*autentic",
        "Memória": r"WARNING.*memória"
    }
    resultados = {}
    for nome, regex in padroes.items():
        encontrados = [log for log in logs if re.search(regex, log, re.IGNORECASE)]
        resultados[nome] = encontrados
    return resultados

def ler_logs_arquivo(caminho):
    if not os.path.exists(caminho):
        print(f"⚠️ Arquivo de log não encontrado: {caminho}")
        return []
    with open(caminho, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f.readlines()]

