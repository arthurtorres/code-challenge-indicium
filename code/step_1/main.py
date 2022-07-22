from step_1.helpers.tools import get_tables_from_post,get_columns_names_from_post,postgresql_to_dataframe,create_conn_post,save_csv_locally,save_postgree_locally
import os 

def step_1(dates) :
   try :
      #This code represents the step 1 of the pipeline.
      #It will conect with the postgree database and save the tables on a tables folder locally.(1)
      #It will get the csv file and save on the tables folders.(2)
      
      #1
      #------------------------------

      conn = create_conn_post() # creating the conenction with the database
      tables = get_tables_from_post(conn) # using the connection to get the tables of the dataset
      

      for table in tables : #iterate for each table on the database
         result =save_postgree_locally(conn,table,dates)  #load the data locally
         if result == "Failure" : # if that some error, return the table with the error and a message
            return f"Error to load {table}  locally"

         print(f"The Table  {table} was loaded locally") #if is sucessuful, print a message of sucess
            

      conn.close() # finish the conneciton with the postgree databased

      #------------------------------



      #2
      #------------------------------
      file_csv_location = "data/order_details.csv"
      result = save_csv_locally(file_csv_location,dates) 
   #-------------------------------
      return  "First step finished with sucess. Execute Second Step"
   except :
      return "Unkown error on step 1. Probably the error is linked to the connection with the postgree database. DONT execute second step"


