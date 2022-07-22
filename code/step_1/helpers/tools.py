import pandas as pd 
import psycopg2
import  os 
def create_conn_post() :
    """
    Create the connection with the postgree database.
    """

    conn = psycopg2.connect( #create the connection
        database="northwind",
        user="northwind_user",
        password="thewindisblowing",
        host="0.0.0.0"
        )
    return conn

def get_tables_from_post(conn) :
        """

        Given the connection, return all tables on the postgree database where the schema is public
        
        """

        cursor = conn.cursor()
        query = "SELECT * FROM information_schema.tables WHERE table_schema = 'public'"   
        cursor.execute(query) # execute thq query for the specific  schema
        tupples = cursor.fetchall() # get the data in tupples
        cursor.close() # end connection
        df = pd.DataFrame(tupples) # transform the data in a dataframe
  
        tables = df[2].values # get the tables, which are the third column on the result dataset

        return tables 


def get_columns_names_from_post(conn,table) :
    """
    Given the connection and the specific table of the database, return the columns of that table.
    
    """
   
   
    cursor = conn.cursor()
    query = f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table}'"
    cursor.execute(query) # query the table
    tupples = cursor.fetchall() # get the data
    cursor.close()
    df = pd.DataFrame(tupples) # transform the tupples in a dataframe
    columns = df[0].tolist() # get the first column, where we have the name of the columns
    return columns


def postgresql_to_dataframe(conn, select_query,columns_name):

    """
    Given a Query, a connection and the name of the columns, execute the query in the database and return the result as a  pandas dataframe
    
    """
    
    cursor = conn.cursor()
    try:
        cursor.execute(select_query) #execute the query, if failed print the error and finished the execution

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        cursor.close()
        return 1
    
    tupples = cursor.fetchall() # if sucessuful get the tupples
    cursor.close() # end conneciton
    
    df = pd.DataFrame(tupples,columns =columns_name) #transform the data in a pandas dataframe
    return df


def save_csv_locally(file_csv_location,date) :
    """
    Given the location of a csv file and a date, save it locally on an specific format

    """


    try :
     file_csv_destination = f"tables/csv/order_details/{date}/" # create the directory where to save the table
     if not os.path.isdir(file_csv_destination): #create the directory if not exist
            os.makedirs(file_csv_destination)
     df = pd.read_csv(file_csv_location) # read the csv file

     df.to_csv(f'{file_csv_destination}/order_details.csv',index = False) #save the file
     return "Sucess"
    except :
     return "Failure"

def save_postgree_locally(conn,table,date) :

    """
    Given a Connection, a table, and a date save the table locally in a specific format
    """
    try :
        columns= get_columns_names_from_post(conn,table) # get the columns of the table
        query = f"SELECT * FROM {table}" # mount the SQL query needed to query all the data
        df = postgresql_to_dataframe(conn,query,columns) # transform the table on a dataframe
        directory = f"tables/postgres/{table}/{date}/" # create the directory where to save the table
        file =  f"{table}.csv"  # define the name of the file (that is, the name of the table )
        if not os.path.isdir(directory): #create the directory if not exist
                os.makedirs(directory)
        df.to_csv(f'{directory}{file}',index = False) #save the data locally in csv
        return "Sucess"
    except :
        return "Failure"
