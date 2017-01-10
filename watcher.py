import threading
import urllib2
import time

#Very general error handling...
#This will be changed later

class HeadRequest(urllib2.Request):
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
            urllib2.urlopen(HeadRequest(site['url']), timeout=self.request_timeout)
          except Exception:
            site['status'] = 0
          else:
            site['status'] = 1
        self.db.update(sites)
      time.sleep(self.delay)
