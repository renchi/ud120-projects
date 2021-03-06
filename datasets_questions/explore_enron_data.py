#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

enron_data_count = len(enron_data)
print("Total data points = {}".format(enron_data_count))

# Count of features available for each person. Answer is 21.
for data in enron_data.values():
    print("Features available for each person = {}".format(len(data)))
    break

# Numbers of POI in the data set. Answer is 18
poi_count = 0
for data in enron_data.values():
    for key, value in data.items():
        if (key == 'poi' and value == 1):
            poi_count += 1
print("POIs in final_project_dataset.pkl = {}".format(poi_count))

# Count of POIs in poi_names.txt
poi_count = 0
poi_names_file = open("../final_project/poi_names.txt", "r") # Open as text file, so use "r" not "rb"
list_of_names = poi_names_file.readlines()
poi_names_file.close();
for name in list_of_names:
    if name.find('(y)') == 0 or name.find('(n)') == 0:
        poi_count += 1
print("POIs in poi_names.txt = {}".format(poi_count))

# total value of the stock belonging to James Prentice:
lookupName = "Prentice James"
for key in enron_data.keys():
    if re.search(lookupName, key, re.IGNORECASE):
        total_stock_value = enron_data[key]['total_stock_value']
        print("Total stock value of {} = {}".format(key,total_stock_value ))

# How many email messages do we have from Wesley Colwell to persons of interest?
lookupName = "Colwell Wesley"
for key in enron_data.keys():
    if re.search(lookupName, key, re.IGNORECASE):
        count_of_email_to_poi = enron_data[key]['from_this_person_to_poi']
        print("Email count from {} to POI = {}".format(key,count_of_email_to_poi ))

# What’s the value of stock options exercised by Jeffrey K Skilling?
lookupName = "Skilling Jeffrey"
for key in enron_data.keys():
    if re.search(lookupName, key, re.IGNORECASE):
        stock_options_exercised = enron_data[key]['exercised_stock_options']
        print("Value of stock options exercised by {}= {}".format(key,stock_options_exercised ))

# who took home the most money
lookupNameArray = ["Skilling", "Fastow", "Lay"]
for key in enron_data.keys():
    total_payments = 0
    if re.search(lookupNameArray[0], key, re.IGNORECASE):
        total_payments = enron_data[key]['total_payments']
    elif re.search(lookupNameArray[1], key, re.IGNORECASE):
        total_payments = enron_data[key]['total_payments']
    elif re.search(lookupNameArray[2], key, re.IGNORECASE):
        total_payments = enron_data[key]['total_payments']

    if total_payments > 0:
        print("{} took {} million".format(key,float(total_payments)/1000000))

# How many folks in this dataset have a quantified salary? What about a known email address?
have_salary = 0
have_email_address = 0
for data in enron_data.values():
    for key, value in data.items():
        if key == 'salary' and value != 'NaN' and int(value) > 0:
           have_salary += 1
        elif key == 'email_address' and value != 'NaN':
            have_email_address += 1
print("Folks that have a quantified salary= {}; email_address = {}".format(have_salary, have_email_address))

# Percentage of people that have NaN in total payments
count_of_nan_payment = 0
for data in enron_data.values():
    for key, value in data.items():
        if key == 'total_payments' and value == 'NaN':
           count_of_nan_payment += 1

percent_of_nan_payment = (count_of_nan_payment/enron_data_count) * 100
print ("People that have NaN in total payments is {} %".format(percent_of_nan_payment))

# Percentage of POI that have NaN in total payments
count_of_poi_nan_payment = 0
for data in enron_data.values():
    for key, value in data.items():
        if key == 'poi' and value == 1:
            if data['total_payments'] == 'NaN':
                count_of_poi_nan_payment += 1

percent_of_poi_nan_payment = (count_of_poi_nan_payment/poi_count) * 100
print ("POI that have NaN in total payments is {} %".format(percent_of_poi_nan_payment))

'''
count_of_nan_payment += 10
enron_data_count += 10
percent_of_nan_payment = (count_of_nan_payment/enron_data_count) * 100
print ("enron_data_count {} count_of_nan_payment {} percent_of_nan_payment {}"
       .format(enron_data_count, count_of_nan_payment, percent_of_nan_payment))
'''
