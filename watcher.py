import threading
from urllib2 import urlopen, Request, URLError
import time

#Very general error handling...
#This will be changed later

class HeadRequest(Request):
    def get_method(self):
        return 'HEAD'

class SiteWatcher(threading.Thread):

  def __init__(self, db, delay, request_timeout):
    threading.Thread.__init__(self)
    self.db = db
    self.delay = delay
    self.request_timeout = request_timeout
    self.daemon = True

  def run(self):
    while True:
      sites = self.db.load()
      if sites:
        for site in sites:
          try:
            urlopen(HeadRequest(site['url']), timeout=self.request_timeout)
          except URLError as e:
            site['status'] = 0
          else:
            site['status'] = 1
        self.db.update(sites)
      time.sleep(self.delay)
