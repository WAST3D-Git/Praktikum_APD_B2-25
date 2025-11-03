from tinydb import TinyDB

db = TinyDB('database/database.json')
users_table = db.table('users')
projects_table = db.table('projects')
