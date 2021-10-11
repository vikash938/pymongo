import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["university"]
collection = db["colleges"]
#for insert one data
data = {"department":"Science",
        "students":{
            "name":"Rad",
            "class":"B.Sc. 1st Year",
            "Rollnumber":"39"
            },
        "subject":["Mathematics","Physics","Chemistry"]

        }
#using insert_one to upload data in db
x = collection.insert_one(data)
print(x)
list_of_data = [{"department":"Commerce",
                 "students":{
                     "name":"Jam",
                     "class":"B.Com 1st Year",
                     "Rollnumber":"23"
                     },
                 "subject":["Accounts","finance","Business"]

                },
                {"department":"Arts",
                 "students":{
                     "name":"Bala",
                     "class":"B.A. 1st Year",
                     "Rollnumber":"14"
                     },
                 "subject":["History","Geography","English Literature"]

                },
                {"department":"Computer",
                 "students":{
                     "name":"Oesin",
                     "class":"B.C.A. 1st Year",
                     "Rollnumber":"49"
                     },
                 "subject":["Fundamental of programming","Data Structure"]
                }

                ]
#using insert_many to insert list of documents in db
x = collection.insert_many(list_of_data)
print(x)


# To print all documents use find method with for loop 
for doc in collection.find():
    print(doc)






