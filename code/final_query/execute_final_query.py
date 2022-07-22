import pymysql
import pandas as pd 

#connect to the database
conn = pymysql.connect( user='user', 
                            passwd='password', 
                            host='0.0.0.0',
                             database='db')

cursor = conn.cursor()
sql_file = "queries/execute_final_query.sql" # define file to read
with open(sql_file,'r') as sql_file:
        cursor.execute(sql_file.read()) # execute the sql file
        tupples = cursor.fetchall() # get the result from the query
        cursor.close()

columns = ["order_id","product_id","unit_price","quantity","discount","customer_id","employee_id","order_date",
            "required_date","shipped_date","ship_via","freight","ship_name","ship_address","ship_city","ship_region",
            "ship_postal_code","ship_country"] # columns of the dataframe
df = pd.DataFrame(tupples,columns = columns) # create the dataframe with the result of the query

df.to_csv("order_with_details.csv",index = False) # save the result on a csv file.

