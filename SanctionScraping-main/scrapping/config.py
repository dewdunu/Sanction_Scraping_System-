HEADER = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/50.0.2661.102 Safari/537.36 '
}

import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.vtipj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["sanctions_db"]
sanctions = db["sanctions"]
