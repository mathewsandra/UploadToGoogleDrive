from schema.service_model import SqlConnection
from schema.user_schema import user_schema
from schema.sp_schema import sp_schema

def all_schemas(metadata):
    print("under all schemas")
    user = user_schema(metadata)
    sp_devices = sp_schema(metadata)
    allModels = {
        'user': user,
        'sp_devices': sp_devices,
        'db': SqlConnection()
    }

    return allModels
