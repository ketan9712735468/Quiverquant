import requests
import json

# ---------------- live trading ---------------------------

url = 'https://api.quiverquant.com/beta/live/insiders'
headers = {'accept': 'application/json',
'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'}
r = requests.get(url, headers=headers)

all_data = r.json()

with open('quiverquant/Insider Trading/insiders.json', 'w') as file_object:
    json.dump(all_data, file_object)

