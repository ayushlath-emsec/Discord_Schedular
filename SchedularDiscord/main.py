from flask import Flask
from Database_Connection import *
from getfunc import *
from datetime import date,datetime,timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from flag import *
import asyncio

# Flask..
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Discord'
def Discord_scrapping():
    print(datetime.now())
    if (isNodeBusy!=True):
        # to check if there is any urgent channel to scrap
        if collection.count_documents({'isUrgent':True})>0:
            print(f"No of urgent Channel :{collection.count_documents({'isUrgent':True})}")
            _urgent = collection.find({"isUrgent":True,"status":{"$ne":"running"}})
            try:
                getfunction(_urgent[0])
            except:
                pass 
        else:  
            d = datetime.today() - timedelta(hours=0, minutes=5)
            if collection.count_documents({"status":{"$ne":"running"},"time":{"$lte":d}})>0:
                _not_urgent = collection.find({"status":{"$ne":"running"},"time":{"$lte":d}})           
                getfunction(_not_urgent[0])    
            else:
                print("Each Discord channel is scrapped.!!") 
    else:
        print("Schedular is Busy!!")


Discord_scrapping()
# Scheduler..
async def main():
    schedular = BackgroundScheduler(daemon = True)
    schedular.add_job(Discord_scrapping,'interval',minutes=2)
    schedular.start()

@app.route('/')
def Discord():
	return 'Discord Scrapper...'
       
# main flask function
if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()     
    app.run(debug=True)