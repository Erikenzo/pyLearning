#task https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
#notes https://cs50.harvard.edu/python/2022/notes/4/

# When running this script from CLI we need to pass number of BTC we want to buy with argv[1] value, it will return calculated price for those units.

import requests, sys

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit()
else:
    print('Missing command-line argument')
    sys.exit()

try:
    response_body = requests.get("https://api.coincap.io/v2/assets/bitcoin").json()
    priceUSD = round(float(response_body["data"]["priceUsd"]),4)
    print("$ {:,}".format(priceUSD*float(sys.argv[1])))
except requests.RequestException:
    print("There is no current price for BTC")
    sys.exit()