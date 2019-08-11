import sys
sys.path.append("..")
from typing import *
from util.fs_util import *
from util.deliv_util import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 310 Boxplot
X_310 = pd.read_csv(get_path_dir("data/cleaned/310", "310-commit-df.csv"))
sns.boxplot(data=X_310[['d0', 'd1', 'd2', 'd3']])
plt.title("Number of commits per CS3 Deliverable")
plt.ylabel("Number of commits")
plt.xlabel("Deliverable")

plt.savefig("cs3-commit-boxplot.png", dpi=150)

# Clear plt
plt.clf()

# 210 Boxplot
X_210 = pd.read_csv(get_path_dir("data/cleaned/210", "210-commit-df.csv"))
sns.boxplot(data=X_210[['phase1', 'phase2', 'phase3', 'phase4', 'phase5']])
plt.title("Number of commits per CS2 Deliverable")
plt.ylabel("Number of commits")
plt.xlabel("Deliverable")

plt.savefig("cs2-commit-boxplot.png", dpi=150)
