from step_2.helpers.tools import csv_to_mysql,get_all_files
import os

def step_2() :
   try :
         

      path ="tables" #define the folder to get the data to save on MySQL
      pathes = get_all_files(path) # get all files on the path
      for file in pathes   :
         result =csv_to_mysql(file) # for each file, save it on MySQL database
         
         print(f"The file {file} was {result} on the MySQL database")
      
      return "Sucess on the second step."
   except :
      return "Failure on the second step"


