from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
import config.config as config

dialect = config.dialect
# username = config.username
username = 'postgres'
password = ''
if config.password is not None:
    password = config.password
host = config.host
database = config.database

class SqlConnection:
    connection = 0
    engine = 0
    def __init__(self):
        get_address = dialect+username+':'+password+host+database
        print(get_address)
        self.engine = create_engine(get_address, encoding="utf-8")
        self.connection = self.engine.connect()

    def getConnection(self):
        return self.connection

    def connectionClose(self):
        self.engine.dispose()
        self.connection.close()
        return