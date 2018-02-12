#from model import DTModel
from math import log

class DTClassifier:
    def __init__(self):
        pass

    def fit(self):
        pass

class Node:
    def __init__(self,name,branches=None):
        self.name = name
        self.parent = None
        self.children = []
        self.branches = branches

    def give_parent(self,node):
        self.parent = node

    def give_child(self,node):
        self.children.append(node)

    def become_leaf(self):
        self.children = None

    def display_children(self, number=0):
        if number == 0:
            print "Root-0: " + str(self.name)
        else:
            print str(number) + " - Child of " + str(number-1) + ": " + str(self.name)
        if len(self.children) != 0:
            for i in range(len(self.children)):
                if number == 0:
                    print "Branch:"
                self.children[i].display_children(number+1)


class Tree:
    def __init__(self,root):
        self.root = root

    def display_tree(self):
        pass

    def predict(self,data_point):
        pass

    def self_build(self,data_train,targets_train):
        return {}

class DTModel:
    def __init__(self):
        self.predictions = []

    def predict(self):
        pass
