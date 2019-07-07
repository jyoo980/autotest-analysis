import sys
sys.path.append("..")
from typing import *
from util.fs_util import *
from util.deliv_util import *
import pandas as pd

X = pd.read_csv(get_path_dir("data/310" ,"results.csv"))

# Parse csids from commit urls, remove commit url column
csids = X["commitURL"].apply(parse_csid)
X["csids"] = csids
X = X.drop("commitURL", 1)

# Rename columns to be more readable
X.rename(columns={'output.timestamp': 'timestamp', 'output.report.scoreCover': 'coverage', 
'output.report.scoreTest': 'test', 'output.report.scoreOverall': 'overall'}, inplace=True)

d0_df = X[X['delivId'] == 'd0']
d1_df = X[X['delivId'] == 'd1']
d2_df = X[X['delivId'] == 'd2']
d3_df = X[X['delivId'] == 'd3']
d4_df = X[X['delivId'] == 'd4']

# Get the number of commits per csid pair
csids = csid_list(list(X['csids']))
commit_df = pd.DataFrame(columns=['csids','d0','d1','d2', 'd3', 'coverage', 'overall'], index=csids)

commit_df['csids'] = csids

csid_0 = d0_df['csids'].apply(tup_to_str)
d0_df['csids'] = csid_0

csid_1 = d1_df['csids'].apply(tup_to_str)
d1_df['csids'] = csid_1

csid_2 = d2_df['csids'].apply(tup_to_str)
d2_df['csids'] = csid_2

csid_3 = d3_df['csids'].apply(tup_to_str)
d3_df['csids'] = csid_3

for csid in csids:
    # D0
    commits_df = d0_df[d0_df['csids'].str.contains(csid)]
    num_commits = len(commits_df.index)
    commit_df.loc[csid, 'd0'] = num_commits

    # D1
    commits_df = d1_df[d1_df['csids'].str.contains(csid)]
    num_commits = len(commits_df.index)
    commit_df.loc[csid, 'd1'] = num_commits

    # D2
    commits_df = d2_df[d2_df['csids'].str.contains(csid)]
    num_commits = len(commits_df.index)
    commit_df.loc[csid, 'd2'] = num_commits

    # D3
    commits_df = d3_df[d3_df['csids'].str.contains(csid)]
    num_commits = len(commits_df.index)
    commit_df.loc[csid, 'd3'] = num_commits

# At this point, the number of commits for each deliverable for each CSID is filled in
# We need to get a list of csids again to remove the number of people who've dropped the course
# Since D1
csids = csid_list(list(d4_df['csids']))

csids_str = d4_df['csids'].apply(tup_to_str)
d4_df['csids'] = csids_str

for csid in csids:
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
commit_df.to_csv(get_path_dir("data/cleaned/310", "num_commits_vs_scores.csv"), index=False)
