#######IMPORTS#########
import numpy  as np
import pandas as pd
from random import *
import urllib
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors   import KNeighborsClassifier
from hardcoded import HardCodedClassifier
from knneighbors import KnnClassifier
from sklearn import datasets
import val
import csv
#######################


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

def loadCSV(source,file_url=1,delim=','):
    try:
        if file_url:
            print source
            dw = 0
            if delim == None:
                dw = 1
            raw_data = pd.read_csv(source,header=0,delimiter=delim
                                   ,delim_whitespace=dw,dtype=object)#open(source, 'rt')
            print "Reading from file..."
        else:
            raw_data = urllib.urlopen(source)
            print "Reading from URL..."
        data = raw_data.as_matrix(columns=None)#np.loadtxt(raw_data, delimiter=delim)
        if source == './data/mpg_data.csv':
            data = reverse(data)
            data = np.delete(data,0,1)
        print "SUCCESS"
        return data

    except Exception as e:
         print(e)
         print "Invalid data source, Exiting.."

def showdataset(data):
    for item in data:
        print item

def chooseClassifier(val):
    if val == 0:
        return GaussianNB()
    elif val == 1:
        return 

def missing_to_nan(data,indicator='?'):
    for row in data:
        for col_i in range(len(row)):
            if row[col_i] == indicator:
                row[col_i] = np.NaN
    return data

def nan_to_av(npdata,avArr):
# Replace NaN with average of col
    for row in npdata:
        for col_i in range(len(row)):
            if np.isnan(row[col_i]):
                row[col_i] = avArr[col_i]
    return npdata

def av_to_z(values, av):
    # (x-mean)/std
    std = np.std(values,axis=0,dtype=float)
    for row in values:
        for i in range(len(row)):
            row[i] = ((row[i] - av[i])/std[i])
    return values

def getAv(values):
    s = [np.nansum(x) for x in zip(*values)]
    av = [x/(len(values)) for x in s]
    # print av
    return av

def load_dataset(load_type, source,delim=','):
    data   = []
    target = []
    if load_type == 1:
        iris = datasets.load_iris()
        data = iris.data
        target = iris.target
    else:
        if load_type == 0:
            print source
            source_data = loadCSV(source,1,delim)
        # split up source_data into data and targets
        for item in source_data:
            data.append(item[:-1])
            target.append(item[-1])
    return data, target

def cate_to_index(data, cate):
    # Replace all categories
    if not cate:
        return data
    if cate == 1:
        cols = val.car_cols
    for row in range(len(data)):
        for col in range(len(data[row])):
            for cat in range(len(cols[col])):
                if data[row][col] == cols[col][cat]:
                    data[row][col] = cat
    return data

def reverse(data):
    for i in range(len(data)):
        data[i] = data[i][::-1]
    return data
