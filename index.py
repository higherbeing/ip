!pip install Flask-APScheduler

from flask import Flask
from flask_apscheduler import APScheduler

sched = APScheduler()

app = Flask(__name__)

def job1():
  print('hello3')


def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
  sched.add_job(id='job1',func=job1,trigger='interval',seconds=5)
  sched.start()
  app.run(debug=True,use_reloader=False)
  
#from http.server import BaseHTTPRequestHandler
#class handler(BaseHTTPRequestHandler):
#  def do_GET(self):
#    self.send_response(200)
#    self.end_headers()
#    self.wfile.write(self.headers.get('x-forwarded-for').encode())
#    return
