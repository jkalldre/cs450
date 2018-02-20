from model import KnnModel

class KnnClassifier:
    def __init__(self, k=1):
        self.k = k

    def fit(self, data_train, target_train):
        return KnnModel(self.k,data_train,target_train)
