from typing import Counter
import requests
import json
import time
from datetime import date, datetime

from termcolor import cprint


# ---------------- live trading ---------------------------

# url = 'https://api.quiverquant.com/beta/live/congresstrading'
# headers = {'accept': 'application/json',
# 'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
# 'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'}
# r = requests.get(url, headers=headers)

# all_data = r.json()

# with open('quiverquant/Congress/congresstrading_live.json', 'w') as file_object:
#     json.dump(all_data, file_object)


# -------------------- historical trading -----------------------

# call = 0
# start_time = datetime.now()
# file1 = open("US Equities.txt","r")
# for ticker in file1.readlines():
#     if diff < 60 and call >= 999:
#         time.sleep(60-diff+1)
#         start_time = datetime.now()
#     ticker = ticker.strip()
#     all_data = f"https://api.quiverquant.com/beta/historical/congresstrading/{ticker}"
#     headers = {
#     'accept': 'application/json',
#     'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
#     'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'
#     }
#     try:
#         r = requests.get(all_data, headers=headers)
#         trading = r.json()
#     except Exception as e:
#         print(f'error with {ticker}')
#     end_time = datetime.now()
#     if trading:
#         with open('quiverquant/Congress/congresstrading_historical/'+ticker+'.json', 'w') as file_object:
#             json.dump(trading, file_object)
#         print("done with",ticker)
#     call = call+1
#     diff = (end_time-start_time).total_seconds()



call = 0
file1 = open("a.txt","r")
for ticker in file1.readlines():
    if call%1 == 0:
        time.sleep(10)
    ticker = ticker.strip()
    all_data = f"https://api.quiverquant.com/beta/historical/congresstrading/{ticker}"
    headers = {
    'accept': 'application/json',
    'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
    'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'
    }
    try:
        r = requests.get(all_data, headers=headers)
        trading = r.json()
    except Exception as e:
        cprint(f'error with {ticker}')
    if trading:
        with open('quiverquant/Congress/congresstrading_historical/'+ticker+'.json', 'w') as file_object:
            json.dump(trading, file_object)
        print("done with",ticker)
    call += 1