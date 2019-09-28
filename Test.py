# Draft Calculator File

# last Update : 9.27.19

#### To Do:
# update info to match FullRoster.csv label changes
# add section on removing players not kept or rows with no names listed
# ensure faab works properly

import pandas as pd
import numpy as np


full_roster = pd.read_csv('data/Teams/team_info.csv')

print(full_roster.faab)

full_roster['faab'] = full_roster['faab'].str.split('$').str[1]

print(full_roster.faab)

full_roster.to_csv('data/Teams/team_info.csv', sep=',', index=False, encoding='utf-8')
