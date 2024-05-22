import random
import math
import numpy as np

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier

def get_splits(n, k, seed):
  splits = None

  # Implement your code to construct the splits here
  splits = [[] for _ in range(k)]
  start_idx = k % n
  splits_idx = 0
  for i in range(start_idx, n):
    splits[splits_idx % k].append(i)
    splits_idx += 1
  for i in range(start_idx):
    splits[splits_idx % k].append(i)
    splits_idx += 1
  for li in splits:
    li.sort()
  
  return splits

def my_cross_val(method, X, y, splits):
  accuracies = []
  if method == 'GaussianNB':
    model = GaussianNB()
  elif method == 'LinearSVC':
    model = LinearSVC(dual='auto', max_iter=2048, random_state=412)
  elif method == 'SVC':
    model = SVC(gamma='scale', C=10, random_state=412)
  elif method == 'DecisionTreeClassifier':
    model = DecisionTreeClassifier(max_depth=5, random_state=412)
  elif method == 'AdaBoostClassifier':
    model = AdaBoostClassifier( algorithm='SAMME', random_state=412)
  elif method == 'XGBClassifier':
    model = XGBClassifier(max_depth=6, random_state=412)
  elif method == 'MLPClassifier':
    model = MLPClassifier(alpha=1, max_iter=64, shuffle=False, random_state=412)

  # Implement your code to calculate the Accuracies here
  for li in splits:
    train_X, train_y, test_X, test_y = [], [], [], []
    for i in range(len(X)):
      if i not in li:
        train_X.append(X[i])
        train_y.append(y[i])
      else:
        test_X.append(X[i])
        test_y.append(y[i])
    model.fit(train_X, train_y)
    score = model.score(test_X, test_y)
    accuracies.append(score)
  
  return np.array(accuracies)

# test line