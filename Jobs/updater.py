from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import ExpireDeals
def start():
	scheduler = BackgroundScheduler()
	
	scheduler.add_job(ExpireDeals, 'interval', seconds=10)
	scheduler.start() 