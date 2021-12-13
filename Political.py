import time
import requests
import json
from termcolor import cprint

# ---------------- live trading ---------------------------

# url = 'https://api.quiverquant.com/beta/live/politicalbeta'
# headers = {'accept': 'application/json',
# 'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
# 'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'}
# r = requests.get(url, headers=headers)

# all_data = r.json()

# with open('quiverquant/Political Beta/politicalbeta_live.json', 'w') as file_object:
#     json.dump(all_data, file_object)


# -------------------- historical trading -----------------------

count = 0
file1 = open("political.txt","r")
for ticker in file1.readlines():
    ticker = ticker.strip()
    if count%1 == 0:
        time.sleep(10)
    all_data = f"https://api.quiverquant.com/beta/historical/politicalbeta/{ticker}"
    headers = {
    'accept': 'application/json',
    'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
    'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'
    }
    try:
        r = requests.get(all_data, headers=headers)
        trading = r.json()
        if trading:
            with open('quiverquant/Political Beta/politicalbeta_historical/'+ticker+'.json', 'w') as file_object:
                json.dump(trading, file_object)
            print(f"done with {ticker}")
    except Exception as e:
        cprint(f'error with {ticker}',color="red")
    count = count + 1