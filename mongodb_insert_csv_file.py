import pandas as pd
import pymongo
import json

# establish database connection to MongoDB server
mongo_client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")

#creating database name and collection name in server
database_name = mongo_client["airps"]
collection_name = database_name["sensor"]

data_file_path = "E:\PYTHON\MongoDB\mongoDB\dataset\Scania_APS_failure_prediction.ipynb"

df = pd.read_csv(data_file_path)
print(f"rows and columns: {df.shape}")


#convert dataset into json file so that we can dump these record in mongodb
#droping the default index
df.reset_index(drop=True, inplace=True)
json_record = list(json.loads(df.T.to_json()).values())
print(json_record[0])
    
#insert record to mongodb
collection_name.insert_many(json_record)
# client[database_name][collection_name].insert_many(json_record)

