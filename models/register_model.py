from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from schema.all_schemas import all_schemas
from sqlalchemy import MetaData, Table
from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy.sql.expression import Insert, select
from sqlalchemy.dialects.postgresql import insert
import json
import datetime

Base = declarative_base()

class register_model():
    def register_undermodel(self, email, password, confirmPassword):
        metadata = MetaData()
        schemas = all_schemas(metadata)
        eng = schemas['db'].getConnection()
        Base.metadata.bind = eng
        Session = sessionmaker(bind=eng)
        ses = Session()
      
        print("ttt")
        db_query = ses.query(schemas['db_details'])
        print(db_query)
    
        flag = 0

        if password == confirmPassword:
            sql = schemas['db_details'].insert().values(email=email, password=password, verified = '0' )      
            ses.execute(sql)
            flag = 1

        
        ses.commit()
        ses.close()
        schemas['db'].connectionClose()
        del metadata
        del schemas
        del ses
        if flag == 1:
            return 1

        else:
            return 0
      