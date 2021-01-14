from mailjet_rest import Client
import os

email_sender = "ruanpablomp@gmail.com"
email_name = "Email Campaigne Ruan"

API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']


#EmailSender = email da aplicacao
#EmailSender = email da aplicacao

mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')
def send_mail(email_dest, name_dest, link_wll_clicked):
    data = {
        'Messages': [
            {
            "From": {
                "Email": f"{email_sender}",
                "Name": f"{email_name}"
            },
            "To": [
                {
                "Email": f"{email_dest}",
                "Name": f"{name_dest}"
                }
            ],
            "Subject": f"{title}",
            "TextPart": "Greetings from Mailjet!",
            "HTMLPart": f"<h3>Teste, Bem Vindo a minha aplicação de campanhas de email <a href=\"{link_wll_clicked}\">Mailjet</a>!</h3><br />May the delivery force be with you!"
            }
        ]
    }

    result = mailjet.send.create(data=data)
    print(result.status_code)