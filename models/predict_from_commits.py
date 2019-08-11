import sys
sys.path.append("..")
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from math import sqrt
from util.fs_util import get_path_dir
from plot_learning_curve import *
import pandas as pd
import matplotlib.pyplot as plt

clf = RandomForestRegressor(max_depth=95, n_estimators=15, max_features=4)
data = pd.read_csv(get_path_dir("data/cleaned/310", "num_commits_vs_scores_full-2.csv"))

# Prep data for training/prediction
labels = data['overall']
X = data.drop(['csids', 'coverage', 'overall', 'average_num_commits'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.10, random_state=2)

clf.fit(X_train, y_train)
print("Classification score - RandomForestRegressor:     " + str(clf.score(X_test, y_test)))

# Feature Importance
predictors = list(X_train)
feat_imp = pd.Series(clf.feature_importances_, predictors).sort_values(ascending=False)
feat_imp.plot(kind='bar', title='Importance of Features', color="#42739d")
plt.xticks(rotation=45)
plt.ylabel('Feature Importance Score')
plt.tight_layout()
plt.savefig("cs3-feature-importance.png", dpi=150)
plt.clf()
# End feature Importance

# Use GBR
clf = GradientBoostingRegressor(n_estimators = 600, max_depth = 5, min_samples_split = 2, learning_rate = 0.1, loss = 'ls', max_features=4, warm_start=True)
clf.fit(X_train, y_train)
print("Classification score - GradientBoostingRegressor: " + str(clf.score(X_test, y_test)))
