######IMPORTS######
import csv
import numpy as np
import urllib
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from random import *
from hardcoded import HardCodedClassifier
###################

def main():
    print ""
    # if given True or left empty, GaussianNB is used
    # anything else invokes HardCodedClassifier
    standardset(0)
    # advancedset()
    print ""

def standardset(classifier_type=1):
    '''Reads from iris dataset'''
    iris = datasets.load_iris()
    # Show the data (the attributes of each instance)
    #print(iris.data)

    # Show the target values (in numeric format) of each instance
    #print(iris.target)

    # Show the actual target names that correspond to each number
    #print(iris.target_names)

    # use my function to randomly divide data 70-30
    trainset, testset = my_train_test_split(len(iris.data))

    # variables to hold the sets
    data_train    = []
    targets_train = []
    data_test     = []
    targets_test  = []

    # fill variables with each type data
    for index in trainset:
        data_train.append(iris.data[index])
        targets_train.append(iris.target[index])
    for index in testset:
        data_test.append(iris.data[index])
        targets_test.append(iris.target[index])

    # decide between naive_bayes Gaussian and my own classifier
    if classifier_type:
        classifier = GaussianNB()
    else:
        classifier = HardCodedClassifier()
    model = classifier.fit(data_train,targets_train)
    targets_predicted = model.predict(data_test)

    # Shape of the dataset
    shape(iris.data)

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
    print "Dataset Shape: [" + str(len(dataset)) + "," + str(len(dataset[0])) + "]"

def print_iris_set(dataset,iris):
    '''Print iris dataset in meaningful way'''
    for index in dataset:
        print iris.data[index], ":"  \
             ,iris.target[index], ":"\
             ,iris.target_names[iris.target[index]]

def my_train_test_split(size):
    '''Split up dataset randomly 70-30'''
    # size     = len(dataset)
    thirty   = int(size*.3)
    trainset = [x for x in range(size)]
    testset  = []
    while thirty != 0:
        steal(trainset,testset)
        thirty -= 1
    return trainset, testset

def steal(setA,setB):
    '''Randomly grab one item from a set and give to other'''
    r = randint(0, len(setA)-1)
    setB.append(setA[r])
    del setA[r]

def advancedset():
    '''Capacity to read from file or url'''
    data = loadCSV('./pima_indian_data.csv')
    # data = loadCSV("https://archive.ics.uci.edu/ml/machine-learning-databases\
                #    /pima-indians-diabetes/pima-indians-diabetes.data",0)
    # showdataset(data)

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
        print "Data Shape:", data.shape
        return data

    except Exception as e:
         print(e)
         print "Invalid data source, Exiting.."

def showdataset(data):
    for item in data:
        print item



if __name__ == "__main__":
    main()
