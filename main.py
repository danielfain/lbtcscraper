import json
import requests
import time
from datetime import datetime
import smtplib

while True:
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/")
    data = r.json()

    btc_price = data[0]["price_usd"]
    btc_percent_change = data[0]["percent_change_24h"]

    if float(btc_price) < 8000:
        content = 'Bitcoin is below $8,000'
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('danieljsocial@gmail.com', 'rlhbjjhdobmorkgn')
        mail.sendmail('danieljsocial@gmail.com', 'daniel11fain@gmail.com', content)
        mail.close()

    if float(btc_percent_change) > 10:
        content = "Bitcoin has gained 10% in value"
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('danieljsocial@gmail.com', 'rlhbjjhdobmorkgn')
        mail.sendmail('danieljsocial@gmail.com', 'daniel11fain@gmail.com', content)
        mail.close()
    elif float(btc_percent_change) < -10:
        content = "Bitcoin has dropped 10% in value"
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('danieljsocial@gmail.com', 'rlhbjjhdobmorkgn')
        mail.sendmail('danieljsocial@gmail.com', 'daniel11fain@gmail.com', content)
        mail.close()

    print(f"Bitcoin: ${btc_price} ({btc_percent_change}%)")
    time.sleep(120)
