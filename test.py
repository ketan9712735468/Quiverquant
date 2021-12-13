from tiingo import TiingoClient
import json
import requests

config = {}
config['session'] = True
config['api_key'] = "9292570d8a91fe15a742343f6dea0b536b65d0f5"

# Initialize
client = TiingoClient(config)

ticker_price = client.get_ticker_price("AAPL", frequency="daily",startDate='2021/05/17',endDate='2021/05/19')
tickers = client.list_stock_tickers()
ticker_metadata = client.get_ticker_metadata("GOOGL")
# print(tickers)


# file_name = open("test.json", mode="w")
# json.dump(tickers,file_name, indent=4)
all_data = {}
unique_ticker = []
for ticker in tickers:
    history = "https://api.quiverquant.com/beta/historical/senatetrading/"+ticker["ticker"]

    headers = {
    'accept': 'application/json',
    'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
    'Authorization': 'Token 8b5c9229cbf3d5a96e4bb79becbeca0e61b130f3'
    }
    r = requests.get(history, headers=headers)
    trading = r.json()
    print("}{+?>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.._+_+_+_",trading)













# import requests
# import json
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
# }
# data = requests.get("https://api.bseindia.com/BseIndiaAPI/api/ListofScripData/w?Group=&Scripcode=&industry=&segment=&status=",
#                                 headers= headers)

# file_name = open(r"c:/Users/admin/Documents/Jaydip/Test/Tiingo/test.json", mode="w")
# json.dump(data.json(),file_name, indent=4)


# from typing import List
# from io import StringIO
# from datetime import datetime
# import csv

# class TransactionSummary2:
#     @staticmethod
#     def calculate_summary(
#         person_info_csv_str: str, 
#         transaction_info_csv_str: str
#         ) -> List[dict]:
        
#         result = []
#         persons = csv.DictReader(StringIO(person_info_csv_str))
#         transactions = csv.DictReader(StringIO(transaction_info_csv_str))

#         transactions_list = []

#         for txn in transactions:
#             transactions_list.append(
#                 {
#                     "transaction_id": txn['transaction_id'],
#                     "transaction_date":txn['transaction_date'],
#                     "person_id":txn['person_id'],
#                     "type":txn['type'],
#                     "amount":txn['amount']
#                 }
#             )

#         for data in persons:
            
#             records = list(filter(lambda x : x['person_id'] == data['person_id'], transactions_list))
#             if len(records) == 0:
#                 result.append(
#                     {'name': data['person_name'], 'last_transaction_date': None, 'amount': 0}
#                 )
#             elif len(records) == 1:
#                 try:
#                     amount = int(records[0]['amount'])
#                 except:
#                     amount = 0
#                 result.append(
#                     {'name': data['person_name'], 
#                     'last_transaction_date': datetime.strptime(records[0]['transaction_date'], "%Y-%m-%d").strftime("%A %B %d %Y"), 
#                     'amount': (-1 * amount) if records[0]['type'] == 'WITHDRAW' else amount 
#                     }
#                 )
            
#             else:
#                 max_date = []
#                 amounts = []
#                 for record in records:
#                     max_date.append(datetime.strptime(record['transaction_date'], "%Y-%m-%d"))
#                     try:
#                         amount = int(record['amount'])
#                     except:
#                         amount = 0
#                     if record['type'] == 'WITHDRAW':
                       
#                         amounts.append(amount * -1)
#                     else:
#                         amounts.append(amount)
#                 print(amounts)
#                 result.append(
#                     {'name': data['person_name'], 
#                     'last_transaction_date': max(max_date).strftime("%A %B %d %Y"),
#                     'amount': sum(amounts)
#                     }
#                 )
#         return result


# person_info_csv_str = """\
# person_id,person_name,person_birthday
# 2,John Smith,1990-12-24
# 1,Jane Smith,2000-09-15
# 7,"Elisabeth, George",1991-11-06
# 3,Emma Watson,1986-04-18
# 10,Willy Wonga,1999-11-11
# """

# transaction_info_csv_str = """\
# transaction_id,transaction_date,person_id,type,amount
# 1,2020-10-11,1,DEPOSIT,100
# 2,2020-10-15,2,DEPOSIT,200
# 3,2020-10-16,1,WITHDRAW,50
# 4,2020-10-20,2,DEPOSIT,10
# """


# print(
#     TransactionSummary2().calculate_summary(
#         person_info_csv_str, 
#         transaction_info_csv_str
#     )
# )

# # print(
# #     TransactionSummary2().calculate_summary(
# #         person_info_csv_str, 
# #         transaction_info_csv_str
# #     )
# # )


# # var params = "?"
# #     Object.keys(profile).forEach(function(item) {
# #     if (profile[item]){
# #         params += `${item}=${profile[item]}`
# #     }