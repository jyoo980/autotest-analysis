import sys
sys.path.append("..")
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from math import sqrt
from util.fs_util import *
import pandas as pd

clf = RandomForestRegressor(max_depth=200, n_estimators=100)
data = pd.read_csv(get_path_dir("data/cleaned/310", "num_commits_vs_scores_full.csv"))

labels = data['overall']
X = data.drop(['csids', 'coverage', 'overall'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.10, random_state=2)

clf.fit(X_train, y_train)
print("Classification score - RandomForestRegressor: " + str(clf.score(X_test, y_test)))

clf = GradientBoostingRegressor(n_estimators = 500, max_depth = 5, min_samples_split = 2, learning_rate = 0.2, loss = 'ls')
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))