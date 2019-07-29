'''
*****************THE PROGRAM IS ABOUT CREATING CSV FILE AND ADDING VALUES*********

'''
import pandas as pd
import datetime
import csv

#create a csv file handle
#data = pd.read_csv(r"TEMP.csv")
#print("done reading")
#print(data.head()) to read first 5 values of csv
with open(r"TEMP.csv", 'w') as csvfile:
    names = ['Time', 'Light' , 'Fan']
        
    put = csv.DictWriter(csvfile, fieldnames = names)
    put.writeheader()
    count = 0
    while count < 10:
        light, fan = input(" mark 1 for high and 0 for low ").split() 
        print("state of light is {0} and fan is {1}".format(light,fan))
        time_hr = datetime.datetime.now().strftime("%H")
        #print(time_hr)
        time_min = datetime.datetime.now().strftime("%M")
        #print(time_min)
        values = str(time_hr) + "." + str(time_min) + "," + light + "," + fan
        
        put.writerow({'Time':  str(time_hr) + "." + str(time_min), 'Light': light, 'Fan': fan})
        
        #print(values)
        count += 1


