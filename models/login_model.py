from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from schema.all_schemas import all_schemas
from schema.user_schema import user_schema
from sqlalchemy import MetaData, Table
from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy.sql.expression import Insert, select
from flask import jsonify
import config.config as config
import json
import datetime
import jwt
import time

Base = declarative_base()

class Login_model():
    def logintest(self, email, password):
        return 0

    def login(self, email, password):
        metadata = MetaData()
        schemas = all_schemas(metadata)
        eng = schemas['db'].getEngine()
        schemas['db'].connectionClose()
        Base.metadata.bind = eng      
        print(eng)
        Session = sessionmaker(bind=eng)
        ses = Session()
        user1 = ses.query(schemas['user'])
        user1 = user1.filter_by(email=email).first()
        if user1:
            if user1.password:
                if user1.password == password:
                    flag = 1
                    auth_token = jwt.encode({email : email, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, config.SECRET_KEY)
                    # auth_tokenstring = jsonify({'auth_token' : auth_token.decode('UTF-8')})
                    # auth_tokenstring = jsonify({'auth_token' : auth_token})
                    # print(auth_tokenstring)
                    # sql = schemas['sp_devices'].update().values(publickey = auth_token).where(schemas['sp_devices'].c.userid == user1.email)
                    # ses.execute(sql)
                    # user2 = ses.query(schemas['sp_devices'])
                    # user2 = user2.filter_by(userid=user1.email).first()
                    
                else:
                    flag = 0    
            else:
                flag = 0     
        else:
            flag = 0
        ses.commit()
        ses.close()
        schemas['db'].connectionClose()
        del metadata
        del schemas
        del ses 
        if flag == 1:
            print("under flag")
            print(auth_token)
            return 1
        else:
            print("flag is 0")
            return 0
