import pyodbc
import pandas as pd
import urllib
import sqlalchemy as sa
import dotenv
from os import environ as env



def sql_connection(driver, server, db):
    pass

class SqlHelper():
    """
    stores various parameters for the project

    default server
    default db

    maintain open connection?


"""
    server=""
    db =""
    cnx = None
    drivers = pyodbc.drivers()
    driver = drivers[-1]
    
    def __init__(self, server="", db="", maintain_cnx = False) -> None:
        """
        take provided args, or read from config file
        """
        pass





    def connection():
        pass

    def read_sql():
        pass

    def exec_sql():
        pass
