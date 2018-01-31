######IMPORTS######
import csv
import numpy as np
from useful import *
import val
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
                       "\tFrom URL     (1)\n"\
                       "\tIris dataset (2)\n"\
                       ">")

    indicator = 0
    file_name = './data/'
    cate = 0
    delim = ','
    if load_type == 0:
        file_op = input("\nSource:\n"\
                        "\tPima_Indian_Diabetes (0)\n"\
                        "\tUCI:_Car_Evaluation  (1)\n"\
                        "\tMPG_data_set         (2)\n"\
                        ">")
        if file_op == 0:
            file_name += 'pima_indian_data.csv'
            indicator = 0
        elif file_op == 1:
            file_name += 'car_evaluation.csv'
            indicator = '?'
            cate = 1
        else:
            file_name += 'mpg_data.csv'
            indicator = '?'
            cate = 0
            delim = None

    # Choose which classifier to use
    norm = input("\nNormalize:\n"\
                    "\tNo  (0)\n"\
                    "\tYes (1)\n"\
                    ">")

    classifier_type = input("\nClassifier:\n"\
                            "\tGaussianNB          (0)\n"\
                            "\tHardCodedClassifier (1)\n"\
                            "\tKnnClassifier       (2)\n"\
                            "\tOTS_KnnClassifier   (3)\n"\
                            ">")
    return classifier_type,load_type,norm,file_name,indicator, cate, delim

def body(classifier_type, load_type, norm=0,
         source='', indicator=0,cate=0, delim=',',valid=1):
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
    classifier = chooseClassifier(classifier_type)

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
        model = classifier.fit(data_train,targets_train)
        targets_predicted = model.predict(data_test)

        # to calculate accuracy
        correct = 0
        for index in range(len(testset)):
            if targets_predicted[index] == targets_test[index]:
                correct += 1

        # print number correct and calculated accuracy
        print "Correct: [" + str(correct) + "/" + str(len(testset)) + "]"
        print str(round(((correct / float(len(testset))) * 100),4)) + "%"

    if valid == 1:
        pivot_amt = (len(data)/10)
        pivot = pivot_amt
        s = 0
        for i in range(10):
            data_test     =   data[pivot-pivot_amt:pivot]
            targets_test  = target[pivot-pivot_amt:pivot]
            # if pivot != pivot_amt:
            data_train = np.concatenate((data[0:pivot-pivot_amt],
                                             data[pivot:]))
            targets_train = np.concatenate((target[0:pivot-pivot_amt],
                                               target[pivot:]))
            # else:
            #     data_train    =   data[pivot:]
            #     targets_train = target[pivot:]
            model = classifier.fit(data_train,targets_train)
            targets_predicted = model.predict(data_test)

            # to calculate accuracy
            correct = 0
            for index in range(len(data_test)):
                if targets_predicted[index] == targets_test[index]:
                    correct += 1

            s += (correct/float(len(data_test)))*10
            pivot += pivot_amt
        print "Accuracy: "+ str(s) + "%"
    # Shape of the dataset
    shape(data)





if __name__ == "__main__":
    main()
