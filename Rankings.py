# Projected Rankings System

# last Update : 10.6.19



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


currentYear = 2019

#################################################

#### Create Batting and Pitching Point totals ###

#################################################

# Creates files for batting and pitching point totals


# Procrastination Points

# ESPN Settings



def pointAmountsBat():

    global R, Single, Double, Triple, HR, TB, RBI, BB, K, SB, AB, Hits, XBH, GWRBI, IBB, HBP, SAC, CS, SBN, GIDP, CYC, GSHR, BTW, BTL
    global FC, PO, AST, OFAST, BatE, DPT

    ## Batting Scoring
    R = 1 # Runs Scored
    Single = 0 # Singles
    Double = 0 # Doubles
    Triple = 0 # Triples
    HR = 2 # Home Runs
    TB = 1 # Total Bases
    RBI = 1 # Runs Batted In
    BB = 1 # Walks
    K = -1 # Strikeouts
    SB = 1 # Stolen Bases
    AB = 0 # At Bats
    Hits = 0 # Hits
    XBH = 0 # Extra Base Hits
    GWRBI = 0 # Game Winning RBI
    IBB = 1 # Intentional Walks
    HBP = 0 # Hit by Pitch
    SAC = 0 # Sacrifices
    CS = -1 # Caught Stealing
    SBN = 0 # Net Stolen Bases
    GIDP = 0 # Ground into Double Plays
    CYC = 20 # Hitting for the Cycle
    GSHR = 4 # Grand Slam Home Runs
    BTW = 0 # Batter Team Win
    BTL = 0 # Batter Team Loss

    ## Fielding
    FC = 0 # Fielding Chances
    PO = 0 # Put Outs
    AST = 0 # Assists
    OFAST = 0 # Outfield Assists
    BatE = -1 # Errors
    DPT = 0 # Double Plays Turned

    return R, Single, Double, Triple, HR, TB, RBI, BB, K, SB, AB, Hits, XBH, GWRBI, IBB, HBP, SAC, CS, SBN, GIDP, CYC, GSHR, BTW, BTL
    return FC, PO, AST, OFAST, BatE, DPT


def pointAmountsPit():

    global IP, ER, K, SO, W, L, SV, BS, G, GS, H, RA, HR, BB, HB, WP, B, PKO, QS, CG, NH, PG, BF, PC, SOP, HD, PTW, PTL, SVHD

    ### Pitching
    IP = 3 # Innings Pitched # INNINGS PITCHED / OUTS RECORDED
    # Although Innings Pitched are typically displayed throughout the game, pitchers will accrue points for each out they record. The point value entered here applies to outs recorded. For example, if you choose a value of 2 points, a pitcher that pitches 1 inning will earn 6 points (2 points * 3 outs).
    ER = -2 # Earned Runs
    K = 1 # Strikeouts
    SO = 5 # Shutouts
    W = 5 # Wins
    L = -5 # Losses
    SV = 5 # Saves
    BS = -5 # Blown Saves
    G = 0 # Appearances
    GS = 0 # Games Started
    H = -1 # Hits Allowed
    RA = 0 # Runs Allowed
    HR = 0 # Home Runs Allowed
    BB = -1 # Walks Issued
    HB = -1 # Hit Batsmen
    WP = -1 # Wild Pitches
    B = -1 # Balks
    PKO = 2 # Pick Offs
    QS = 5 # Quality Starts
    CG = 10 # Complete Games
    NH = 15 # No Hitters
    PG = 20 # Perfect Games
    BF = 0 # Batters Faced
    PC = 0 # Pitch Count
    SOP = 0 # Save Opportunities
    HD = 0 # Holds
    PTW = 0 # Pitcher Team Win
    PTL = 0 # Pitcher Team Loss
    SVHD = 0 # Saves Plus Holds

    return IP, ER, K, SO, W, L, SV, BS, G, GS, H, RA, HR, BB, HB, WP, B, PKO, QS, CG, NH, PG, BF, PC, SOP, HD, PTW, PTL, SVHD



def points(currentSeason):
    from pybaseball import batting_stats

    data = batting_stats(currentSeason, qual=1)

    pointAmountsBat()

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
    data['Points'] = data['Points'].round(decimals=0)

    BattingStats = data[['Season', 'Name', 'Team', 'Age', 'Points', 'G', 'PA', 'AB', 'AVG', 'H', '1B', '2B', '3B', 'HR', 'R', 'RBI', 'BB', 'IBB', 'SO', 'HBP', 'SB', 'CS', 'Pitches']]

    BattingStats = BattingStats.sort_values('Points', ascending=False)
    BattingStats = BattingStats.reset_index(drop=True)


    BattingStats.to_csv('data/bstats.csv')

    from pybaseball import pitching_stats

    pdata = pitching_stats(currentSeason)

    pointAmountsPit()

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
    pdata['Points'] = pdata['Points'].round(decimals=0)

    PitchingStats = pdata[['Season', 'Name', 'Team', 'Age', 'Points', 'W', 'L', 'ERA', 'ER', 'WAR', 'G', 'GS', 'CG', 'ShO', 'SV', 'BS', 'IP', 'H', 'R', 'HR', 'BB', 'IBB', 'HBP', 'BK', 'SO', 'TBF', 'Pitches']]

    PitchingStats = PitchingStats.sort_values('Points', ascending=False)
    PitchingStats = PitchingStats.reset_index(drop=True)

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
    Rankings = pd.merge(bstats, pstats, left_on=['Name_bat', 'Age_bat', 'Team_bat'], right_on=['Name_pit', 'Age_pit', 'Team_pit'], how='outer', suffixes=('_bat', '_pit'))
    Rankings.drop(labels=['Unnamed: 0_bat', 'Unnamed: 0_pit'], axis=1,inplace = True)
    Rankings.Name_bat.fillna(Rankings.Name_pit, inplace=True)
    Rankings = Rankings.fillna(0)
    Total_Points = Rankings['Points_bat'] + Rankings['Points_pit']
    Rankings.insert(1, 'Total_Points', Total_Points)
    Rankings = Rankings.sort_values('Total_Points', ascending=False)
    Rankings = Rankings.reset_index(drop=True)
    Rank = Rankings.index
    Rankings.insert(0, 'Rank', Rank)

    Rankings['Name_bat'] = np.where(Rankings['Name_bat'] == 0, Rankings['Name_pit'], Rankings['Name_bat'])
    Rankings['Season_bat'] = np.where(Rankings['Season_bat'] == 0, Rankings['Season_pit'], Rankings['Season_bat'])
    Rankings['Age_bat'] = np.where(Rankings['Age_bat'] == 0, Rankings['Age_pit'], Rankings['Age_bat'])
    Rankings['Team_bat'] = np.where(Rankings['Team_bat'] == 0, Rankings['Team_pit'], Rankings['Team_bat'])

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
    global currentYear
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
    MarcelProjectionTable = pd.merge(currentYear, previousYear, left_on=['Name_bat_Year1'], right_on=['Name_bat_Year2'], how='outer')
    MarcelProjectionTable = pd.merge(MarcelProjectionTable, TwoYear, left_on=['Name_bat_Year1'], right_on=['Name_bat_Year3'], how='outer')

    # Final Marcel Output
    MarcelProjectionTable.to_csv('data/marcel/MarcelTable.csv', sep=',', index=False, encoding='utf-8')




def marcelCalculations_bat():


    #Import Files
    # last three years of player data
    MarcelTable = pd.read_csv('data/marcel/MarcelTable.csv')
    MarcelTable = MarcelTable.fillna(0)

    # League Averages by Year
    lgAVG = pd.read_csv('data/marcel/lgAVG.csv')
    lgAVG = lgAVG.fillna(0)

    # Stats we need
    BatStatNeeded = ['G', 'AB', 'AVG', 'H', '1B', '2B', '3B', 'HR', 'R', 'RBI', 'BB', 'IBB', 'SO', 'HBP', 'SB', 'CS', 'Pitches']
    BatStatNeeded = [x + '_bat' for x in BatStatNeeded]
    # print(BatStatNeeded)

    # need to add Name, Age, Etc...
    #Create Empty set to use for export
    Result = pd.DataFrame(index=MarcelTable.index, columns=BatStatNeeded )
    Result = Result.fillna(0)
    Result.to_csv('data/marcel/MarcelResultBat.csv')

    # What Year are we using?
    Year1 = MarcelTable['Season_bat_Year1'][1]
    Year2 = MarcelTable['Season_bat_Year2'][1]
    Year3 = MarcelTable['Season_bat_Year3'][1]
    # print("Year Data being Accessed: " + str(Year1) + " , " + str(Year2) + " , " + str(Year3) )

    # finds the index number of each season
    LG_Year1 = lgAVG[lgAVG['Season_bat']==Year1].index.values.astype(int)[0]
    LG_Year2 = lgAVG[lgAVG['Season_bat']==Year2].index.values.astype(int)[0]
    LG_Year3 = lgAVG[lgAVG['Season_bat']==Year3].index.values.astype(int)[0]
    # print("lgAVG Index Number: " + str(LG_Year1) + " , " + str(LG_Year2) + " , " + str(LG_Year3) )

    # Cycle through columns
    for ind in MarcelTable.index:

        for word in BatStatNeeded:
            Mstat = word
            # print ("State being Evaluated: " + str(Mstat) )

            # Label the Stat for each year of Data
            MS_Year1 = (str(Mstat) + "_Year1")
            MS_Year2 = (str(Mstat) + "_Year2")
            MS_Year3 = (str(Mstat) + "_Year3")
            # print ("State Labels: " + str(MS_Year1) + " , " + str(MS_Year2) + " , " + str(MS_Year3) )

            # Weighted total of individual players stat and Plate Apperances
            MStateTotal = (MarcelTable[MS_Year1][ind] * 5) + (MarcelTable[MS_Year2][ind] * 4) + (MarcelTable[MS_Year3][ind] * 3)
            PA = (MarcelTable['PA_bat_Year1'][ind]*.5) + (MarcelTable['PA_bat_Year2'][ind]*.1) + (200)
            # print("Player Weighted Stat: " + str(MStateTotal) + "  Player Weighted Plate Apperances: " + str(PA) )

            # Calculating the Weighted Mean of state per plate apperances for that individual player
            MS_Y1 = lgAVG[Mstat][LG_Year1]/lgAVG['PA_bat'][LG_Year1] * MarcelTable['PA_bat_Year1'][ind] * 5
            MS_Y2 = lgAVG[Mstat][LG_Year2]/lgAVG['PA_bat'][LG_Year2] * MarcelTable['PA_bat_Year2'][ind] * 4
            MS_Y3 = lgAVG[Mstat][LG_Year3]/lgAVG['PA_bat'][LG_Year3] * MarcelTable['PA_bat_Year3'][ind] * 3
            # print("Player State Mean by year: " + str(MS_Y1) + " , " + str(MS_Y2) + " , " + str(MS_Y3) )

            # Players total Weighted Plate Apperances (added +1 to ensure no PA = 0 or NAN values)
            Total_PAS = ( MarcelTable['PA_bat_Year1'][ind] * 5 ) + ( MarcelTable['PA_bat_Year2'][ind] * 4 ) + ( MarcelTable['PA_bat_Year3'][ind] * 3 ) + 1
            # print("Weighted PA: " + str(Total_PAS) )

            # Adjusting ratio to match 1200 apperances
            MS_Ratio = ( (MS_Y1 + MS_Y2 + MS_Y3) * 1200 ) / Total_PAS
            # print("Adjusted Ratio for 1200 PA: " + str(MS_Ratio) )

            # taking league ratio out of 1200 and adding it to the actual players result to get that players ratio of stat per PA
            MS_Perct = ( MS_Ratio + MStateTotal ) / ( 1200 + Total_PAS )
            # print("Adjusting with League Average: " + str(MS_Perct) )

            # Take the player's ratio and multiply it by the expected number of plate apperances
            MS_Expected = ( MS_Perct * PA )
            # print("Player Ratio for # of PA: " + str(MS_Expected) )

            # Adjust for players age
            Age_Reg = ( ( 29 - MarcelTable['Age_bat_Year1'][ind] ) * 0.05 )
            # print("Age Adjustment: " + str(Age_Reg) )

            # Final Result
            Marcel_Result = MS_Expected * ( 1 + Age_Reg )
            # print("Final Player Projection: " + str(Marcel_Result) )

            Result.at[ind, word] = Marcel_Result
            # print(Result.head())

        if MarcelTable['Name_bat_Year1'][ind] is '0':
            Result.at[ind, 'Season'] = MarcelTable['Season_pit_Year1'][ind]
            Result.at[ind, 'Name'] = MarcelTable['Name_pit_Year1'][ind]
            Result.at[ind, 'Team'] = MarcelTable['Team_pit_Year1'][ind]
            Result.at[ind, 'Age'] = MarcelTable['Age_pit_Year1'][ind]
        else:
            Result.at[ind, 'Season'] = MarcelTable['Season_bat_Year1'][ind]
            Result.at[ind, 'Name'] = MarcelTable['Name_bat_Year1'][ind]
            Result.at[ind, 'Team'] = MarcelTable['Team_bat_Year1'][ind]
            Result.at[ind, 'Age'] = MarcelTable['Age_bat_Year1'][ind]

    Result = Result[Result.Name != 0]
    Result.to_csv('data/marcel/MarcelResultBat.csv')
    print("Success")


def marcelCalculations_pit():

    #Import Files
    # last three years of player data
    MarcelTable = pd.read_csv('data/marcel/MarcelTable.csv')
    MarcelTable = MarcelTable.fillna(0)

    # League Averages by Year
    lgAVG = pd.read_csv('data/marcel/lgAVG.csv')
    lgAVG = lgAVG.fillna(0)

    # Stats we need
    PitStatNeeded = ['W', 'L', 'ERA', 'ER', 'WAR', 'G', 'GS', 'CG', 'ShO', 'SV', 'BS', 'IP', 'H', 'R', 'HR', 'BB', 'IBB', 'HBP', 'BK', 'SO', 'Pitches']
    PitStatNeeded = [x + '_pit' for x in PitStatNeeded]
    # print(BatStatNeeded)

    # need to add Name, Age, Etc...
    #Create Empty set to use for export
    Result = pd.DataFrame(index=MarcelTable.index, columns=PitStatNeeded )
    Result = Result.fillna(0)
    Result.to_csv('data/marcel/MarcelResultPit.csv')

    # What Year are we using?
    Year1 = MarcelTable['Season_bat_Year1'][1]
    Year2 = MarcelTable['Season_bat_Year2'][1]
    Year3 = MarcelTable['Season_bat_Year3'][1]
    # print("Year Data being Accessed: " + str(Year1) + " , " + str(Year2) + " , " + str(Year3) )

    # finds the index number of each season
    LG_Year1 = lgAVG[lgAVG['Season_pit']==Year1].index.values.astype(int)[0]
    LG_Year2 = lgAVG[lgAVG['Season_pit']==Year2].index.values.astype(int)[0]
    LG_Year3 = lgAVG[lgAVG['Season_pit']==Year3].index.values.astype(int)[0]
    # print("lgAVG Index Number: " + str(LG_Year1) + " , " + str(LG_Year2) + " , " + str(LG_Year3) )

    # Cycle through columns
    for ind in MarcelTable.index:
        for word in PitStatNeeded:
            Mstat = word
            # print ("State being Evaluated: " + str(Mstat) )

            # Label the Stat for each year of Data
            MS_Year1 = (str(Mstat) + "_Year1")
            MS_Year2 = (str(Mstat) + "_Year2")
            MS_Year3 = (str(Mstat) + "_Year3")
            # print ("State Labels: " + str(MS_Year1) + " , " + str(MS_Year2) + " , " + str(MS_Year3) )

            # Weighted total of individual players stat and Plate Apperances
            MStateTotal = (MarcelTable[MS_Year1][ind] * 5) + (MarcelTable[MS_Year2][ind] * 4) + (MarcelTable[MS_Year3][ind] * 3)
            TBF = (MarcelTable['TBF_pit_Year1'][ind]*.5) + (MarcelTable['TBF_pit_Year2'][ind]*.1) + (200)
            # print("Player Weighted Stat: " + str(MStateTotal) + "  Player Weighted Plate Apperances: " + str(PA) )

            # Calculating the Weighted Mean of state per plate apperances for that individual player
            MS_Y1 = lgAVG[Mstat][LG_Year1]/lgAVG['TBF_pit'][LG_Year1] * MarcelTable['TBF_pit_Year1'][ind] * 5
            MS_Y2 = lgAVG[Mstat][LG_Year2]/lgAVG['TBF_pit'][LG_Year2] * MarcelTable['TBF_pit_Year2'][ind] * 4
            MS_Y3 = lgAVG[Mstat][LG_Year3]/lgAVG['TBF_pit'][LG_Year3] * MarcelTable['TBF_pit_Year3'][ind] * 3
            # print("Player State Mean by year: " + str(MS_Y1) + " , " + str(MS_Y2) + " , " + str(MS_Y3) )

            # Players total Weighted Plate Apperances (added +1 to ensure no PA = 0 or NAN values)
            Total_TBF = ( MarcelTable['TBF_pit_Year1'][ind] * 5 ) + ( MarcelTable['TBF_pit_Year2'][ind] * 4 ) + ( MarcelTable['TBF_pit_Year3'][ind] * 3 ) + 1
            # print("Weighted PA: " + str(Total_PAS) )

            # Adjusting ratio to match 1200 apperances
            MS_Ratio = ( (MS_Y1 + MS_Y2 + MS_Y3) * 1200 ) / Total_TBF
            # print("Adjusted Ratio for 1200 PA: " + str(MS_Ratio) )

            # taking league ratio out of 1200 and adding it to the actual players result to get that players ratio of stat per PA
            MS_Perct = ( MS_Ratio + MStateTotal ) / ( 1200 + Total_TBF )
            # print("Adjusting with League Average: " + str(MS_Perct) )

            # Take the player's ratio and multiply it by the expected number of plate apperances
            MS_Expected = ( MS_Perct * TBF )
            # print("Player Ratio for # of PA: " + str(MS_Expected) )

            # Adjust for players age
            Age_Reg = ( ( 29 - MarcelTable['Age_pit_Year1'][ind] ) * 0.05 )
            # print("Age Adjustment: " + str(Age_Reg) )

            # Final Result
            Marcel_Result = MS_Expected * ( 1 + Age_Reg )
            # print("Final Player Projection: " + str(Marcel_Result) )

            Result.at[ind, word] = Marcel_Result
            # print(Result.head())

        if MarcelTable['Name_bat_Year1'][ind] is '0':
            Result.at[ind, 'Season'] = MarcelTable['Season_pit_Year1'][ind]
            Result.at[ind, 'Name'] = MarcelTable['Name_pit_Year1'][ind]
            Result.at[ind, 'Team'] = MarcelTable['Team_pit_Year1'][ind]
            Result.at[ind, 'Age'] = MarcelTable['Age_pit_Year1'][ind]
        else:
            Result.at[ind, 'Season'] = MarcelTable['Season_bat_Year1'][ind]
            Result.at[ind, 'Name'] = MarcelTable['Name_bat_Year1'][ind]
            Result.at[ind, 'Team'] = MarcelTable['Team_bat_Year1'][ind]
            Result.at[ind, 'Age'] = MarcelTable['Age_bat_Year1'][ind]


    Result = Result[Result.Name != 0]
    Result.to_csv('data/marcel/MarcelResultPit.csv')
    print("Success")



def MarcelPoints():
    global currentYear

    pointAmountsBat()
    data = pd.read_csv('data/marcel/MarcelResultBat.csv')

    points = ( ( R * data['R_bat'] )
    + ( Single * data['1B_bat'] )
    + ( Double * data['2B_bat'] )
    + ( Triple * data['3B_bat'] )
    + ( HR * data['HR_bat'] )
    + ( TB * ( data['1B_bat'] + (2 * data['2B_bat']) + (3 * data['3B_bat']) + (4 * data['HR_bat']) ) )
    + ( RBI * data['RBI_bat'] )
    + ( BB * data['BB_bat'] )
    + ( K * data['SO_bat'] )
    + ( SB * data['SB_bat'] )
    + ( AB * data['AB_bat'] )
    + ( Hits * data['H_bat'])
    + ( XBH * ( data['2B_bat'] + data['3B_bat'] + data['HR_bat']) )
    + ( IBB * data['IBB_bat'] )
    + ( HBP * data['HBP_bat'] )
    + ( CS * data['CS_bat'] ) )


    # missing Sac and GWRBI and everything past CS

    data['Points_bat'] = points
    data['Season'] = currentYear + 1

    data.drop(labels=['Unnamed: 0'], axis=1, inplace = True)
    data = data.sort_values('Points_bat', ascending=False)
    data = data.reset_index(drop=True)
    Rank = data.index
    data.insert(0, 'Bat_Rank', Rank)
    data.to_csv('data/marcel/MarcelResultBat.csv')

    pdata = pd.read_csv('data/marcel/MarcelResultPit.csv')

    pointAmountsPit()

    ppoints = ( ( IP * pdata['IP_pit'] )
    + ( ER * pdata['ER_pit'] )
    + ( K * pdata['SO_pit'] )
    + ( SO * pdata['ShO_pit'] )
    + ( W * pdata['W_pit'] )
    + ( L * pdata['L_pit'] )
    + ( SV * pdata['SV_pit'] )
    + ( BS * pdata['BS_pit'] )
    + ( G * pdata['G_pit'] )
    + ( GS * pdata['GS_pit'] )
    + ( BS * pdata['BS_pit'] )
    + ( H * pdata['H_pit'] )
    + ( RA * pdata['R_pit'] )
    + ( HR * pdata['HR_pit'] )
    + ( BB * pdata['BB_pit'] )
    + ( HB * pdata['HBP_pit'] )
    + ( IBB * pdata['IBB_pit'] )
    + ( B * pdata['BK_pit'] )
    #+ ( PKO * pdata['PKO'] )
    + ( QS * pdata['BK_pit'] )
    + ( CG * pdata['CG_pit'] )
    #+ ( NH * pdata['NH'] )
    #+ ( PG * pdata['PG'] )
    #+ ( BF * pdata['BF'] )
    + ( PC * pdata['Pitches_pit'] )
    #+ ( SOP * pdata['SOP'] )
    #+ ( HD * pdata['HD'] )
    )

    pdata['Points_pit'] = ppoints
    pdata['Season'] = currentYear + 1
    pdata.drop(labels=['Unnamed: 0'], axis=1, inplace = True)
    pdata = pdata.sort_values('Points_pit', ascending=False)
    pdata = pdata.reset_index(drop=True)
    Rank = pdata.index
    pdata.insert(0, 'Pit_Rank', Rank)
    pdata.to_csv('data/marcel/MarcelResultPit.csv')



def marcelCalculations():
    global currentYear

    marcelCombinedFile()
    marcelCalculations_bat()
    marcelCalculations_pit()
    MarcelPoints()

    bstats = pd.read_csv('data/marcel/MarcelResultBat.csv')
    pstats = pd.read_csv('data/marcel/MarcelResultPit.csv')

    bstats.drop(labels=['Unnamed: 0'], axis=1, inplace = True)
    pstats.drop(labels=['Unnamed: 0'], axis=1, inplace = True)

    #Combine CSV
    Rankings = pd.merge(bstats, pstats, on=['Name'], how='inner', suffixes=('_bat', '_pit'))

    #Rankings.drop(labels=['Unnamed: 0_bat', 'Unnamed: 0_pit'], axis=1, inplace = True)
    # Rankings.Name_bat.fillna(Rankings.Name_pit, inplace=True)
    Rankings = Rankings.fillna(0)
    Total_Points = Rankings['Points_bat'] + Rankings['Points_pit']
    Rankings.insert(0, 'Total_Points', Total_Points)
    Rankings = Rankings.sort_values('Total_Points', ascending=False)
    Rankings = Rankings.reset_index(drop=True)
    Rank = Rankings.index
    Rankings.insert(0, 'Rank', Rank)
    # print(Rankings.describe())
    Teams = np.where(Rankings['Team_bat'] == 0, Rankings['Team_pit'], Rankings['Team_bat'])
    Age = np.where(Rankings['Age_bat'] == 0, Rankings['Age_pit'], Rankings['Age_bat'])

    Season = (currentYear + 1)
    Name = Rankings['Name']
    #Teams = Rankings['Team_bat'] + Rankings['Team_pit']
    Rankings.drop(labels=['Name', 'Age_bat', 'Age_pit', 'Team_bat', 'Team_pit', 'Season_bat', 'Season_pit'], axis=1, inplace = True)

    Rankings.insert(2, 'Name', Name)
    Rankings.insert(3, 'Age', Age)
    Rankings.insert(4, 'Season', Season)
    Rankings.insert(5, 'Team', Teams)


    Rankings.to_csv('data/marcel/MarcelResultTotal.csv', sep=',', index=False, encoding='utf-8')




################################

#### Cycle Through Each Year ###

################################

# runs points on a range of years and creates a csv for that year
# Each Year is Tabulated and saved to its own csv file
# each year also runs a lgAVG and that data is stored


def PointCycle():
    global currentYear

    yearRange = list(range(2000, currentYear + 1))
    # print(yearRange)
    for x in yearRange:
        # print(X)
        points(x)
        combinePoints()
        R = pd.read_csv('data/Rankings.csv')
        filename = "data/YearPoints/%s.csv" % x
        R.to_csv(filename, sep=',', index=False, encoding='utf-8')
        lgAVG()
        print(str(x) + ": Successful")









#####################

#### Run Programs ###

#####################


# Creates files for batting and pitching
# points(2019)

# Combines batting and pitching files together
# combinePoints()

# Run Marcel Projections Table to later create projections
# marcelCombinedFile()

## Creating a Lg Total document for Marcel Projections
# lgAVG()


# Run Marcel Projections
marcelCalculations()

# Run Point Cycle
# PointCycle()
