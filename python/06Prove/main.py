######IMPORTS######
import csv
import numpy as np
from useful import *
import val
from node import Node, Layer
###################

def main():
    print ""
    classifier_type, load_type, norm, file_name, indicator\
    , cate, delim = menu()
    body(classifier_type,load_type,norm,file_name,indicator\
         , cate, delim)
    print ""

def menu():
    # Choose how to load in data
    load_type = input("Run:\n"\
                       "\tFrom file    (0)\n"\
                       "\tIris dataset (1)\n"\
                       ">")

    indicator = 0
    file_name = './data/'
    cate = 0
    delim = ','
    if load_type == 0:
        file_op = 0
        if file_op == 0:
            file_name += 'pima_indian_data.csv'
            indicator = 0

    # Choose which classifier to use
    norm = input("\nNormalize:\n"\
                    "\tNo  (0)\n"\
                    "\tYes (1)\n"\
                    ">")

    # classifier_type = input("\nClassifier:\n"\
    #                         "\tGaussianNB          (0)\n"\
    #                         ">")
    return 0,load_type,norm,file_name,indicator, cate, delim

def body(classifier_type, load_type, norm=0,
         source='', indicator=0,cate=0, delim=',',valid=0):
    np.set_printoptions(suppress=True, threshold=np.inf) #np

    # Load the data
    data,target = load_dataset(load_type, source,delim)

    # data munging
    data = missing_to_nan(data, indicator)
    data = cate_to_index(data, cate)

    for row in range(len(data)):
        for col in range(len(data[row])):
            data[row][col] = float(data[row][col])

    if source == './data/mpg_data.csv':
        for i in range(len(target)):
            target[i] = float(target[i])

    # replace missing values with column average
    avArr = getAv(data)
    data = nan_to_av(data, avArr)

    # normalize
    if norm:
        data = av_to_z(data,avArr)

    # for item in target:
    #     print item
    # return

    # variables to hold the sets
    data_train    = []
    targets_train = []
    data_test     = []
    targets_test  = []

    # decide between naive_bayes Gaussian and my own classifier
    # classifier = chooseClassifier(classifier_type)
    if valid == 0:
        # use my function to randomly divide data 70-30
        trainset, testset = my_train_test_split(len(data))

        # fill variables with each type data
        for index in trainset:
            data_train.append(data[index])
            targets_train.append(target[index])
        for index in testset:
            data_test.append(data[index])
            targets_test.append(target[index])
        
        layer = Layer(data_train,3,-1)
        print layer.results()

    shape(data)





if __name__ == "__main__":
    main()
