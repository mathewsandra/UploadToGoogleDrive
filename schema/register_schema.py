from sqlalchemy import Table, Column, BIGINT, VARCHAR, DATETIME, INTEGER, \
    ForeignKey, func
from sqlalchemy.dialects.mssql import TINYINT

def db_schema(metadata):
    print("under db_schema")
    db_details = Table('db_details', metadata, 
                       Column('email', VARCHAR(length=100), primary_key = True),
                       Column('password', VARCHAR(length=100)),
                       Column('verified', VARCHAR(length=100))
                       )

    return db_details    