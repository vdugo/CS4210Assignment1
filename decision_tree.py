#-------------------------------------------------------------------------
# AUTHOR: Vincent Verdugo
# FILENAME: decision_tree.py
# SPECIFICATION: This program will read a dataset and output the ID3 (Iterative Dichotomiser 3) decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: 50 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []
num_attributes = 4

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 2D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
# For each instance in the dataset
for instance in db:
  # Create a list, then run through each instance
  replacement = []
  for index, value in enumerate(instance):
    # Replace each value with an arbitrary number
    if index == 0:
      if value == 'Young':
        replacement.append(1)
      elif value == 'Prepresbyopic':
        replacement.append(2)
      else:
        replacement.append(3)
    elif index == 1: 
      if value == 'Myope':
        replacement.append(1)
      else:
        replacement.append(2)
    elif index == 2: 
      if value == 'No':
        replacement.append(1)
      else:
        replacement.append(2)
    elif index == 3:
      if value == 'Reduced':
        replacement.append(1)
      else:
        replacement.append(2)
  # append the instance replaced by integer values
  X.append(replacement)
# Now X will be the same as db, but each value for each instance is replaced by an arbitrary integer
print(X)

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# Go through every instance, only paying attention to the last column (the output variable)
# append a 1 if it is a positive instance, otherwise append a 2 for a negative instance
for instance in db:
  if instance[num_attributes] == 'Yes':
    Y.append(1)
  else:
    Y.append(2)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
