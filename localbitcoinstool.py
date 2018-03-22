import json
import requests
import time
from datetime import datetime
import smtplib

while True:
    r = requests.get("https://localbitcoins.com/sell-bitcoins-online/US/united-states/ebay-gift-card-code/.json")
    data = r.json()

    # This prints all JSON data with a readable format
    #print(json.dumps(data, indent=2))

    # This prints relevant JSON data
    for item in data["data"]["ad_list"]:
        price = item["data"]["temp_price"]
        print("$" + price)

    if float(price) >= 15000:
        content = 'The price is now above 15k'
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('danieljsocial@gmail.com', 'rlhbjjhdobmorkgn')
        mail.sendmail('danieljsocial@gmail.com', 'daniel11fain@gmail.com', content)
        mail.close()
    else:
        print(str(datetime.now()))
        time.sleep(60)
