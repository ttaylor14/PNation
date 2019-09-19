# loop test


import pandas as pd
import numpy as np

def marcelCalculations():

    #Create Empty set to use for export
    Result = []

    #Import Files
    # last three years of player data
    MarcelTable = pd.read_csv('data/marcel/MarcelTable.csv')

    # League Averages by Year
    lgAVG = pd.read_csv('data/marcel/lgAVG.csv')

    Year = lgAVG.index[lgAVG["Season_bat"] == 2019.0]
    Year = lgAVG[lgAVG['Season_bat']==Year1].index.values.astype(int)[0]
    print(Year)


#marcelCalculations()


"""
# Import pandas package
import pandas as pd

# making data frame
data = pd.read_csv("data/marcel/MarcelTable.csv")

# iterating the columns
for col in data.columns:
    print(col)
"""


currentYear = pd.read_csv('data/marcel/currentYear.csv')
previousYear = pd.read_csv('data/marcel/previousYear.csv')
TwoYear = pd.read_csv('data/marcel/TwoYear.csv')

# Merge all tables into one based on player name
MarcelProjectionTable = pd.merge(currentYear, previousYear, left_on=['Name_bat_Year1'], right_on=['Name_bat_Year2'], how='outer')
#MarcelProjectionTable = pd.merge(MarcelProjectionTable, TwoYear, left_on=['Name_bat_Year1'], right_on=['Name_bat_Year3'], how='outer')

print(MarcelProjectionTable['Name_bat_Year1'])

# Final Marcel Output
#MarcelProjectionTable.to_csv('data/marcel/MarcelTable.csv', sep=',', index=False, encoding='utf-8')

