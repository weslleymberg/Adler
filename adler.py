import urllib2
import bottle

import sitesDAO

DATABASE = 'adler.db'

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
def addsite():
  site_name = bottle.request.forms.get('name')
  site_url = bottle.request.forms.get('url')

  sites.save(site_name, site_url)
  return bottle.redirect('/')

sites = sitesDAO.SitesDAO(DATABASE)
bottle.debug(True)
bottle.run(host='localhost', port=8000)
