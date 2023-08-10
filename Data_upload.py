import requests
import time
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://1234:1234@cluster0.scppxjp.mongodb.net/?retryWrites=true&w=majority")
db = client.FinalProject  # Use the "Finalproject" database
collection = db.NBA  # Use the "NBA" collection

while True:
    r = requests.get('https://nba-stats-db.herokuapp.com/api/playerdata/topscorers/total/season/2023/')
    if r.status_code == 200:
        data = r.json()
        collection.insert_one(data)  # Insert data into the collection
        print(data)
        time.sleep(86200)
    else:
        exit()






