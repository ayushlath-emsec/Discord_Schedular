from Discord_Scrapper import *
from bson import ObjectId
from Database_Connection import *
from flag import *
import asyncio


def getfunction(func):
    print("Scrapping in progress...")
    channel_id = func['channel_id']
    channel_name = func['channel_name']
    failedCount = func['failedCount']
    _id = func['_id']
    isNodeBusy = True
    try:    
        print(channel_name + " is scrapping now")
        scrapRunning(channel_id)
        asyncio.run(Discord_scrap_func(channel_id,ObjectId(_id)))
        scrapSuccess(channel_id)
        print(channel_name + " Scrapped Succesfully")
    except:
        print(channel_name + " Scrapping Failed")
        print("FailedCount of Discord Channel {channel_name} : " , (failedCount+1) )
        scrapFailed(channel_id , failedCount)       
        
    isNodeBusy = False