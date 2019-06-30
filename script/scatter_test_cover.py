import sys
sys.path.append("..")
from util.fs_util import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

X = pd.read_csv(get_path("results.csv"))

# Filter dataframe by deliverable
d4_df = X[X["delivId"] == "d4"]

# Create new Dataframe to draw
df = pd.DataFrame(columns = ["Coverage Score", "Test Score"])

# TODO: We cannot depend on the D4 dataframe for the coverage score - coverage
#       is not measured in the AutoTest run for it.
df["Coverage Score"] = d4_df["output.report.scoreCover"]
df["Test Score"] = d4_df["output.report.scoreTest"]