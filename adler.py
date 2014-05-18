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
def add_site():
  site_name = bottle.request.forms.get('name')
  site_url = bottle.request.forms.get('url')

  sites.save(site_name, site_url)
  return bottle.redirect('/')


@bottle.post('/deletesite')
def delete_site():
  site_id = bottle.request.forms.get('site_id')

  sites.delete(site_id)
  return bottle.redirect('/')

sites = sitesDAO.SitesDAO(DATABASE)
bottle.debug(True)
bottle.run(host='localhost', port=8000)
