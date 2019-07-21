import sys
sys.path.append("..")
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from math import sqrt
from util.fs_util import get_path_dir
import pandas as pd

clf = RandomForestRegressor(max_depth=95, n_estimators=15, max_features=4)
data = pd.read_csv(get_path_dir("data/cleaned/310", "num_commits_vs_scores_full-2.csv"))

labels = data['overall']
X = data.drop(['csids', 'coverage', 'overall', 'average_num_commits'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.10, random_state=2)

clf.fit(X_train, y_train)
print("Classification score - RandomForestRegressor:     " + str(clf.score(X_test, y_test)))

clf = GradientBoostingRegressor(n_estimators = 600, max_depth = 5, min_samples_split = 2, learning_rate = 0.1, loss = 'ls')
clf.fit(X_train, y_train)
print("Classification score - GradientBoostingRegressor: " + str(clf.score(X_test, y_test)))

# Hyperparamter tuning for RandomForestRegressor
# best_score = -1
# best_depth = 0
# best_num_est = 0
# for depth in range(5, 500, 5):
#     for estimators in range(10, 700, 5):
#         clf = RandomForestRegressor(max_depth=depth, n_estimators=estimators, max_features=4)
#         clf.fit(X_train, y_train)
#         clf.fit(X_train, y_train)
#         current_score = clf.score(X_test, y_test)
#         if current_score > best_score:
#             best_score = current_score
#             best_depth = depth
#             best_num_est = estimators

# print("Best error with RandomForestRegressor: " + str(best_score))
# print("With depth: " + str(best_depth))
# print("With num estimators: " + str(best_num_est))


