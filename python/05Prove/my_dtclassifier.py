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

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

    def give_parent(self,node):
        self.parent = node

    def give_child(self,node):
        self.children.append(node)

    def become_leaf(self):
        self.children = None

    def child_disp(self):
        for each in self.children:
            print each.name

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


class Tree: # ['good','high','good','yes']    #0
    def __init__(self,root):
        self.root = root

    def display_tree(self):
        self.root.display_children()

    def predict(self,data_point,node=None):
        if node == None:
            node = self.root
        if len(node.children) == 0:
            return node.name
        else:
            print len(node.children), len(node.branches.keys()), len(node.children)
            return self.predict(data_point, node.children[node.branches.keys().index(data_point[node.name])])



class DTModel:
    def __init__(self,tree):
        self.predictions = []
        self.tree = tree

    def predict(self,dataset):
        for each in dataset:
            self.predictions.append(self.tree.predict(each))
        return self.predictions
