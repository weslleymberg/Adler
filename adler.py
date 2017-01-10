import urllib2
import bottle

import sitesDAO
from watcher import SiteWatcher

DATABASE = 'adler.db'
DELAY = 10 #seconds
REQUEST_TIMEOUT = 3 #seconds

@bottle.route('/')
def index():
  all_sites = sites.load()
  statuses = []
  for site in all_sites:
    statuses.append(site['status'])
  return bottle.template('index_template', dict(sites=all_sites,
                                                all=all(statuses),
                                                any=any(statuses)))

@bottle.post('/addsite')
def add_site():
  site_name = bottle.request.forms.get('name')
  site_url = bottle.request.forms.get('url')

  sites.save(site_name, site_url)
  return bottle.redirect('/')

@bottle.get('/new')
def new_site():
  return bottle.template('add_site')


@bottle.post('/deletesite')
def delete_site():
  site_id = bottle.request.forms.get('site_id')

  sites.delete(site_id)
  return bottle.redirect('/')


#Startup configuration
sites = sitesDAO.SitesDAO(DATABASE)

def initialize_app():
    watcher = SiteWatcher(sites, DELAY, REQUEST_TIMEOUT)
    watcher.start()
    return bottle.default_app()

if __name__ == '__main__':
    bottle.debug(False)
    bottle.run(host='0.0.0.0', port=8000)

app = initialize_app()
