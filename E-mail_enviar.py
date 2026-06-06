import Arquivo_Notifica
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
load_dotenv()  # essa linha carrega o .env — estava faltando!
remetente = os.environ.get("EMAIL_USER")
senha = os.environ.get("EMAIL_PASS")
destinatario = "carater.cristo.h7@gmail.com"


def mensagem_funcion(parametro_lista):
    mensagem_str = ''
    for c in parametro_lista:
        mensagem = f"Hoje você as {c[0]}, você tem o seguinte compromisso: {c[1]}"
        mensagem_str += f"{mensagem} \n"
    return mensagem_str


mensagem_final = mensagem_funcion(Arquivo_Notifica.leitura())
print(mensagem_final)

msg = MIMEText(f"{mensagem_final}", "plain")
msg["From"] = remetente
msg["To"] = destinatario
msg["Subject"] = "Teste"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(remetente, senha)
    server.send_message(msg)
    print("E-mail enviado com sucesso!")

