import sys
sys.path.append("..")
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from math import sqrt
from util.fs_util import get_path_dir
import pandas as pd

clf = RandomForestRegressor(max_depth=95, n_estimators=15, max_features=5)
data = pd.read_csv(get_path_dir("data/cleaned/210", "210-commit-df.csv"))

labels = data['overall']
X = data.drop(['coverage', 'overall'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.10, random_state=2)

clf.fit(X_train, y_train)
print("Classification score - RandomForestRegressor:     " + str(clf.score(X_test, y_test)))

clf = GradientBoostingRegressor(n_estimators = 600, max_depth = 10, min_samples_split = 2, learning_rate = 0.1, loss = 'ls')
clf.fit(X_train, y_train)
print("Classification score - GradientBoostingRegressor: " + str(clf.score(X_test, y_test)))