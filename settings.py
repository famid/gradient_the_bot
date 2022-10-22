import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_SSH_URL = os.getenv("GITHUB_SSH_URL")
ROOT_PATH = os.getenv("ROOT_PATH")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

APP_LIST = ['Laravel', 'React']
