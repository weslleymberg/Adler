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

sites = sitesDAO.SitesDAO(DATABASE)
bottle.debug(True)
bottle.run(host='localhost', port=8000)
