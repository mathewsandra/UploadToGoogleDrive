from dotenv import load_dotenv
import os
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# print("vellom nadakuo")
SECRET_KEY = os.getenv("SECRET_KEY")
dialect = os.getenv("dialect")
username = os.getenv("username")
password = os.getenv("password")
host = os.getenv("host")
database = os.getenv("database")