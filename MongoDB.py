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
print(name_of_albums)

# Number of albums within the collection.
number_of_albums = len(name_of_albums)
print(number_of_albums)

# Number of songs per select albums
# We will write a for loop to iterate through the list of album names
for i in name_of_albums:
    sum = drake.count_documents({"album": i})
    print(sum)


# Top 10 most popular songs

songs = drake.find(
    filter = {},
    projection = {"lyrics_title": 1, "album": 1, "track_views": 1, "_id" : 0 }, # fields that will be displayed
    sort = [("track_views", -1)] # sort by track views, descending order
)

for song in songs [:10]:
    print(song)  # Print the documents

# Search for a song from the collection using just the lyrics
# Search for all songs that contain the line "But it's far from over" using regular expressions
from bson.regex import Regex # import regex from bson

c = {"lyrics": Regex("But it's far from over") }
results = drake.find(
    filter = c,
    projection = {"lyrics_title": 1, "album": 1, "track_views": 1, "_id" : 0 }, # fields that will be displayed
)

results = list(results)
print(results)# Displays information about the song

# Retrive lyrics of a particular song
# We will attempt to retrieve the lyrics of the song "Don't matter to me".

dmtm_lyrics = drake.find(
    filter ={"lyrics_title" : "Don't Matter to Me by Drake & Michael Jackson Lyrics"}, # We have to include the exact lyric title to retrieve the document
    projection = {"lyrics_title" : 1 , "lyrics" : 1, "_id" : 0} # Use projections to retrieve only lyrics title and lyrics. Exclude ID field
)

print(list(dmtm_lyrics)) # Use list method to display results


# Create an index to speed up queries

# First, we will time the unindexed query

import timeit

start = timeit.timeit()
#Beginning of query
for song in drake.find(
    filter = {},
    projection = {"lyrics_title": 1, "album": 1, "track_views": 1, "_id" : 0 }, # fields that will be displayed
    sort = [("track_views", -1)] # sort by track views, descending order
    ):

    print(song)

end = timeit.timeit()

print("The time it took to run the query is", start-end, "seconds") # Print elapsed time between 2 points

# create an index that helps speed up the above query

drake.create_index(
    [("lyrics_title", 1), ("album", 1), ("track_views", -1)])

#Run the same query after indexing
start = timeit.timeit()
#Beginning of query
for song in drake.find(
    filter = {},
    projection = {"lyrics_title": 1, "album": 1, "track_views": 1, "_id" : 0 }, # fields that will be displayed
    sort = [("track_views", -1)] # sort by track views, descending order
    ):

    print(song)

end = timeit.timeit()

print("The time it took to run the query is", start-end, "seconds") # Print elapsed time between 2 points


