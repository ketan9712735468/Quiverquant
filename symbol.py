import requests
import csv
import json

# with open('Final_data.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     next(csv_reader)

    # unique_ticker = []
    # for i in csv_reader:
    #     # unique_ticker.append(i)
    #     history = "https://api.quiverquant.com/beta/historical/senatetrading/"+i[0]

    #     headers = {
    #     'accept': 'application/json',
    #     'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
    #     'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'
    #     }

    #     r = requests.get(history, headers=headers)
    #     trading = r.json()
    #     if trading:
    #         with open('senatetrading_historical/'+i[0]+'.json', 'w') as file_object:
    #             json.dump(trading, file_object)


# -----------------Read txt file-----------------------

# file1 = open("US Equities.txt","r")
# for ticker in file1.readlines():
#     ticker = ticker.strip()
#     history = f"https://api.quiverquant.com/beta/historical/senatetrading/{ticker}"
#     headers = {
#     'accept': 'application/json',
#     'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
#     'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'
#     }
#     try:
#         r = requests.get(history, headers=headers)
#         trading = r.json()
#         if trading:
#             with open('json/'+ticker+'.json', 'w') as file_object:
#                 json.dump(trading, file_object)
#             print("done with",ticker)
#     except Exception as e:
#         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>e")
#         print('--------------------------',ticker)


# ----------------------xml file get senator data-----------------------------------

# from bs4 import BeautifulSoup
# import xml.etree.cElementTree as et

# tree=et.parse('year/2008FD/2008FD.xml')
# root=tree.getroot()
# first = []
# last = []

# for time in root.iter('Last'):
#     first.append(time.text)
# for time in root.iter('First'):
#     last.append(time.text)

# def merge(lst1, lst2):
#     return[a+' '+b for (a,b) in zip(lst1, lst2)]

# data = []
# for i in merge(first,last):
#     if i in data:
#         continue
#     else:
#         data.append(i)
# print(data)


# ---------------------------------------------

import json

f = open('master.json')
all_data = json.load(f)

senator = []
aapl_list = {}

for data in all_data:
    if data['Senator'] not in aapl_list:
        aapl_list[data['Senator']] = 1
        senator.append(data)

for i in senator:
    data = json.load(open('master.json', mode='r'))

    listed = list(filter(lambda x: x['Senator'] == i['Senator'], data))

    with open('senator/'+i['Senator']+'.json', 'w') as file_object:
        json.dump(listed, file_object)