######IMPORTS######
import csv
import numpy as np
import urllib
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors   import KNeighborsClassifier
from random import *
from hardcoded import HardCodedClassifier
from knneighbors import KnnClassifier
###################

def main():
    print ""
    # Choose how to load in data
    load_type = input("Read in:\n"\
                       "\tFrom file    (0)\n"\
                       "\tFrom URL     (1)\n"\
                       "\tIris dataset (2)\n"\
                       ">")

    # Choose which classifier to use
    classifier_type = input("Classifier:\n"\
                            "\tGaussianNB          (0)\n"\
                            "\tHardCodedClassifier (1)\n"\
                            "\tKnnClassifier       (2)\n"\
                            "\tOTS_KnnClassifier   (3)\n"\
                            ">")

    standardset(classifier_type,load_type)
    print ""

def standardset(classifier_type=2, load_type=2):
    # Reads from iris dataset
    data   = []
    target = []
    if load_type == 2:
        iris = datasets.load_iris()
        data = iris.data
        target = iris.target
    else:
        if load_type == 0:
            source_data = loadCSV("./pima_indian_data.csv")
        elif load_type == 1:
            source_data = loadCSV("https://archive.ics.uci.edu/ml/machine-learning-databases"\
                           "/pima-indians-diabetes/pima-indians-diabetes.data",0)
        # split up source_data into data and targets
        for item in source_data:
            data.append(item[:-1])
            target.append(int(item[-1]))

    # use my function to randomly divide data 70-30
    trainset, testset = my_train_test_split(len(data))

    # variables to hold the sets
    data_train    = []
    targets_train = []
    data_test     = []
    targets_test  = []

    # fill variables with each type data
    for index in trainset:
        data_train.append(data[index])
        targets_train.append(target[index])
    for index in testset:
        data_test.append(data[index])
        targets_test.append(target[index])

    # decide between naive_bayes Gaussian and my own classifier
    if classifier_type == 0:
        classifier = GaussianNB()
    elif classifier_type == 1:
        classifier = HardCodedClassifier()
    elif classifier_type == 2 or \
         classifier_type == 3:
        k = input("Enter a value for K: ")
        if classifier_type == 2:
            classifier = KnnClassifier(k) #give num of neighbors
        else:
            classifier = KNeighborsClassifier(k)

    model = classifier.fit(data_train,targets_train)
    targets_predicted = model.predict(data_test)

    # Shape of the dataset
    shape(data)

    # to calculate accuracy
    correct = 0
    for index in range(len(testset)):
     # print "Index:", index, "Prediction:", targets_predicted[index], "Actual:", targets_test[index]
        if targets_predicted[index] == targets_test[index]:
            correct += 1

     # print number correct and calculated accuracy
    print "Correct: [" + str(correct) + "/" + str(len(testset)) + "]"
    print str(round(((correct / float(len(testset))) * 100),4)) + "%"

def shape(dataset):
    # Print shape of data
    print "Dataset Shape: [" + str(len(dataset)) + "," + str(len(dataset[0])) + "]"

def print_iris_set(dataset,iris):
    # Print iris dataset in meaningful way
    for index in dataset:
        print iris.data[index], ":"  \
             ,iris.target[index], ":"\
             ,iris.target_names[iris.target[index]]

def my_train_test_split(size):
    # Split up dataset randomly 70-30
    thirty   = int(size*.3)
    trainset = [x for x in range(size)]
    testset  = []
    while thirty != 0:
        steal(trainset,testset)
        thirty -= 1
    return trainset, testset

def steal(setA,setB):
    # Randomly grab one item from a set and give to other
    r = randint(0, len(setA)-1)
    setB.append(setA[r])
    del setA[r]

def loadCSV(source,file_url=1):
    '''True to read from file
       False to read from URL'''
    try:
        if file_url:
            raw_data = open(source, 'rt')
            print "Reading from file..."
        else:
            raw_data = urllib.urlopen(source)
            print "Reading from URL..."
        data = np.loadtxt(raw_data, delimiter=",")
    #prints (numRow,numCol)
        print "SUCCESS"
        # print "Data Shape:", data.shape
        return data

    except Exception as e:
         print(e)
         print "Invalid data source, Exiting.."

def showdataset(data):
    for item in data:
        print item



if __name__ == "__main__":
    main()
