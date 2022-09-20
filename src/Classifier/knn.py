
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("breast-cancer.csv")

y = df['diagnosis']
X = df.drop('diagnosis', axis = 1)
X = X.drop('id', axis = 1)
# Separating the dependent and independent variable
  
X_train, X_test, y_train, y_test = train_test_split(
             X, y, test_size = 0.3, random_state = 0)
# Splitting the data into training and testing data

K = []
training = []
test = []
scores = {}
  
for k in range(2, 21):
    clf = KNeighborsClassifier(n_neighbors = k)
    clf.fit(X_train, y_train)
  
    training_score = clf.score(X_train, y_train)
    test_score = clf.score(X_test, y_test)
    K.append(k)
  
    training.append(training_score)
    test.append(test_score)
    scores[k] = [training_score, test_score]

for keys, values in scores.items():
    print(keys, ':', values)

# ax = sns.stripplot(K, training);
# # ax.set(xlabel ='values of k', ylabel ='Training Score')

# # plt.show()
# # function to show plot
# ax = sns.stripplot(K, test);
# ax.set(xlabel ='values of k', ylabel ='Test Score')
# plt.show()

plt.scatter(K, training, color ='k')
plt.scatter(K, test, color ='g')
plt.xlabel('values of k')
plt.ylabel('scores (black=training) (green=test)')
plt.show()
# For overlapping scatter plots


