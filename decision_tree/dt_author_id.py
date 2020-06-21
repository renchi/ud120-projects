#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree
from sklearn.metrics import accuracy_score

features_train, features_test, labels_train, labels_test = preprocess()


# number of rows is the number of data points and the number of columns is the number of features;
# so to extract this number, use a line of code like len(features_train[0]).)
# This depends on SelectPercentile() in email_preprocess.py
features_count = len(features_train[0])
print("Number of features:{}".format(features_count))

this_min_sample_split = 40
clf = tree.DecisionTreeClassifier(min_samples_split=this_min_sample_split)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
scoretest = accuracy_score(pred, labels_test)
print("Accuracy of min_sample_split:{}, Test Score: {:2f} \n".format(this_min_sample_split,scoretest))




