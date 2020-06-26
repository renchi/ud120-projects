#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn import svm
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
#plt.xlim(0.0, 1.0)
#plt.ylim(0.0, 1.0)
#plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
#plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
#plt.legend()
#plt.xlabel("bumpiness")
#plt.ylabel("grade")
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


for this_n_estimators in [10,50,100]:
    clf = RandomForestClassifier(n_estimators=this_n_estimators)
    clf = clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)
    scoretest = accuracy_score(pred, labels_test)
    print("Accuracy of Random forest estimator = {}, Test Score: {:2f} ".format(this_n_estimators,scoretest))

    adaclf = AdaBoostClassifier(n_estimators=this_n_estimators, random_state=0)
    adaclf = adaclf.fit(features_train, labels_train)
    pred2 = adaclf.predict(features_test)
    adascoretest = accuracy_score(pred2, labels_test)
    print("Accuracy of Adaboost= {}, Test Score: {:2f}".format(this_n_estimators,adascoretest))

    clfsvm = svm.SVC(C=1000)
    clfsvm = clfsvm.fit(features_train, labels_train)
    pred3 = clfsvm.predict(features_test)
    svmScoretest = accuracy_score(pred3, labels_test)
    print("Accuracy of SVM= {}, Test Score: {:2f} \n".format(this_n_estimators,svmScoretest))


    '''
    try:
        prettyPicture(adaclf, features_test, labels_test)
    except NameError:
        pass    
    '''

