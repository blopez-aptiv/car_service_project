# Connection to a database
import pymysql
import os

class MySQL:
    def __init__(self) -> None:
        username = os.environ['MYSQL_USERNAME'] 
        password = os.environ['MYSQL_PASSWORD']
        mysql_db = os.environ['MYSQL_DB']
        mysql_host = os.environ['MYSQL_HOST']
        
        self.mysql_connection = pymysql.connect(host= mysql_host , user=username, password=password, database=mysql_db, cursorclass=pymysql.cursors.DictCursor, autocommit=True)