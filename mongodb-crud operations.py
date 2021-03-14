#!/usr/bin/env python
# coding: utf-8

#importing pymongo package

import pymongo

#Connecting to mondodb compass
connection_url="mongodb://localhost:27017/" #MongoDB compass local host URL. You can replace the SRV string if you are connecting with mongodb atlas  
client=pymongo.MongoClient(connection_url)
client.list_database_names()#listing the available databases 

database_name="student_database"
student_db=client[database_name]#creating a database named student_database
collection_name="computer science"
collection=student_db[collection_name]#creating a collection in student_database
#inserting documents 

document={"Name":"Raj",
"Roll No":  153,
"Branch": "CSE"}
collection.insert_one(document)#insetring single document 


documents=[{"Name":"Roshan","Roll No":159,"Branch":"CSE"},{"Name":"Rahim","Roll No":155,"Branch":"CSE"},{"Name":"Ronak","Roll No":156,"Branch":"CSE"}]
collection.insert_many(documents)#inserting multiple documents

#Retrieving data from collection
query={"Name":"Raj"}
print(collection.find_one(query))#Retrieving single document


query={"Branch":"CSE"}
result=collection.find(query)#Retrieving multiple documents
for i in result:
    print(i)


result=collection.find({}).limit(2)#limiting the results
for i in result:
    print(i)


query={"Roll No":{"$eq":153}}
print(collection.find_one(query))# using filter to retrive document

#Updating documents in collection

query={"Roll No":{"$eq":153}}
present_data=collection.find_one(query)
new_data={'$set':{"Name":'Ramesh'}}
collection.update_one(present_data,new_data)#updating single document


present_data={"Branch":"CSE"}
new_data={"$set":{"Branch":"ECE"}}
collection.update_many(present_data,new_data)#updating multiple documents

#deleting documents from collection
query={"Roll No":153}
collection.delete_one(query)#deleting single document


query={"Branch":"ECE"}
collection.delete_many(query)#deleting multiple documents


#dropping collection

collection.drop()




