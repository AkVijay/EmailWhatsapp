

import json
from bs4 import BeautifulSoup
from twilio.rest import Client
import requests
from requests.auth import HTTPBasicAuth
import time
import settings

account_sid = settings.twillio_account_sid
auth_token = settings.twillio_auth_token
client = Client(account_sid, auth_token)



def email_sendingFund():
    url = 'https://mail.google.com/mail/feed/atom'
    print (url)

    response = requests.get(url, auth=HTTPBasicAuth(settings.email_id, settings.password))
    soup = BeautifulSoup(response.text, 'html.parser')
    entries = soup.find_all('entry')

    for entry in entries:
        if(str(entry.email).find('credit') != -1):
            message = client.messages.create(
                body = entry.title,
                from_=settings.whatsAppFrom,
                to=settings.whatsAppTo
            )


while True :
    email_sendingFund()
    time.sleep(86400)

