from flask import Flask
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import todo_listo as todo_listo 
import os, time
os.environ['TZ'] = 'America/Chicago'

application = Flask(__name__)

@application.route("/")
def index():
    return "Follow @dionicio_98"

def job():
    todo_listo.twitter()
    

    
scheduler = BackgroundScheduler()
scheduler.add_job(func=job, trigger = 'cron', day_of_week='mon-fri',hour='21', minute='1', timezone = 'UTC')
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    application.run(port=5000, debug=True,use_reloader=False)