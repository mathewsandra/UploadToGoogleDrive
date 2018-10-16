from schema.service_model import SqlConnection
from schema.user_schema import user_schema
from schema.sp_schema import sp_schema
from schema.register_schema import db_schema

def all_schemas(metadata):
    print("under all schemas")
    user = user_schema(metadata)
    sp_devices = sp_schema(metadata)
    db_details = db_schema(metadata) 
    allModels = {
        'user': user,
        'sp_devices': sp_devices,
        'db_details': db_details,
        'db': SqlConnection()
    }

    return allModels
