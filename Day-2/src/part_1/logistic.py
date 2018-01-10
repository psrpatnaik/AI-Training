# Part 1 - Hello World - https://youtu.be/cKxRvEZd3Mw

# Follow a recipe for supervised learning (a technique to create a classifier from examples) and code it up.

import csv
from sklearn import tree


# Examples
# mass height width fruit-type

fruits_file= open("fruits.csv")

fruits_reader=csv.reader(fruits_file,delimiter=',')

features=list();
labels=list();
for line in fruits_reader:
	features.append(list(map(float,(line[1:4]))))
	labels.append(float(line[0]))

# Training Data
# features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]  # Input to classifier
#features = [[140, 1], [130, 1], [150, 0], [170, 0]]  # scikit-learn uses real-valued features
# labels = ["apple", "apple", "orange", "orange"]  # Desired output
#labels = [0, 0, 1, 1]

# Train Classifer
clf = tree.DecisionTreeClassifier()  # Decision Tree classifier
clf = clf.fit(features, labels)  # Find patterns in data

# Make Predictions
# 119.0,6.5,6.5
print (clf.predict([[119.0, 6.5,6.5]]))
# Output: 0-apple, 1-orange
# Correct output is: 1-orange
print (clf.predict([[170.0, 7.5,7.5]]))
