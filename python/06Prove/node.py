from random import randint, uniform

class Node:
    def __init__(self,inputs):
        self.inputs  = inputs
        self.weights = []
        for i in range(len(inputs)):
            self.weights.append(self.initWeight())

    def initWeight(self):
        return uniform(0,1) * ([-1,1][randint(0,1)])

    def output(self):
        summ = 0
        for i in range(len(self.inputs)):
            summ += (self.inputs[i]*self.weights[i])
        if summ > .5:
            return 1
        else:
            return 0

    def update(self,inputs):
        self.inputs = inputs

class Layer:
    def __init__(self,dataset,numNodes=0,bias=None):
        self.inputs = dataset[0]
        print dataset[0]
        self.nodes = []
        self.bias = bias
        for i in range(numNodes):
            self.nodes.append(Node(self.inputs))

    def newInputs(self,inputs):
        for each in self.nodes:
            each.update(inputs)

    def results(self):
        resultarr = []
        for i in range(len(self.nodes)):
            resultarr.append(self.nodes[i].output())
        return resultarr
