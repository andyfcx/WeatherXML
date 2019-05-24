import configparser
from sqlalchemy import create_engine, MetaData, Table

class SettingDB():
    def __init__(self):
        self._DB_IP = "127.0.0.1"
        self._DB_ACCOUNT = "root"
        self._DB_PASSWORD = "andypersonal"

create_engine("mysql://root:andypersonal@127.0.0.1/")

