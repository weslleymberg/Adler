import sqlite3

class SitesDAO(object):

  def __init__(self, db_name):
    self.db_name = db_name
    self._create_table()

  def save(self, name, url):
    statement = "INSERT INTO Sites VALUES (?, ?, ?);"
    params = (name, url, 0)
    self._execute(statement, params)

  def load(self, limit=-1):
    statement = "SELECT rowid, name, url, last_status FROM Sites LIMIT ?;"
    params = (str(limit), )
    return self._execute(statement, params)

  def delete(self, rowid):
    statement = "DELETE FROM Sites WHERE rowid=?"
    params = (str(rowid), )
    self._execute(statement, params)

  def _create_table(self):
    statement = "CREATE TABLE IF NOT EXISTS Sites (name text, url text, last_status integer);"
    self._execute(statement)

  def _execute(self, statement, params=None): #params is a tuple
    result = None
    conn = sqlite3.connect(self.db_name)
    c = conn.cursor()
    if params:
      c.execute(statement, params)
    else:
      c.execute(statement)
    if statement.startswith('SELECT'):
      result = c.fetchall()
    else:
      conn.commit()
    conn.close()
    return result