
library(e1071)
library(rpart)
library(MASS)
library(caret)

setwd("D:/Documents/school/18_winter/450_cs/R")
vowel <- read.csv('Data/vowel.csv')


index <- 1:nrow(vowel)
testindex <- sample(index, trunc(length(index)/3))
testset <- vowel[testindex,]
trainset <- vowel[-testindex,]
#tab <- table(pred = prediction, true = testset[,13])
#print(tab)
#confusionMatrix(data = prediction, reference = testset[,13])

#test for gamma
model <- svm(Class~.,data = trainset, gamma = .1, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])


model <- svm(Class~.,data = trainset, gamma = .2, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .3, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .4, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .5, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .6, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .7, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .8, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .9, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

#gamma at .4 worked the best
#test for C
model <- svm(Class~.,data = trainset, gamma = .4, cost = .1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .4, cost = .2, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .4, cost = .6, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .4, cost = .7, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .4, cost = .8, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .4, cost = .9, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .4, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .4, cost = 1.1, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

model <- svm(Class~.,data = trainset, gamma = .4, cost = 1.2, type="C-classification")
prediction <- predict(model, testset[,-13])
postResample(pred = prediction, obs = testset[,13])

# best results at 1 for C
model <- svm(Class~.,data = trainset, gamma = .4, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-13])
confusionMatrix(data = prediction, reference = testset[,13])

##################################END VOWEL TESTS#########################
letters <- read.csv('Data/letters.csv')

index <- 1:nrow(letters)
testindex <- sample(index, trunc(length(index)/3))
testset <- letters[testindex,]
trainset <- letters[-testindex,]

#test for gamma
model <- svm(letter~.,data = trainset, gamma = .1, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])


model <- svm(letter~.,data = trainset, gamma = .2, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .3, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .4, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .5, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .6, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .7, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .8, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .9, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

#gamma at .4 worked the best
#test for C
model <- svm(letter~.,data = trainset, gamma = .4, cost = .1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .4, cost = .2, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .4, cost = .6, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .4, cost = .7, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .4, cost = .8, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .4, cost = .9, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .4, cost = 1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .4, cost = 1.1, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])

model <- svm(letter~.,data = trainset, gamma = .4, cost = 1.8, type="C-classification")
prediction <- predict(model, testset[,-1])
postResample(pred = prediction, obs = testset[,1])
confusionMatrix(data = prediction, reference = testset[,13])








