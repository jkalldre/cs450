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
        self.t = 0
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
        # print self.h
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
    def __init__(self,numLayers,numNodes,dataset,datatargets,bias=-1,n=.25):
        self.dataset = dataset
        self.targets = datatargets
        self.bias    = bias
        self.layers = self.createLayers(numLayers,numNodes)
        self.n = n
        self.error = []
        # print len(self.layers[1].nodes[0].weights)
        # self.currindex = 0
        # self.setTargets(self.currindex)
        # self.feedForward(dataset[self.currindex])
        # self.test()
        # self.output()

    def test(self):
        correct = 0
        total = len(self.dataset)
        for i in range(total):
            self.setTargets(i)
            self.feedForward(self.dataset[i])
            self.error.append(self.predict(i))
            self.backProp()
        return self.error

    def predict(self,index):
        result = []
        targets = Counter(self.targets)

        for each in self.layers[-1].nodes:
            result.append(abs(each.d))

        return result

    def calcAccuracy(self, measured, accepted):
        return (measured - accepted)/float(accepted)

    def createLayers(self, numLayers, numNodes):
        layers = []
        for i in range(numLayers):
            if len(numNodes) == 1:
                layers.append(Layer(self.dataset,numNodes[0],self.bias))
            else:
                layers.append(Layer(self.dataset,numNodes[i],self.bias))
        return layers

    def setTargets(self,index):
        self.layers[-1].nodes[int(self.targets[index])].t = 1

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
        self.calcErr()
        self.AdjWeights()

    def calcErr(self):
        numLay = len(self.layers)
        for i in range(numLay):
            if i == numLay-1:
                for j in range(len(self.layers[i].nodes)):
                    currnode = self.layers[i].nodes[j]
                    a = currnode.a
                    self.layers[i].nodes[j].d = (a*(1-a)*(a-currnode.t))
            else:
                for j in range(len(self.layers[i].nodes)):
                    currnode = self.layers[i].nodes[j]
                    a = currnode.a
                    summ = self.sumAdjWeights(j,i+1)
                    self.layers[i].nodes[j].d = (a*(1-a)*summ)

    def AdjWeights(self):
        for i in range(len(self.layers)):
            for j in range(len(self.layers[i].nodes)):
                for k in range(len(self.layers[i].nodes[j].weights)):
                    node = self.layers[i].nodes[j]
                    self.layers[i].nodes[j].weights[k] = \
                    node.weights[k] - (self.n*node.d*node.inputs[k])

    def sumAdjWeights(self,nodeI,layerI):
        summ = 0
        for i in range(len(self.layers[layerI].nodes)):
            summ += (self.layers[layerI].nodes[i].weights[nodeI]*\
                     self.layers[layerI].nodes[i].d)
        return summ


    def alterWeights(self):
        pass
