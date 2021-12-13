import requests
import json

# ---------------- live trading ---------------------------

url = 'https://api.quiverquant.com/beta/live/senatetrading'
headers = {'accept': 'application/json',
'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'}
r = requests.get(url, headers=headers)

all_data = r.json()

with open('quiverquant/Senate/senatetrading_live.json', 'w') as file_object:
    json.dump(all_data, file_object)


# -------------------- historical trading -----------------------

file1 = open("US Equities.txt","r")
for ticker in file1.readlines():
    ticker = ticker.strip()
    all_data = f"https://api.quiverquant.com/beta/historical/senatetrading/{ticker}"
    headers = {
    'accept': 'application/json',
    'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
    'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'
    }
    try:
        r = requests.get(all_data, headers=headers)
        trading = r.json()
        if trading:
            with open('quiverquant/Senate/senatetrading_historical/'+ticker+'.json', 'w') as file_object:
                json.dump(trading, file_object)
            print("done with",ticker)
    except Exception as e:
        print(f'error with {ticker}')