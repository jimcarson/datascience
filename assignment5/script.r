library("caret")
library("rpart")
library("tree")
library("randomForest")
library("e1071")
library("ggplot2")

t = read.csv("seaflow_21min.csv")
# Question 1: How many particles labeled synecho
summary(t$pop)
# Question 2: What is the 3rd Quantile of the field fsc_small
# Precision will make a difference in the second call
summary(t)
summary(t$fsc_small, digits=12) 

# splitdf function will return a list of training and testing sets
splitdf <- function(dataframe, seed=NULL) {
	if (!is.null(seed)) set.seed(seed)
	index <- 1:nrow(dataframe)
	trainindex <- sample(index, trunc(length(index)/2))
	trainset <- dataframe[trainindex, ]
	testset <- dataframe[-trainindex, ]
	list(trainset=trainset,testset=testset)
}

splits = splitdf(t, seed=1234)
training = splits$trainset
test = splits$testset

# Question 3: mean time of training set
mean(training$time)

# Question 4 - plot pe vs chi_small.  What we should see is some overlap.
g = ggplot(training, aes(pe, chl_small))
g + geom_point() + geom_point(aes(color = pop)) 
h = ggplot(test, aes(pe, chl_small))
h + geom_point() + geom_point(aes(color = pop)) 


# Decision Tree model --  the "class" avoids having to round and remap data.
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
dt_model <- rpart(fol, method="class", data=training)

# Question 5: what populations, if any, is the tree *incapable* of measuring?
# (Hint: look for the one that's not listed.)
# Question 6: Verify there's a threshold on PE learned in the model.
# Question 7: Based on the tree, which variables appear most important
print(dt_model)

# Question 8: Decision tree prediction.
# 5326 false, 30846 true = .852759
dt_predict <- predict(dt_model, newdata=test, type="class")
dt_result = dt_predict == test$pop
summary(dt_result)

# Bonus points: A different decision tree method
#  3184 false, 32988 true = 0.912...
myformula <-  pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small
ctree_model = ctree(myformula, data=training)
ct_predict = predict(ct_model, newdata=test)
ct_result =  ct_predict == test$pop
summary(ct_result)

# Question 9: Random Forests
# 2873 false, 32299 true = .9205739
library("randomForest")
rf_model <- randomForest(fol, data=training)
rf_predict = predict(rf_model, newdata=test)
rf_result = rf_predict == test$pop
summary(rf_result)

# Question 10: which varibles appear most important in terms of gini
# impurity measure
importance(rf_model)
#          MeanDecreaseGini
#fsc_small        2707.8413
#fsc_perp         2029.5238
#fsc_big           205.2021
#pe               8925.3778
#chl_big          4789.3601
#chl_small        8211.2013



# Question 11: Support Vector Machine
# 2869 false, 33303 true = .9206845
library("e1071")
svm_model = svm(fol, data=training)
svm_predict = predict(svm_model, newdata=test)
svm_result = svm_predict == test$pop
summary(svm_result)

# Question 12: Confusion matrices.
# What appears to be the most common error?  I found the DT one more helpful.
table(pred = dt_predict, true = test$pop) # Decision tree
table(pred = ct_predict, true = test$pop)
table(pred = rf_predict, true = test$pop) # Random Forest
table(pred = svm_predict, true = test$pop) # Support Vector Machine

# Question 13: We assumed variables were continuous.  One of them has a
# lot of clustering.  
plot(t$chl_big, t$chl_small)
plot(t$fsc_big, t$fsc_small)
plot(t$fsc_perp, t$pe)

# 
# Just for kicks, let's check this out without this variable in our
# function.
#
newfol <- formula(pop ~ fsc_small + fsc_perp + pe + chl_big + chl_small)
new_dt_model <- rpart(newfol, method="class", data=training)
print(new_dt_model)
new_dt_predict <- predict(new_dt_model, newdata=test, type="class")
new_dt_result = new_dt_predict == test$pop
summary(new_dt_result)

# Answer: Not much!  

# Question 14: Remove File 208 from the mix and run the SVM again.
# What's the change in accuracy?

t2 = subset(t, t$file_id != 208)

# Resample.
splits = splitdf(t2, seed=1234)
new_training = splits$trainset
new_test = splits$testset

library("e1071")
new_svm_model = svm(newfol, data=new_training)
new_svm_predict = predict(new_svm_model, newdata=new_test)
new_svm_result = new_svm_predict == new_test$pop
summary(new_svm_result)
# 810 false, 29364 true = .9731557

# .9731557 - .9206845 = 0.0524712 == this is very significant!
