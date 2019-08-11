import sys
sys.path.append("..")
from typing import *
from util.fs_util import *
from util.deliv_util import *
import pandas as pd

X = pd.read_csv(get_path_dir("data/310", "pushes.csv"))

csids = X["commitURL"].apply(parse_csid)
X["csids"] = csids
X = X.drop("commitURL", 1)

d0_df = X[X['delivId'] == "d0"]
d1_df = X[X['delivId'] == "d1"]
d2_df = X[X['delivId'] == "d2"]
d3_df = X[X['delivId'] == "d3"]

valid_ids = csid_list(list(d3_df['csids']))
push_df = pd.DataFrame(columns=['csids','d0 num push','d1 num push','d2 num push', 'd3 num push', 'overall'], index=valid_ids)
push_df['csids'] = valid_ids

csid_0 = d0_df['csids'].apply(tup_to_str)
d0_df['csids'] = csid_0

csid_1 = d1_df['csids'].apply(tup_to_str)
d1_df['csids'] = csid_1

csid_2 = d2_df['csids'].apply(tup_to_str)
d2_df['csids'] = csid_2

csid_3 = d3_df['csids'].apply(tup_to_str)
d3_df['csids'] = csid_3

for csid in valid_ids:
    # D0
    _commit_df = d0_df[d0_df['csids'].str.contains(csid)]
    num_commits = len(_commit_df.index)
    commit_df.loc[csid, 'd0 num push'] = num_commits
    # D1
    _commit_df = d1_df[d1_df['csids'].str.contains(csid)]
    num_commits = len(_commit_df.index)
    push_df.loc[csid, 'd1 num push'] = num_commits
    # D2
    _commit_df = d2_df[d2_df['csids'].str.contains(csid)]
    num_commits = len(_commit_df.index)
    push_df.loc[csid, 'd2 num push'] = num_commits
    # D3
    _commit_df = d3_df[d3_df['csids'].str.contains(csid)]
    num_commits = len(_commit_df.index)
    push_df.loc[csid, 'd3 num push'] = num_commits


push_df.to_csv(get_path_dir("data/cleaned/310", "num_commits_vs_scores_full.csv"), index=False)
