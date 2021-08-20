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

# Get the fields present in each document
drake_doc = drake.find_one() # extract one document from the collection
drake_fields = list(drake_doc.keys()) # extract the keys of the fields and turn it into a list

print(drake_fields)

# How many songs are contained within Drake's music catalog
# As each document represents a song lyrics, the total number of songs will be the total amount of documents
filter = {}
total_songs = drake.count_documents(filter)

print(total_songs)


# Name of albums within the entire collection
name_of_albums = list(drake.distinct("album"))

# Number of albums within the collection.
number_of_albums = len(name_of_albums)

# Number of songs per select albums
# We will write a for loop to iterate through the list of album names
for i in number_of_albums:
    sum = drake.count_documents({"album": i})
    print(sum)

# Most popular songs per album


# Search for a song from the collection using just the lyrics
# Search for all songs that contain the line "you promised me you would never change" using regular expressions
from bson.regex import Regex

c = {"lyrics": Regex("you promised me you would never change") }
drake.distinct("lyrics", c)

# Create an index to speed up queries








