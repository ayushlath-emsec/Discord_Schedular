import pymongo

# MongoDb Connection...
client =pymongo.MongoClient("mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority")

# Database Name
db =client['']

# Collection Name
collection =db['']

print ("Total Dicord channel in collection:", collection.count_documents())