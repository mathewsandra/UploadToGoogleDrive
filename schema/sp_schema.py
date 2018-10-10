from sqlalchemy import Table, Column, BIGINT, VARCHAR, DATETIME, INTEGER, \
    ForeignKey, func
from sqlalchemy.dialects.mssql import TINYINT


def sp_schema(metadata):
    print("under user_schema")
    sp = Table('sp_devices', metadata,
                     Column('id', VARCHAR(length=11), primary_key = True),
                     Column('deviceid', VARCHAR(length=100)),
                       Column('publickey', VARCHAR(length=500)),
                       Column('created_at', DATETIME(), nullable=False,
                            default=func.utc_timestamp()),
                       Column('updated_at', DATETIME(), nullable=False,
                            default=func.utc_timestamp()),
                       Column('userid',VARCHAR(length=100)),
                       Column('devicetype',VARCHAR(length=100)),
                       
                       )
    return sp

