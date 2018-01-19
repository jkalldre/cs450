class HCModel:
    # Used to predict targets
    def __init__(self):
        self.targets = []

    def predict(self,dataset):
        for item in dataset:
            self.targets.append(0)
        return self.targets

class KNModel:
    # Used to predict targets
    def __init__(self):
        self.targets = []

    def predict(self,dataset):
        for item in dataset:
            self.targets.append(0)
        return self.targets
