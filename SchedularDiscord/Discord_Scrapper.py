# add necessary header files
import requests
import json
import pandas as pd
from datetime import datetime , timezone ,date
from Database_Connection import *
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
    num = 0
    limit = 100
    content=[]
    channelid=[]
    author=[]
    date=[]
    id=[]
    is_thread=[]
    thread_id=[]
    thread_last_id=[]
    attachments=[]
    headers = {
        'authorization': {"enter your authorization key"}
    }

    last_message_id =None

    while True:
        query_parameters = f'limit={limit}'
        if last_message_id is not None:
            query_parameters += f'&before={last_message_id}'

        r = requests.get(
            f'https://discord.com/api/v9/channels/{channel_id}/messages?{query_parameters}',headers=headers
            )
        jsonn = json.loads(r.text)
        if len(jsonn) == 0:
            break

        for value in jsonn:
          # if value[]
            try:
             id1= value['thread']['id']
            #  dic=thread_messages(id1,None)
             thread_id.append(id1)
            #  thread_last_id.append(dic["last_message_id"])
             is_thread.append(True)

            except:
              thread_id.append(None)
              # thread_last_id.append("")
              is_thread.append(False)

            if len(value['embeds'])>0:
              try:
                if value['embeds'][0]['type']=='rich':
                  content.append(f"{value['content']} \n url_title: {value['embeds'][0]['description']}")
                else:
                   content.append(f"{value['content']} \n url_title: {value['embeds'][0]['title']}")
              except:
                content.append(value['content'])
            else:
              content.append(value['content'])
            if len(value['embeds'])>0:
              # print(list(value.keys()),(value['embeds'][0]), '\n')
              channelid.append(value['channel_id'])
              author.append(value['author']['username'])
              date.append(int(datetime.fromisoformat(value['timestamp']).timestamp()))
              id.append(value['id'])
              last_message_id = value['id']

            if len(value['attachments'])>0:
              attachment=[]
              for i in range(len(value['attachments'])):
                attachment.append({'filename':value['attachments'][i]['filename'],"downlode_link":value['attachments'][i]['url']})
              attachments.append(attachment)
            else:
              attachments.append(None)
            num=num+1
            print(num,"-------------------------------------------------------------------------------------------------------------------------------------")


    dic = {"post_id":id,"post":content,"channel_id":channelid,"author":author,"date":date,"is_thread":is_thread,"thread_id":thread_id,"attachments":attachments}
    df = pd.DataFrame(dic)
    print(df)
    # add program to complete your dumping in database

