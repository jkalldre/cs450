from sklearn import datasets
from sklearn import tree
import graphviz


iris = datasets.load_iris()


classifier = tree.DecisionTreeClassifier()
model      = classifier.fit(iris.data,iris.target)

# dot_data = tree.export_graphviz(classifier, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("iris")
#
# dot_data = tree.export_graphviz(classifier, out_file=None,
#                          feature_names=iris.feature_names,
#                          class_names=iris.target_names,
#                          filled=True, rounded=True,
#                          special_characters=True)
# graph = graphviz.Source(dot_data)

print model.predict(iris.data)
print iris.target
