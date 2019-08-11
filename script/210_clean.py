import sys
sys.path.append("..")
from typing import *
from util.fs_util import *
from util.deliv_util import *
import pandas as pd

X = pd.read_csv(get_path_dir("data/210", "results.csv"))

# Parse the CSID from the commit URL
X['csids'] = X['commitURL'].apply(parse_one_csid)

# Remove anything that is not phase1,2,3,4,5
challenge1_rows = X[X['delivId'] == "challenge1"].index
challenge2_rows = X[X['delivId'] == "challenge2"].index
challenge3_rows = X[X['delivId'] == "challenge3"].index
challenge4_rows = X[X['delivId'] == "challenge4"].index
phase5_iterator_rows = X[X['delivId'] == "phase5Iterator"].index
assign0_rows = X[X['delivId'] == "assign0"].index
assign2_rows = X[X['delivId'] == "assign2"].index
assign3_rows = X[X['delivId'] == "assign3"].index
assign4_rows = X[X['delivId'] == "assign4"].index
asgn1_rows = X[X['delivId'] == "asgn1"].index

X.drop(challenge1_rows, inplace=True)
X.drop(challenge2_rows, inplace=True)
X.drop(challenge3_rows, inplace=True)
X.drop(challenge4_rows, inplace=True)
X.drop(phase5_iterator_rows, inplace=True)
X.drop(assign0_rows, inplace=True)
X.drop(assign2_rows, inplace=True)
X.drop(assign3_rows, inplace=True)
X.drop(assign4_rows, inplace=True)
X.drop(asgn1_rows, inplace=True)

phase1_df = X[X['delivId'] == "phase1"]
phase2_df = X[X['delivId'] == "phase2"]
phase3_df = X[X['delivId'] == "phase3"]
phase4_df = X[X['delivId'] == "phase4"]
phase5_df = X[X['delivId'] == "phase5"]

# Get the csids of the people who did not drop the course
csids = phase5_df['csids'].tolist()
csids = list(dict.fromkeys(csids))

result_df = pd.DataFrame(columns=['phase1','phase2','phase3', 'phase4', 'phase5', 'coverage', 'test', 'overall'], index=csids)

# Phase1
phase1_df = X[X['delivId'] == 'phase1']
for csid in csids:
    num_autotest_runs = len(phase1_df[phase1_df['csids'] == csid].index)
    result_df.loc[csid, 'phase1'] = num_autotest_runs

# Phase 2
phase2_df = X[X['delivId'] == 'phase2']
for csid in csids:
    num_autotest_runs = len(phase2_df[phase2_df['csids'] == csid].index)
    result_df.loc[csid, 'phase2'] = num_autotest_runs

# Phase 3
phase3_df = X[X['delivId'] == 'phase3']
for csid in csids:
    num_autotest_runs = len(phase3_df[phase3_df['csids'] == csid].index)
    result_df.loc[csid, 'phase3'] = num_autotest_runs

# Phase 4
phase4_df = X[X['delivId'] == 'phase4']
for csid in csids:
    num_autotest_runs = len(phase4_df[phase4_df['csids'] == csid].index)
    result_df.loc[csid, 'phase4'] = num_autotest_runs

# Phase 5
for csid in csids:
    num_autotest_runs = len(phase5_df[phase5_df['csids'] == csid].index)
    result_df.loc[csid, 'phase5'] = num_autotest_runs

# Grades
for csid in csids:
    phase_5_runs = phase5_df[phase5_df['csids'] == csid]
    phase_5_grades = phase_5_runs.loc[phase_5_runs['output.timestamp'].idxmax()]
    overall = phase_5_grades['output.report.scoreOverall']
    coverage = phase_5_grades['output.report.scoreCover']
    test = phase_5_grades['output.report.scoreTest']
    result_df.loc[csid, 'overall'] = overall
    result_df.loc[csid, 'coverage'] = coverage
    result_df.loc[csid, 'test'] = test

# Outlier removal
result_df = result_df.dropna()
result_df = result_df[result_df['overall'] != 0]

result_df.to_csv(get_path_dir("data/cleaned/210", "210-commit-df.csv"), index=False)