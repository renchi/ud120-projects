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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# Total data points. Answer is 146
print(len(enron_data))

# Count of features available for each person. Answer is 21.
for data in enron_data.values():
    print(len(data))

# Numbers of POI in the data set. Answer is 18
poi_count = 0
for data in enron_data.values():
    for key, value in data.items():
        if (key == 'poi' and value == 1):
            poi_count += 1
print (poi_count)





