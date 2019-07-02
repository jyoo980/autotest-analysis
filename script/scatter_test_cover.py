import sys
sys.path.append("..")
from typing import *
from util.fs_util import *
from util.deliv_util import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

X = pd.read_csv(get_path("results.csv"))

# Set up the d4 dataframe
d4_df = X[X["delivId"] == "d4"]
col_csid = d4_df["commitURL"].apply(parse_csid)
d4_df = d4_df.drop("commitURL", 1)
d4_df["csids"] = col_csid

# We need to obtain the coverage score from the d3 csv
d3_df = X[X["delivId"] == "d3"]
col_csid = d3_df["commitURL"].apply(parse_csid)
d3_df = d3_df.drop("commitURL", 1)
d3_df["csids"] = col_csid

# For each pair of csids, compute the row with the greatest timestamp
row_dict: Dict[Tuple[Optional[str], Optional[str]], Any] = {}
for _, row in d3_df.iterrows():
    csids = row["csids"]
    if csids not in row_dict:
        row_dict.update({ csids: row })
    else:
        stored_row = row_dict.get(csids)
        if row['output.timestamp'] > stored_row['output.timestamp']:
            row_dict.update({ csids: row })

for index, row in d4_df.iterrows():
    d3_row = row_dict.get(row["csids"])
    d4_df.loc[index, 'output.report.scoreCover'] = d3_row['output.report.scoreCover']

d4_df.to_csv(get_path("test_cover_data.csv"))

sns.set()
sns.scatterplot('Coverage Score', 'Test Score', data=d4_df, s=25)
plt.show()