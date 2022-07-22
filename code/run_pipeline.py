from step_1.main import step_1
import argparse
from datetime import datetime,date 
from step_2.main import step_2
#---------------- #create the date flag
parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-d','--date', help='date you want the pipeline to run', required=False)
args = vars(parser.parse_args())

#------------------- 


#checking if the date flag was set 
#-------------------------------
if args["date"] : 
    date = args["date"]
else :
    date= datetime.date(datetime.today()) # getting today date
#------------------------------
print(date)


#Execute step 1 of  pipeline
result = step_1(date)
print(result)  #print the result of the first pipeline
if result == "First step finished with sucess. Execute Second Step" : #if there is no fails on step 1...
    result_2 = step_2() # execute the second step
    print(result_2) #print the result of the second step
else :
    print("Pipeline Ended with error")


