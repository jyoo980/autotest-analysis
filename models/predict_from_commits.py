import sys
sys.path.append("..")
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from math import sqrt
from util.fs_util import *
import pandas as pd

scaler = StandardScaler()
tree_model = DecisionTreeRegressor()
rf_model = RandomForestRegressor(max_depth=200, n_estimators=100)
data = pd.read_csv(get_path_dir("data/cleaned/310", "num_commits_vs_scores.csv"))

n,d = data.shape

# Training set
X_train = data.head(n // 2)
y_train = X_train['overall'].apply(int)
X_train = X_train.drop(['csids', 'coverage', 'overall'], axis=1)
train_scaled = scaler.fit_transform(X_train)

# Validation set
X_valid = data.tail(n // 2)
y_valid = X_valid['overall'].apply(int)
X_valid = X_valid.drop(['csids', 'coverage', 'overall'], axis=1)
valid_scaled = scaler.transform(X_valid)

# Fit model
tree_model = tree_model.fit(train_scaled, y_train)
rf_model = rf_model.fit(train_scaled, y_train)

# Training error
tree_mse = mean_squared_error(y_train, tree_model.predict(train_scaled))
tree_mae = mean_absolute_error(y_train, tree_model.predict(train_scaled))
rf_mse = mean_squared_error(y_train, rf_model.predict(train_scaled))
rf_mae = mean_absolute_error(y_train, rf_model.predict(train_scaled))

print("Decision Tree training mse = ",tree_mse," & mae = ",tree_mae," & rmse = ", sqrt(tree_mse))
print("Random Forest training mse = ",rf_mse," & mae = ",rf_mae," & rmse = ", sqrt(rf_mse))
