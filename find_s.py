#-------------------------------------------------------------------------
# AUTHOR: Vincent Verdugo
# FILENAME: find_s.py
# SPECIFICATION: This program finds the maximally specific hypothesis of the dataset
# FOR: CS 4210 - Assignment #1
# TIME SPENT: 25 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv
# number of features (input variables) in the dataset
num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
for index, instance in enumerate(db):
  if instance[num_attributes] == 'Yes':
    for i in range(num_attributes):
      hypothesis[i] = instance[i]
    break

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
# loop through the entire dataset (a list of instances, each instance is a row)
for index, instance in enumerate(db):
  # if the current row is a positive instance
  if instance[num_attributes] == 'Yes':
    # loop through this instance
    for i in range(num_attributes):
      # if the corresponding value of the instance is the same as the hypothesis, do nothing
      if hypothesis[i] == instance[i]:
        pass
      # otherwise they are different, so we need to make it more general
      else:
        hypothesis[i] = '?'

# After looping through the entire db (list of instances), we should have the maximally specific hypothesis.
print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)