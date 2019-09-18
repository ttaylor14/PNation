# Projected Rankings System

# last Update : 9.2.19



#### points(currentSeason)
# Import data from pybaseball to create point totals for the currentSeason
# Complete

#### Rosters_To_Team_Files()
# This seperates full_roster into each team
# Complete

#### Roster_lahman_tag()
# This applies lahman, retro, bbref tags to players
# Complete (some players skipped?)


import pandas as pd
import numpy as np

#################################################

#### Create Batting and Pitching Point totals ###

#################################################

# Creates files for batting and pitching point totals



def points(currentSeason):
    from pybaseball import batting_stats


    data = batting_stats(currentSeason, qual=1)



    # Procrastination Points

    # ESPN Settings

    ## Batting Scoring

    R = 1
    # Runs Scored

    Single = 0
    # Singles

    Double = 0
    # Doubles

    Triple = 0
    # Triples

    HR = 2
    # Home Runs

    TB = 1
    # Total Bases

    RBI = 1
    # Runs Batted In

    BB = 1
    # Walks

    K = -1
    # Strikeouts

    SB = 1
    # Stolen Bases


    AB = 0
    # At Bats

    Hits = 0
    # Hits

    XBH = 0
    # Extra Base Hits

    GWRBI = 0
    # Game Winning RBI

    IBB = 1
    # Intentional Walks

    HBP = 0
    # Hit by Pitch

    SAC = 0
    # Sacrifices

    CS = -1
    # Caught Stealing

    SBN = 0
    # Net Stolen Bases

    GIDP = 0
    # Ground into Double Plays

    CYC = 20
    # Hitting for the Cycle

    GSHR = 4
    # Grand Slam Home Runs

    BTW = 0
    # Batter Team Win

    BTL = 0
    # Batter Team Loss



    points = ( ( R * data['R'] )
    + ( Single * data['1B'] )
    + ( Double * data['2B'] )
    + ( Triple * data['3B'] )
    + ( HR * data['HR'] )
    + ( TB * ( data['1B'] + (2 * data['2B']) + (3 * data['3B']) + (4 * data['HR']) ) )
    + ( RBI * data['RBI'] )
    + ( BB * data['BB'] )
    + ( K * data['SO'] )
    + ( SB * data['SB'] )
    + ( AB * data['AB'] )
    + ( Hits * data['H'])
    + ( XBH * ( data['2B'] + data['3B'] + data['HR']) )
    + ( IBB * data['IBB'] )
    + ( HBP * data['HBP'] )
    + ( CS * data['CS'] ) )


    # missing Sac and GWRBI and everything past CS

    data['Points'] = points

    BattingStats = data[['Season', 'Name', 'Team', 'Age', 'Points', 'G', 'PA', 'AB', 'AVG', 'H', '1B', '2B', '3B', 'HR', 'R', 'RBI', 'BB', 'IBB', 'SO', 'HBP', 'SB', 'CS', 'Pitches']]
    #BattingStats.sort_values("Points", inplace=True)
    # print(BattingStats)


    BattingStats.to_csv('data/bstats.csv')

    ## Fielding

    FC = 0
    # Fielding Chances

    PO = 0
    # Put Outs

    AST = 0
    # Assists

    OFAST = 0
    # Outfield Assists

    BatE = -1
    # Errors

    DPT = 0
    # Double Plays Turned







    from pybaseball import pitching_stats

    pdata = pitching_stats(currentSeason)

    ### Pitching

    IP = 3
    # Innings Pitched
    # INNINGS PITCHED / OUTS RECORDED
    # Although Innings Pitched are typically displayed throughout the game, pitchers will accrue points for each out they record. The point value entered here applies to outs recorded. For example, if you choose a value of 2 points, a pitcher that pitches 1 inning will earn 6 points (2 points * 3 outs).

    ER = -2
    # Earned Runs

    K = 1
    # Strikeouts

    SO = 5
    # Shutouts

    W = 5
    # Wins

    L = -5
    # Losses

    SV = 5
    # Saves

    BS = -5
    # Blown Saves


    G = 0
    # Appearances

    GS = 0
    # Games Started

    H = -1
    # Hits Allowed

    RA = 0
    # Runs Allowed

    HR = 0
    # Home Runs Allowed

    BB = -1
    # Walks Issued

    HB = -1
    # Hit Batsmen

    WP = -1
    # Wild Pitches

    B = -1
    # Balks

    PKO = 2
    # Pick Offs

    QS = 5
    # Quality Starts

    CG = 10
    # Complete Games

    NH = 15
    # No Hitters

    PG = 20
    # Perfect Games

    BF = 0
    # Batters Faced

    PC = 0
    # Pitch Count

    SOP = 0
    # Save Opportunities

    HD = 0
    # Holds

    PTW = 0
    # Pitcher Team Win

    PTL = 0
    # Pitcher Team Loss

    SVHD = 0
    # Saves Plus Holds


    ppoints = ( ( IP * pdata['IP'] )
    + ( ER * pdata['ER'] )
    + ( K * pdata['SO'] )
    + ( SO * pdata['ShO'] )
    + ( W * pdata['W'] )
    + ( L * pdata['L'] )
    + ( SV * pdata['SV'] )
    + ( BS * pdata['BS'] )
    + ( G * pdata['G'] )
    + ( GS * pdata['GS'] )
    + ( BS * pdata['BS'] )
    + ( H * pdata['H'] )
    + ( RA * pdata['R'] )
    + ( HR * pdata['HR'] )
    + ( BB * pdata['BB'] )
    + ( HB * pdata['HBP'] )
    + ( IBB * pdata['IBB'] )
    + ( B * pdata['BK'] )
    #+ ( PKO * pdata['PKO'] )
    + ( QS * pdata['BK'] )
    + ( CG * pdata['CG'] )
    #+ ( NH * pdata['NH'] )
    #+ ( PG * pdata['PG'] )
    #+ ( BF * pdata['BF'] )
    + ( PC * pdata['Pitches'] )
    #+ ( SOP * pdata['SOP'] )
    #+ ( HD * pdata['HD'] )
    )

    pdata['Points'] = ppoints

    PitchingStats = pdata[['Season', 'Name', 'Team', 'Age', 'Points', 'W', 'L', 'ERA', 'WAR', 'G', 'GS', 'CG', 'ShO', 'SV', 'BS', 'IP', 'H', 'R', 'HR', 'BB', 'IBB', 'HBP', 'BK', 'SO', 'Pitches']]
    # PitchingStats.sort_values("Points", inplace=True)
    # print(PitchingStats)
    PitchingStats.to_csv('data/pstats.csv')


#####################################

#### Combine Batting and Pitching ###

#####################################

# Combines Batting and Pitching csv files into one
# ranks players by points and assigns a rank

def combinePoints():

    bstats = pd.read_csv('data/bstats.csv')
    pstats = pd.read_csv('data/pstats.csv')

    bstats = bstats.add_suffix('_bat')
    pstats = pstats.add_suffix('_pit')

    #Combine CSV
    Rankings = pd.merge(bstats, pstats, left_on=['Name_bat'], right_on=['Name_pit'], how='outer', suffixes=('_bat', '_pit'))
    Rankings.drop(labels=['Unnamed: 0_bat', 'Unnamed: 0_pit'], axis=1,inplace = True)
    Rankings = Rankings.fillna(0)
    Total_Points = Rankings['Points_bat'] + Rankings['Points_pit']
    Rankings.insert(1, 'Total_Points', Total_Points)
    Rankings = Rankings.sort_values('Total_Points', ascending=False)
    Rankings = Rankings.reset_index(drop=True)
    Rank = Rankings.index
    Rankings.insert(0, 'Rank', Rank)

    Rankings.to_csv('data/Rankings.csv', sep=',', index=False, encoding='utf-8')


########################################

#### Creating league Average by Year ###

########################################

def lgAVGBat():
    # Import batting Stats
    BattingStats = pd.read_csv('data/bstats.csv')
    # find year of data
    Year = BattingStats['Season'][1]
    NumPlayers = len(BattingStats.index)


    # read lgAVG file
    lgAVG = pd.read_csv('data/marcel/lgAVGBat.csv')

    # locate correct year on file, remove previous entry, and add sum
    lgAVG = lgAVG[lgAVG.Season != Year]
    lgAVG.loc[Year] = BattingStats.sum()

    # delete unneeded Information columns
    lgAVG['Name'] = 'X'
    lgAVG['Team'] = 'X'

    # Change Season Calue to the correct year rather than the Sum
    lgAVG['Season'][Year] = Year
    # add number of players
    lgAVG['NumPlayers'][Year] = NumPlayers

    # drop unneeded column
    lgAVG.drop(labels=['Unnamed: 0'], axis=1,inplace = True)

    # Sort by Season and reset Index
    lgAVG = lgAVG.sort_values('Season', ascending=False)
    lgAVG = lgAVG.reset_index(drop=True)

    # Export Data to File
    lgAVG.to_csv('data/marcel/lgAVGBat.csv')


def lgAVGPit():
    # Import batting Stats
    PitchingStats = pd.read_csv('data/pstats.csv')
    # find year of data
    Year = PitchingStats['Season'][1]
    NumPlayers = len(PitchingStats.index)

    # read lgAVG file
    lgAVG = pd.read_csv('data/marcel/lgAVGPit.csv')

    # locate correct year on file, remove previous entry, and add sum
    lgAVG = lgAVG[lgAVG.Season != Year]
    lgAVG.loc[Year] = PitchingStats.sum()

    # delete unneeded Information columns
    lgAVG['Name'] = 'X'
    lgAVG['Team'] = 'X'

    # Change Season Calue to the correct year rather than the Sum
    lgAVG['Season'][Year] = Year
        # add number of players
    lgAVG['NumPlayers'][Year] = NumPlayers

    # drop unneeded column
    lgAVG.drop(labels=['Unnamed: 0'], axis=1,inplace = True)

    # Sort by Season and reset Index
    lgAVG = lgAVG.sort_values('Season', ascending=False)
    lgAVG = lgAVG.reset_index(drop=True)

    # Export Data to FIle
    lgAVG.to_csv('data/marcel/lgAVGPit.csv')


def lgAVG():
    # Run LGAVG for Batting and Pitching
    lgAVGBat()
    lgAVGPit()
    # Retrieve Data and add Suffix
    lgBat = pd.read_csv('data/marcel/lgAVGBat.csv')
    lgBat = lgBat.add_suffix('_bat')
    lgPit = pd.read_csv('data/marcel/lgAVGPit.csv')
    lgPit = lgPit.add_suffix('_pit')
    # Merge both files into one file
    lgAVG = pd.merge(lgBat, lgPit, left_on=['Season_bat'], right_on=['Season_pit'], how='outer')

    lgAVG.drop(labels=['Unnamed: 0_bat'], axis=1,inplace = True)
    lgAVG.drop(labels=['Unnamed: 0_pit'], axis=1,inplace = True)

    # Export Combine File for later use
    lgAVG.to_csv('data/marcel/lgAVG.csv', sep=',', index=False, encoding='utf-8')





####################################

#### Creating Marcel Projections ###

####################################

# runs points on current and past 2 season (3 total)
# merges all files into one document
# ranks by projection for the upcoming year


def marcelCombinedFile():

    # Current or Season before Projection
    currentYear = 2019
    previousYear = (currentYear - 1)
    TwoYear = (currentYear - 2)

    points(currentYear)
    lgAVG()
    combinePoints()
    currentYear = pd.read_csv('data/Rankings.csv')
    currentYear = currentYear.add_suffix('_Year1')
    currentYear.to_csv('data/marcel/currentYear.csv', sep=',', index=False, encoding='utf-8')



    # Previous Seasons stats

    points(previousYear)
    lgAVG()
    combinePoints()
    previousYear = pd.read_csv('data/Rankings.csv')
    previousYear = previousYear.add_suffix('_Year2')
    previousYear.to_csv('data/marcel/previousYear.csv', sep=',', index=False, encoding='utf-8')


    # Two Seasons ago stats

    points(TwoYear)
    lgAVG()
    combinePoints()
    TwoYear = pd.read_csv('data/Rankings.csv')
    TwoYear = TwoYear.add_suffix('_Year3')
    TwoYear.to_csv('data/marcel/TwoYear.csv', sep=',', index=False, encoding='utf-8')

    currentYear = pd.read_csv('data/marcel/currentYear.csv')
    previousYear = pd.read_csv('data/marcel/previousYear.csv')
    TwoYear = pd.read_csv('data/marcel/TwoYear.csv')


    # Merge all tables into one based on player name
    MarcelProjectionTable = pd.merge(currentYear, previousYear, left_on=['Name_Year1'], right_on=['Name_Year2'], how='outer')
    MarcelProjectionTable = pd.merge(MarcelProjectionTable, TwoYear, left_on=['Name_Year1'], right_on=['Name_Year3'], how='outer')




    # Final Marcel Output
    MarcelProjectionTable.to_csv('data/marcel/MarcelTable.csv', sep=',', index=False, encoding='utf-8')




def marcelCalculations():


    #Import Files
    # last three years of player data
    MarcelTable = pd.read_csv('data/marcel/MarcelTable.csv')

    # League Averages by Year
    lgAVG = pd.read_csv('data/marcel/lgAVG.csv')

    # Stats we need
    BatStatNeeded = ['G', 'AB', 'AVG', 'H', '1B', '2B', '3B', 'HR', 'R', 'RBI', 'BB', 'IBB', 'SO', 'HBP', 'SB', 'CS', 'Pitches']

    # need to add Name, Age, Etc...
    #Create Empty set to use for export
    Result = pd.DataFrame(index=MarcelTable.index, columns=BatStatNeeded )
    Result = Result.fillna(0)
    Result.to_csv('data/marcel/MarcelResult.csv')

    # What Year are we using?
    Year1 = MarcelTable['Season_bat_Year1'][1]
    Year2 = MarcelTable['Season_bat_Year2'][1]
    Year3 = MarcelTable['Season_bat_Year3'][1]
    print("Year Data being Accessed: " + str(Year1) + " , " + str(Year2) + " , " + str(Year3) )

    # finds the index number of each season
    LG_Year1 = lgAVG[lgAVG['Season_bat']==Year1].index.values.astype(int)[0]
    LG_Year2 = lgAVG[lgAVG['Season_bat']==Year2].index.values.astype(int)[0]
    LG_Year3 = lgAVG[lgAVG['Season_bat']==Year3].index.values.astype(int)[0]
    print("lgAVG Index Number: " + str(LG_Year1) + " , " + str(LG_Year2) + " , " + str(LG_Year3) )
    print(" ")

    # Cycle through columns
    for ind in MarcelTable.index:
        for word in BatStatNeeded:
            Mstat = word
            print ("State being Evaluated: " + str(Mstat) )

            # Label the Stat for each year of Data
            MS_Year1 = (str(Mstat) + "_Year1")
            MS_Year2 = (str(Mstat) + "_Year2")
            MS_Year3 = (str(Mstat) + "_Year3")
            print ("State Labels: " + str(MS_Year1) + " , " + str(MS_Year2) + " , " + str(MS_Year3) )
            print(" ")

            # Weighted total of individual players stat and Plate Apperances
            MStateTotal = (MarcelTable[MS_Year1][ind] * 5) + (MarcelTable[MS_Year2][ind] * 4) + (MarcelTable[MS_Year3][ind] * 3)
            PA = (MarcelTable['PA_Year1'][ind]*.5) + (MarcelTable['PA_Year2'][ind]*.1) + (200)
            print("Player Weighted Stat: " + str(MStateTotal) + "  Player Weighted Plate Apperances: " + str(PA) )
            print(" ")

            # Calculating the Weighted Mean of state per plate apperances for that individual player
            MS_Y1 = lgAVG[Mstat][LG_Year1]/lgAVG['PA_bat'][LG_Year1] * MarcelTable['PA_Year1'][ind] * 5
            MS_Y2 = lgAVG[Mstat][LG_Year2]/lgAVG['PA_bat'][LG_Year2] * MarcelTable['PA_Year2'][ind] * 4
            MS_Y3 = lgAVG[Mstat][LG_Year3]/lgAVG['PA_bat'][LG_Year3] * MarcelTable['PA_Year3'][ind] * 3
            print("Player State Mean by year: " + str(MS_Y1) + " , " + str(MS_Y2) + " , " + str(MS_Y3) )
            print(" ")

            # Players total Weighted Plate Apperances
            Total_PAS = ( MarcelTable['PA_Year1'][ind] * 5 ) + ( MarcelTable['PA_Year2'][ind] * 4 ) + ( MarcelTable['PA_Year3'][ind] * 3 )
            print("Weighted PA: " + str(Total_PAS) )
            print(" ")

            # Adjusting ratio to match 1200 apperances
            MS_Ratio = ( (MS_Y1 + MS_Y2 + MS_Y3) * 1200 ) / Total_PAS
            print("Adjusted Ratio for 1200 PA: " + str(MS_Ratio) )
            print(" ")

            # taking league ratio out of 1200 and adding it to the actual players result to get that players ratio of stat per PA
            MS_Perct = ( MS_Ratio + MStateTotal ) / ( 1200 + Total_PAS )
            print("Adjusting with League Average: " + str(MS_Perct) )
            print(" ")

            # Take the player's ratio and multiply it by the expected number of plate apperances
            MS_Expected = ( MS_Perct * PA )
            print("Player Ratio for # of PA: " + str(MS_Expected) )
            print(" ")

            # Adjust for players age
            Age_Reg = ( ( 29 - MarcelTable['Age_bat_Year1'][ind] ) * 0.5 )

            print("Age Adjustment: " + str(Age_Reg) )
            print(" ")

            # Final Result
            Marcel_Result = MS_Expected * ( 1 + Age_Reg )
            print("Final Player Projection: " + str(Marcel_Result) )
            print(" ")

            Result.at[ind, word] = Marcel_Result
            print(Result.head())

    print(Result)
    Result.to_csv('data/marcel/MarcelResult.csv')




#####################

#### Run Programs ###

#####################


# Creates files for batting and pitching
# points(2019)

# Combines batting an dpitching files together
# combinePoints()

# Run Marcel Projections Table to later create projections
marcelCombinedFile()

## Creating a Lg Total document for Marcel Projections
# lgAVG()


# Run Marcel Projections
#marcelCalculations()
