import sys
sys.path.append("..")
from typing import *
from util.fs_util import *
from util.deliv_util import *
import pandas as pd
import numpy as np

X = pd.read_csv(get_path_dir("data/310", "results.csv"))

csids = X["commitURL"].apply(parse_csid_to_list)
X["csids"] = csids
X = X.drop("commitURL", 1)

# Rename columns to be more readable
X.rename(columns={'output.timestamp': 'timestamp', 'output.report.scoreCover': 'coverage', 
'output.report.scoreTest': 'test', 'output.report.scoreOverall': 'overall'}, inplace=True)

d0_df = X[X['delivId'] == "d0"]
d1_df = X[X['delivId'] == "d1"]
d2_df = X[X['delivId'] == "d2"]
d3_df = X[X['delivId'] == "d3"]
d4_df = X[X['delivId'] == 'd4']

print(d3_df)

valid_ids_unflattened = list(d3_df['csids'])
valid_ids = flatten_ids(valid_ids_unflattened)

commit_df = pd.DataFrame(columns=['csids','d0','d1','d2', 'd3', 'coverage', 'overall'], index=valid_ids)
commit_df['csids'] = valid_ids

csid_0 = d0_df['csids'].apply(list_to_str)
d0_df['csids'] = csid_0

csid_1 = d1_df['csids'].apply(list_to_str)
d1_df['csids'] = csid_1

csid_2 = d2_df['csids'].apply(list_to_str)
d2_df['csids'] = csid_2

csid_3 = d3_df['csids'].apply(list_to_str)
d3_df['csids'] = csid_3

for csid in valid_ids:
    # D0
    _commit_df = d0_df[d0_df['csids'].str.contains(csid)]
    num_pushes = len(_commit_df.index)
    commit_df.loc[csid, 'd0'] = num_pushes

    # D1
    _commit_df = d1_df[d1_df['csids'].str.contains(csid)]
    num_pushes = len(_commit_df.index)
    commit_df.loc[csid, 'd1'] = num_pushes

    # D2
    _commit_df = d2_df[d2_df['csids'].str.contains(csid)]
    num_pushes = len(_commit_df.index)
    commit_df.loc[csid, 'd2'] = num_pushes

    # D3
    _commit_df = d3_df[d3_df['csids'].str.contains(csid)]
    num_pushes = len(_commit_df.index)
    commit_df.loc[csid, 'd3'] = num_pushes

valid_ids_unflattened = list(d4_df['csids'])
valid_ids = flatten_ids(valid_ids_unflattened)

csids_str = d4_df['csids'].apply(list_to_str)
d4_df['csids'] = csids_str

for csid in valid_ids:
    grade_df = d4_df[d4_df['csids'].str.contains(csid)]
    cover_dfs = d3_df[d3_df['csids'].str.contains(csid)]
    cover_latest_row = cover_dfs.loc[cover_dfs['timestamp'].idxmax()]
    cover_latest_val = cover_latest_row['coverage']
    overall = grade_df['overall'].values[0]
    commit_df.loc[csid, 'overall'] = overall
    commit_df.loc[csid, 'coverage'] = cover_latest_val

# Drop any rows with missing data
commit_df = commit_df.dropna()
commit_df = commit_df[commit_df['overall'] != 0]
print(commit_df)

commit_df.to_csv(get_path_dir("data/cleaned/310", "num_commits_vs_scores_full.csv"), index=False)
