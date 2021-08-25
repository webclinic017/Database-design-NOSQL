## Database-design-NOSQL
Step-by-step guide to prescribing and designing NOSQL databases. Within this repository we will discuss what NOSQL databases are, the various architectural patterns in which they can be set up. We will also migrate data into, and design 2 sample NOSQL databases. 

### Table of contents

### What are NOSQL databases?

NOSQL databases refer to "Not only SQL" databases. These are databases that are typically alternatives to relational databases, although NOSQL databases can store relational data also. 

### Why are they necessary?


### Architecture patterns of NOSQL databases:

4 types of NOSQL database architectures patterns:

1) Key Value stores
2) Graph stores
3) Column family stores
4) Document stores
 
 We would explain all the above patterns here and discuss their use cases
 
 **Key value stores**
 
 In this pattern, a unique keys are assigned to certain data values. These block of data values are retrieved using those unique keys. Any type of data (HTML code for websites, text, videos, image binaries...etc) can be stored within these types of databases, while the unique keys are simply text strings.
 This type of data store is similar to a dictionaries where the name of the word being looked up represents the key, while the other contents such as the meaning, pronunciation and image might represent the data block. 
 There is generally no way to search or retrieve portions of the data within the data block being stored. 
 
 
**_Advantages of key-value stores_**:
 
 They are quite simple, and save time and costs by moving the focus from architectural design.
 
 They are very scalable and reliable
 
 Portability and lower operational costs
 
 Very flexible as a general purpose tool (No schema)
 
 
 **_Use of key value store_**
 
3 commands used to manipulate values within the database

PUT: insert a key value pair into a database

GET: retrieve a value using a supplied key

DELETE: remove a key value pair from the database


**_Typical use case for key value stores_**

Web search engines - the URLs represent the key to the website, while the contents of the website represents the value being stored. The contents of the website are then indexed for quick searches.

Amazon S3 bucket - All objects all stored in buckets using key/object pairs.

Other uses include dictionary, image store, query cache, lookup tables


 
 **Graph Stores**
 
 Graphical store is a system that contains a sequence of nodes and relationships that make up a graph. A graph store has 3 data fields namely, notes, relationships and properties. 
 They are ideal when many items (with various properties) that are related to each other in complex ways. In this type of store, simple queries can be made to show the nearest neighboring nodes as well as queries to find patterns. 
 
 Graph nodes are usually representations of real-world entities like nouns (People, telephone numbers, web pages...etc).
  
 
 **_Characteristics of graph stores_**
 
 Nodes have unique identifiers are assigned using uniform resource identifiers (URIs)
 
 Standard of creating URIs to create explicit node identifiers node is called a resource description format (RDF)
 
 The relationship that connects 2 nodes (subject and objects) is called a predicate
 ![node-predicate](https://user-images.githubusercontent.com/83844773/129314974-9462a888-a348-492c-8ea6-913385fd07b5.PNG)
 
 
 **_Advantages of graph stores_**
 
 Can efficiently perform join operations
 
 Computationally lightweight and faster compared to RDMS
 
 
 **_Disadvantages of graph stores_**
 
 Difficult to scale on multiple servers due to the close connectedness of each node in the graph.
 
 
 **_Typical use cases_**
 
 Link analysis - To perform searches and look for patterns and relationships in situations such as social networking. Popular social networking apps use this type to recommend new contacts or connections with individuals that have mutual friends, location or backgrounds. Graph stores can perform these kinds of queries much faster than a RDBMS.
 
 Rules and inference - These are used to run queries on complex structures (e.g. Class libraries, taxonomies and rule based systems)
 
 Integrating linked data - This sort of store can be used to perform real time integration of large amounts of open linked data, without necessarily storing the data.
 This involves joining together different data from different sources automatically using a tool such as linked open data (LOD). 
 
 
 **Column family stores**
 
 This type of NOSQL store is similar to the relational database in the sense that they have rows and columns. However, it does not support joins. Both columns and rows have general purposes keys for data lookup, however they lack other features such as typed columns, secondary indexes, triggers and query languages. 
 In contrast with key value stores that utilize a single key, the column family store utilizes various attributes that serve as the keys such as row identifiers, column name, column family and timestamp. These keys uniquely identifies and corresponds to a certain value. 
 
 **_Advantages of column family store_**
 
 High scalability. Column family stores do not rely on joins, so they scale well on distributed systems
 
 Contain inbuilt automatic fail over built in to detect failing nodes and algorithms to identify corrupt data
 
 Designed to work in distributed filesystems (e.g. Hadoop) and MapReduce transforms.

 High availability - the ability to replicate data on multiple nodes in a network. 
 
 Easy to write in new data.
 
 **_Typical use cases_**
 
 Analytical information in Bigtable - Bigtable is used to store website usage information in Google Analytics, which help track who is visiting a website. When a user clicks on a web page, the hit is stored in a single row-column entry that has the URL and a timestamp as the row ID. 
 
 Google Maps storing geographic information in Bigtable - Used to store longitude and latitude coordinates of geographic points on earth and the moon, allowing users to zoom into and out of places using a 3D- graphical interface.
 
 
 **Document stores**

Quite similar to key-store, however it stores documents rather than "values". These documents are made up of named data and could be nested within other documents.
Unlike key-value and column family stores that aren't indexed or searchable, almost any item within the documents store can be retrieved. Everything inside a document is automatically indexed whenever a new document is added. 
Document store database do not require a schema but each document has a primary key, which uniquely identifies the document.

**_Characteristics of document stores_**

Document collections - Document stores group documents into collections similar to directory structures, which helps effectively manage the large document stores. Collections can also contain various collections.

Application collections - collections within document stores can be used as containers for web application packages.

Document store APIs - Each document store has an API (query language) that specifies the path to the various nodes. 

Implementation of document stores - The implementation of document stores could either be simpler document structure and may use JSON format or complex structure in true document stores.


**_Use cases_**

Ad server in Mongo DB 

## NOSQL database creation and use

Within this repository we will migrate data into, and query data from 2 patterns of NOSQL databases. These examples will be taken to highlight the characteristics of both types of databases

These database architecture patterns are as follows;

1) Key Value Stores
2) Document stores

The other 2 types will be discussed in a subsequent guide.

For the key value stores database we will make use of the in-memory database called **Redis**. While for the document store, **MongoDB Atlas** will be utilized. 
All code will be written in python, hence we will make use of the drivers for the respective databases.

### Key Value Stores - (Demonstrated using Redis)

### Document Stores - (Demonstrated using MongoDB Atlas)

To show the characteristics of document stores, we will be making use of MongoDB Atlas. Mongo DB Atlas is a cloud based database developed by the makers of MongoDB. 

In order to follow this guide, one will need to create a profile and clusters on the MongoDB servers.

To get started (deploying clusters, creating an account...etc) with MongoDB, visit the attached link: [https://docs.atlas.mongodb.com/getting-started/](https://docs.atlas.mongodb.com/getting-started/)


#### The data 
The data we will be migrating and analysing using the MongoDB database are the lyrics of all of Drake's music catalogue. These lyrics are contained in separate documents within a single JSON file. 

The data is named __drake_data.jason__ and is available in this link: [https://www.kaggle.com/juicobowley/drake-lyrics?select=drake_data.json](https://www.kaggle.com/juicobowley/drake-lyrics?select=drake_data.json)

The fields within the various documents are very self-explanatory and are labeled as follows "Album", "Lyrics_title", "Lyrics_URL", "Lyrics" and "Track_views"

To make use of the data within the database we created a database named "lyrics". Within the database we created a collection named "drake". If we decide to add other artists' lyrics, we will simply create separate collection for each artist.

From the image below we can see the database and collection (see the blue rectangle) created with within the newly created mongoDB cluster

The red rectangle encircles 2 documents that represent song lyrics from Drake's latest album "Certified lover boy". From this view,we can see the schema of each document. 

![MongoDB view](https://user-images.githubusercontent.com/83844773/130481021-8ade0572-927d-43ef-b741-52bac09c44cc.png)

### Problems our database will help solve

Imagine we were creating an app that will help users look up lyrics for available artists. 
What kinds of information will the app need to display? For one, I want to be able to search for a song using only a portion of the lyrics.
I would like to be able to see information about the various albums. For instance the number of songs in a certain album, and the most popular songs (Song with the highest number of views). 
I would also like to create an app that is responsive and gives me results quickly.

As a result,the following questions we will answer will be as follows:

1) How many songs are contained with drake's musical catalog?
2) Number of albums within the dataset?
3) Names of the albums within the dataset?
4) Number of songs (documents) per album?
5) What are the 10 most popular songs?
6) Can we perform a search of portions of lyrics ?
7) Create an index to speed up queries.

We show the code needed to answer the queries. We will also display results gotten from the python console.

_How many songs are contained within Drake's musical catalog?_

```` python
# How many songs are contained within Drake's music catalog
# As each document represents a song lyrics, the total number of songs will be the total amount of documents
filter = {}
total_songs = drake.count_documents(filter)

````
![NOSQL MONGO1](https://user-images.githubusercontent.com/83844773/130569411-e225760c-e30e-4fae-9822-fdc71b310cab.png)


_What are the names of the albums within the collection?_

```` python
# Name of albums within the entire collection
name_of_albums = list(drake.distinct("album"))
print(name_of_albums)
````
![NOSQL mongo 2](https://user-images.githubusercontent.com/83844773/130569424-65a683ed-2183-4872-8e3a-ab07fee31494.png)


_How many albums are within the collection?_

```` python
# Number of albums within the collection.
number_of_albums = len(name_of_albums)
print(number_of_albums)
````
![nosql mongo 7](https://user-images.githubusercontent.com/83844773/130569973-ad95bc19-17c4-4751-bb52-3dd9f06e889e.png)


_How many songs contained within each album?_

```` python
# Number of songs per select albums
# We will write a for loop to iterate through the list of album names
for i in name_of_albums:
    sum = drake.count_documents({"album": i})
    print(sum)
````
![NOSQL mongo 3](https://user-images.githubusercontent.com/83844773/130569436-228ac5aa-0d1a-498b-b283-147ac66ae4d5.png)


_What are the 10 most popular songs?_

```` python
# Top 10 most popular songs

songs = drake.find(
    filter = {},
    projection = {"lyrics_title": 1, "album": 1, "track_views": 1, "_id" : 0 }, # fields that will be displayed
    sort = [("track_views", -1)] # sort by track views, descending order
)

for song in songs [:10]:
    print(song)  # Print the documents
````
![NOSQL mongo 4](https://user-images.githubusercontent.com/83844773/130569442-c738ed5d-a87f-4224-a0ce-a9c7b85da782.png)


_Can we perform a search of portions of lyrics?_

```` python
# Search for a song from the collection using just the lyrics
# Search for all songs that contain the line "But it's far from over" using regular expressions
from bson.regex import Regex # import regex from bson

c = {"lyrics": Regex("But it's far from over") }
results = drake.find(
    filter = c,
    projection = {"lyrics_title": 1, "album": 1, 
        "track_views": 1, "_id" : 0 }, # fields that will be displayed
)

results = list(results)
print(results)# Displays information about the song
````
![NOSQL mongo 5](https://user-images.githubusercontent.com/83844773/130569451-aca1b9d3-c94e-4296-91c9-bc01c2de00ba.png)


_Can we search for a song using the title of the song?_

````python

dmtm_lyrics = drake.find(
    filter ={"lyrics_title" : "Don't Matter to Me by Drake & Michael Jackson Lyrics"}, # We have to include the exact lyric title to retrieve the document
    projection = {"lyrics_title" : 1 , "lyrics" : 1, "_id" : 0} # Use projections to retrieve only lyrics title and lyrics. Exclude ID field
)

print(list(dmtm_lyrics)) # Use list method to display results

````
![NOSQL mongo 6](https://user-images.githubusercontent.com/83844773/130569462-ae0228b1-1fe8-4824-9d32-d0c0dff75255.png)


_Can we speed up the common queries?_

Imagine we had millions of documents within our collection and on the app, we intend to display the most popular songs per collection.
This operation will probably take a while and might be computationally demanding. Through indexing, we can create a look up table for finding documents users need frequently. 

Using the code below, we will compare the un-indexed and indexed queries to rank all the songs within the collection by the number of views:
```` python
 # Create an index to speed up query
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
````

![Index 1](https://user-images.githubusercontent.com/83844773/130566096-1a0a50a7-d689-4e13-ae85-19e937b2f35c.png)
![index 2](https://user-images.githubusercontent.com/83844773/130566102-50ebdea9-ee83-4520-9d4d-f1c264fc4f65.png)

From the above images, there was a 96% reduction in query time. Pretty impressive.
