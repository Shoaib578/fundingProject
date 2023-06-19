import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.


DATABASE_URL =os.environ.get("DATABASE_URL")
SECRET_KEY = os.environ.get("SECRET_KEY")