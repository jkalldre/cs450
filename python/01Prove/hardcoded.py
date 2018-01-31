class HardCodedClassifier:
    # Used to train data
    def __init__(self):
        pass

    def fit(self, data_train, targets_train):
        return Model()

class Model:
    # Used to predict targets
    def __init__(self):
        self.targets = []

    def predict(self,dataset):
        for item in dataset:
            self.targets.append(0)
        return self.targets
