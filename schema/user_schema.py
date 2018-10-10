from sqlalchemy import Table, Column, BIGINT, VARCHAR, DATETIME, INTEGER, \
    ForeignKey, func
from sqlalchemy.dialects.mssql import TINYINT


def user_schema(metadata):
    print("under user_schema")
    customer = Table('user', metadata,
                     Column('userr_id', BIGINT,
                            primary_key=True, nullable=False),
                     Column('email', VARCHAR(
                         length=255), nullable=False, unique=True),
                     Column('password', VARCHAR(
                            length=255), nullable=False, unique=False),
                     Column('created_at', DATETIME(), nullable=False,
                            default=func.utc_timestamp()),
                     Column('updated_at', DATETIME(), nullable=False,
                            default=func.utc_timestamp())
                     )
    return customer

