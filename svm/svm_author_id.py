#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

### Use a smaller training sets
#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]


#########################################################
### your code goes here ###

#clf = svm.SVC(kernel="linear")
clf = svm.SVC(C=10000.0)

### fit the classifier on the training features and labels
#print("training started")
#t0 = time()
clf.fit(features_train, labels_train)
#print("training time:", round(time()-t0, 3), "s")

### use the trained classifier to predict labels for the test features
#print("test started")
#t1 = time()
pred = clf.predict(features_test)
#print("testing time:", round(time()-t1, 3), "s")

acc = accuracy_score(pred, labels_test)
print("SVM Accuracy is {} ".format(acc))
#print("Predictions are {}, {}, {}".format(c[10], pred[26], pred[50]))

### Number of predicted as "Chris" (1) class
num_ones = (pred == 1).sum()
print("Chris prediction count = {}".format(np.sum(pred == 1)));
print("Sara prediction count = {}".format(np.sum(pred == 0)));
#########################################################


