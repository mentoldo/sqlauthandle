from sqlauthandle.sqlauthandle import Sqlauth
import getpass

auth = Sqlauth(alias='test', reset_file=True)

auth.set_credentials(dialect='postgresql',
                     host='localhost',
                     port='5432',
                     user='mariano',
                     db_name='tablero_acciones',
                     passwd=getpass.getpass('Password: '))


conn = auth.conect_db()


import pandas.io.sql as sqlio



db = sqlio.read_sql_query("select * from historial", con= conn)

print(db.head())