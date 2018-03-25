import json
import requests
import time
from datetime import datetime
import balloon

# Known scammers I don't want to list
blacklist = ['GemsBitcoins', 'TechnoTrade', 'TraderProMagic']

while True:
    r = requests.get("https://localbitcoins.com/sell-bitcoins-online/US/united-states/ebay-gift-card-code/.json")
    data = r.json()

    # This prints all JSON data with a readable format
    #print(json.dumps(data, indent=2))

    # This prints relevant JSON data
    for item in data["data"]["ad_list"]:
        price = item["data"]["temp_price"]
        trades = item["data"]["profile"]["trade_count"]
        user = item["data"]["profile"]["username"]
        if user not in blacklist:
            print(f"{user}({trades}): ${price}")

    if float(price) >= 15000:
        # Windows notification (found the code on github) (title, message)
        balloon.balloon_tip('Localbitcoins Ebay', 'Price is now above $15,000')
        time.sleep(180)
    else:
        print(str(datetime.now()))
        print("\n")
        time.sleep(60)
