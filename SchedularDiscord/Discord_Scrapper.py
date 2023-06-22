# add necessary header files

from datetime import datetime , timezone ,date
from databaseConnection import *
import asyncio
from getfunc import *

# function to check status 
def scrapSuccess(func):
    collection.update_one({"channel_id":func},{'$set':{"isUrgent":False,"status":"done","time":datetime.now(),"failedCount":0}})
def scrapFailed(func , failedCount):
    collection.update_one({"channel_id":func},{'$set':{"isUrgent":False,"status":"error","time":datetime.now(),"failedCount":failedCount+1}})
def scrapRunning(func):
    collection.update_one({"channel_id":func},{'$set':{"status":"running","time":datetime.now()}})


# add your function here 

async def Discord_scrap_func(channel_id,id):
        print("Add your Discord Server Code")