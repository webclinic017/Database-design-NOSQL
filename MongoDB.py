# import pymongo
import pymongo

# Verify pymongo version
pymongo.version

# import MongoClient
from pymongo import MongoClient

# create client connection
client = MongoClient('mongodb+srv://dbuser:'
                     'password1234@cluster0.gq30y.mongodb.net/Lyrics?retryWrites=true&w=majority')
# Assign database
db = client.Lyrics

# create collections
drake = db.drake
kanye = db.kanye

# insert json data into database
# import json file
import json

# open json file
with open('drake_data.json') as file:
    file_data = json.load(file)

# insert into drake collection
drake.insert_many(file_data)






