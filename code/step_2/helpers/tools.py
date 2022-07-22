import pymysql
from sqlalchemy import create_engine
import os 
from pymysql.constants import CLIENT
import pandas as pd


def get_all_files(folder) : 
    """
    Given a folder, return the full path of all the files inside
    """
    pathes = []
    for path, subdirs, files in os.walk(folder): 
        for name in files:
            pathes.append(os.path.join(path, name))
    return pathes

def csv_to_mysql(table) :
    "Given the path to a table, uplaod it csv to MySQL database"

    try :
        engine = create_engine('mysql+pymysql://root:password@localhost/db') #create connection as root
        table_output = table.split("/")[-1].split(".")[0]  # get the name of the table from the path
        df = pd.read_csv(table,sep=',',encoding='utf8')   # read the data as a pandas dataframe
        df.to_sql(table_output,con=engine,index=False,if_exists='append')  # create the table or append it to a existing table on MySQL database.
        return "loaded"
    except :
        return "not loaded"