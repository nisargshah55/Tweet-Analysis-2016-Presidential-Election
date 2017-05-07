"""
Neel and Julia worked on this.
"""


from sklearn import tree
from sklearn.externals.six import StringIO
import pydot 
from sklearn.feature_extraction.text import TfidfTransformer
import IPython
import sklearn as sk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import re
import csv
import os
from sklearn.cross_validation import cross_val_score, KFold
from sklearn import cross_validation
from scipy.stats import sem
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer
from sklearn import metrics


def read_data(data):
    #data_file_name = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    count = 0
    f1=open('bernie_training.txt',"r")
    for item in f1:

        data.append(item)
    f1.close()



def train_and_evaluate(clf, X_train, X_test, y_train, y_test, i_fold):
    
    clf.fit(X_train, i_fold, y_train) #i_fold is to record information for every fold, it is useful when output visualized decision tree and map from vocabulary index to vocabulary of each fold.
    
    print "Accuracy on training set:"
    print clf.score(X_train, y_train)
    print "Accuracy on testing set:"
    print clf.score(X_test, y_test)
    
    y_pred = clf.predict(X_test)
    
    print "Classification Report:"
    print metrics.classification_report(y_test, y_pred)
    print "Confusion Matrix:"
    print metrics.confusion_matrix(y_test, y_pred)


def evaluate_cross_validation(clf, X, y):
    
    scores = cross_validation.StratifiedKFold(y, n_folds = 2)
    i_fold = 1;
    for tr, te in scores:
        xtr = [X[i] for i in tr] #training set
        ytr = [y[i] for i in tr] #training label
        xte = [X[i] for i in te] #test set
        yte = [y[i] for i in te] #test label
        train_and_evaluate(clf, xtr, xte, ytr, yte, i_fold)
        i_fold += 1
        

data = []
label_number = []
file_name = []

f2=open('bernie_nyc_training.txt',"r")
for i,j,k in f2:
    label_number.append(k)
f2.close()


read_data(data)


clf_3 = Pipeline([
    ('vect', TfidfVectorizer()),
    ('clf', tree.DecisionTreeClassifier()),
])

evaluate_cross_validation(clf_3, data, label_number)

