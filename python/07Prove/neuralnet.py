from random import randint, uniform
import math
from collections import Counter
from sklearn import datasets

class Node:
    def __init__(self,inputs):
        self.inputs  = inputs
        self.weights = []
        self.a = 0
        self.h = 0
        self.d = 0
        self.predictions = []
        for i in range(len(inputs)):
            self.weights.append(self.initWeight())

    def initWeight(self):
        return uniform(0,1) * ([-1,1][randint(0,1)])

    def output(self):
        summ = 0
        for i in range(len(self.inputs)):
            summ += (self.inputs[i]*self.weights[i])
        return summ

    def update(self,inputs):
        self.inputs = inputs
        # print inputs
        if len(self.inputs) != len(self.weights):
            self.weights = []
            for i in range(len(inputs)):
                self.weights.append(self.initWeight())
    def sigmoid(self):
        return (1.0/(1.0 + math.exp(-self.h)))

class Layer:
    def __init__(self,dataset,numNodes=0,bias=-1):
        self.inputs = dataset[0]
        # print dataset[0]
        self.nodes = []
        self.bias = bias
        for i in range(numNodes):
            self.nodes.append(Node(self.inputs))

    def newInputs(self,inputs):
        # print "NewInputs:",inputs
        for each in self.nodes:
            each.update(inputs)

    def results(self):
        resultarr = []
        for i in range(len(self.nodes)):
            resultarr.append(self.nodes[i].output())
        return resultarr

class NNet:
    ''' The last layer created is the output layer and should
    have the number of classes as the number of nodes '''
    def __init__(self,numLayers,numNodes,dataset,datatargets,bias=-1):
        self.dataset = dataset
        self.targets = datatargets
        self.bias    = bias
        self.layers = self.createLayers(numLayers,numNodes)
        # print len(self.layers[1].nodes[0].weights)
        self.feedForward(dataset[0])
        self.output()

    def createLayers(self, numLayers, numNodes):
        layers = []
        for i in range(numLayers):
            if len(numNodes) == 1:
                layers.append(Layer(self.dataset,numNodes[0],self.bias))
            else:
                layers.append(Layer(self.dataset,numNodes[i],self.bias))
        return layers

    def feedForward(self,dataitem):
        priorOutputs = []
        data = dataitem.tolist()
        data.append(self.bias)
        for i in range(len(self.layers)):
            if i == 0:
                # print "FeedForward:",data
                self.layers[i].newInputs(data)
            else:
                priorOutputs.append(self.bias)
                self.layers[i].newInputs(priorOutputs)
                priorOutputs = []
            for j in range(len(self.layers[i].nodes)):
                self.layers[i].nodes[j].h = self.layers[i].nodes[j].output()
                self.layers[i].nodes[j].a = self.layers[i].nodes[j].sigmoid()
                priorOutputs.append(self.layers[i].nodes[j].a)

    def output(self):
        result = []
        targets = Counter(self.targets)

        for each in self.layers[len(self.layers)-1].nodes:
            result.append(each.a)
        print datasets.load_iris().target_names[result.index(max(result))]


    def backProp(self):
        pass
