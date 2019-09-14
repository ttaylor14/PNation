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


marcelCalculations()
