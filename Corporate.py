import requests
import json
import time
import asyncio

# ---------------- live trading ---------------------------

# url = 'https://api.quiverquant.com/beta/live/lobbying'
# headers = {'accept': 'application/json',
# 'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
# 'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'}
# r = requests.get(url, headers=headers)

# all_data = r.json()

# with open('quiverquant/Corporate Lobbying/lobbying_live.json', 'w') as file_object:
#     json.dump(all_data, file_object)


# -------------------- historical trading -----------------------

async def main():
    file1 = open("US Equities.txt","r")
    for ticker in file1.readlines():
        ticker = ticker.strip()
        all_data = f"https://api.quiverquant.com/beta/historical/lobbying/{ticker}"
        headers = {
        'accept': 'application/json',
        'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
        'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'
        }
        try:
            r = requests.get(all_data, headers=headers)
            trading = r.json()
            if trading:
                with open('quiverquant/Corporate Lobbying/lobbying_historical/'+ticker+'.json', 'w') as file_object:
                    json.dump(trading, file_object)
                print("done with",ticker)
        except Exception as e:
            print(f'error with {ticker}')
        await asyncio.sleep(5)

asyncio.run(main())