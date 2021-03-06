# Cost Analysis System

# last Update : 10.5.19

# Using the following links as references:
# https://www.faketeams.com/2013/1/10/3863908/deep-auction-league-strategy-calculating-dollar-values-part-1
# https://www.faketeams.com/2013/1/14/3877620/deep-auction-league-strategy-calculating-dollar-values-part-2


## move player value next to name and rank player by value

import pandas as pd
import numpy as np

##############################################

### Setting up Roster Postion requirements ###

##############################################



# Roster Settings:
# Number of player positions

RosterSpots = 25

catcher = 1
first = 1
second = 1
third = 1
short = 1
outfield = 3
utility = 1

startingP = 5
reliefP = 2

bench = RosterSpots - (catcher + first + second + third + short + outfield + utility + startingP + reliefP)

IL = 5

NumTeams = 14


##################################
## Step 1: Define Universe Size ##
##################################


TotalPlayers = (NumTeams * RosterSpots)
TotalCatcher = (NumTeams * catcher)
TotalFirst = (NumTeams * first)
TotalSecond = (NumTeams * second)
TotalThird = (NumTeams * third)
TotalShort = (NumTeams * short)
TotalOutfield = (NumTeams * outfield)
TotalHitters = (NumTeams * (catcher + first + second + third + short + outfield + utility))

TotalStartingP = (NumTeams * startingP)
TotalReliefP = (NumTeams * reliefP)
TotalPitchers = (NumTeams * (startingP + reliefP))

TotalBench = (NumTeams * bench)
TotalIL = (NumTeams * IL)
MaxPlayers = (NumTeams * (RosterSpots + IL))





####################################
## Step 2: Calculate Category AVG ##
####################################

# possibly run Points(currentYear) to create the most recent data to use?

bstats = pd.read_csv('data/bstats.csv')
pstats = pd.read_csv('data/pstats.csv')

bstatAVG = np.mean(bstats, axis = 0)
# print(bstatAVG)


pstatAVG = np.mean(pstats, axis = 0)
# print(pstatAVG)


bstats = bstats.drop('Unnamed: 0', 1)

pstats = pstats.drop('Unnamed: 0', 1)


#########################################
## Step 3: Calculate points for player ##
#########################################


# need to adjust the standard deviation (under the division sign to represent the the league)

# (most of a col - least of a col) / (Num of teams - 1 )

# remeber some stats are reversed like ERA, WHIP, etc...??

'''
for col in bstats:
    col_AVG = col + '_AVG'
    bstats[col_AVG] = (bstats[col] - bstatAVG[col] ) / 5

for col in pstats:
    col_AVG = col + '_AVG'
    pstats[col_AVG] = (pstats[col] - pstatAVG[col] ) / 5
'''

bstats['Points_AVG'] = (bstats['Points'] - bstatAVG['Points'] ) / ( (700 - 0) / (NumTeams - 1 ) )
pstats['Points_AVG'] = (pstats['Points'] - pstatAVG['Points'] ) / ( (700 - 0) / (NumTeams - 1 ) )

print( bstats.head() )


############################
## Step 4: Sum of AVG COl ##
############################

'''
bstats.fillna(0)

columns_AVG = [column for column in bstats.columns if '_AVG' in column]
print(columns_AVG)
bstats['TotalValue'] = bstats[columns_AVG].sum()

print( bstats.head() )
bstats.to_csv('data/CostAnalysis/CostAnalysis_Bat.csv', sep=',', index=False, encoding='utf-8')

print("Success")
'''

# Basing Price on Point total?

bstats['Points_Cost'] = (bstats['Points_AVG'] )
# print(bstats['Points_Cost'])

pstats['Points_Cost'] = (pstats['Points_AVG'] )
# print(pstats['Points_Cost'])



##############################
## Step 5: Money Allocation ##
##############################


# using point totals

Percent_Hitting = 60
Percent_Pitching = 100 - Percent_Hitting

LeagueBudget = 300

TotalCashSpent = LeagueBudget * NumTeams

TotalCashHitting = TotalCashSpent * (Percent_Hitting / 100)
TotalCashPitching = TotalCashSpent * (Percent_Pitching / 100)

PriceHitterZero = (TotalCashHitting / (TotalHitters + 7) )
PricePerPointBat = ( PriceHitterZero - 1 ) / 4 # check this math??

priceB = PriceHitterZero + (bstats['Points_Cost'] * PricePerPointBat )

bstats.insert(5, 'Price', priceB)

bstats['Price'] = bstats['Price'].round(decimals=2)

PricePitcherZero = (TotalCashPitching / (TotalPitchers + 7) )
PricePerPointPit = ( PricePitcherZero - 1 ) / 4 # check this math??

priceP = PricePitcherZero + (pstats['Points_Cost'] * PricePerPointPit )

pstats.insert(5, 'Price', priceP)

pstats['Price'] = pstats['Price'].round(decimals=2)

bstats.to_csv('data/CostAnalysis/CostAnalysis_Bat.csv', sep=',', index=False, encoding='utf-8')
pstats.to_csv('data/CostAnalysis/CostAnalysis_Pit.csv', sep=',', index=False, encoding='utf-8')



##############################
## Cost Analysis on Marcel ##
#############################


Proj = pd.read_csv('data/marcel/MarcelResultTotal.csv')

ProjAVG = np.mean(Proj, axis = 0)

Proj['Points_AVG'] = (Proj['Total_Points'] - ProjAVG['Total_Points'] ) / ( (750 - 350) / (NumTeams - 1 ) )


PriceZero = (TotalCashSpent / (MaxPlayers) )
PricePerPoint = ( ( PriceZero - 1 ) / 3 ) * 2

priceProj = PriceZero + (Proj['Points_AVG'] * PricePerPoint ) - 20

Proj.insert(2, 'Price', priceProj)

Proj['Price'] = Proj['Price'].round(decimals=2)


Proj.to_csv('data/CostAnalysis/CostAnalysis_Proj.csv', sep=',', index=False, encoding='utf-8')
