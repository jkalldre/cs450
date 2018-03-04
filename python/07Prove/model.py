from collections import Counter

class HCModel:
    # Used to predict targets
    def __init__(self):
        self.targets = []

    def predict(self,dataset):
        for item in dataset:
            self.targets.append(0)
        return self.targets

class KnnModel:
    # Used to predict targets
    def __init__(self, k, data_train, targets_train):
        self.k       = k
        self.data    = data_train
        self.targets = targets_train
        self.predicts = []

    def predict(self, data_test):
        # for item in data_test:
        dist_Matrix = self.createMatrix(data_test)
        for row in dist_Matrix:
            self.predicts.append(self.makePrediction_class(row))
        return self.predicts

    def findDist(self, item_1, item_2):
        # calculate Euclidean distance between two items
        sum = 0
        for i in range(len(item_1)):
            sum += (item_1[i] - item_2[i])**2
        return sum

    def createMatrix(self,data_test):
        # creates a distance matrix to avoid duplicate calculations
        mat = []
        for te_item in data_test:
            tmp = []
            for i in range(len(self.data)):
                tmp.append([round(self.findDist(self.data[i],te_item),4),self.targets[i]])
            mat.append(tmp)
        return mat

    def makePrediction_class(self,row):
        # Returns most common class, if tie occurs first class is returned
        sorted_row = sorted(row,key = lambda x: x[0]) # sort the list
        knn = sorted_row[0:self.k]                    # grab k neighbors
        classes = [item[1] for item in knn]      # grab the class value
        count = Counter(classes)                 # count how often each class occurs
        return max(count.iteritems(), key=lambda x: x[1])[0] # return the prediction

    def makePrediction_regress(self,row):
        sorted_row = sorted(row,key = lambda x: x[0]) # sort the list
        knn = sorted_row[0:self.k]
        vals = [x[1] for x in knn]
        av = round(sum(vals)/len(vals),1)
        print av
        return av
