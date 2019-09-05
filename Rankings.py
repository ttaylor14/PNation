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

    BattingStats = data[['Season', 'Name', 'Team', 'Age', 'Points', 'G', 'PA', 'AB', 'AVG', 'H', '1B', '2B', '3B', 'HR', 'R', 'RBI', 'BB', 'IBB', 'SO', 'HBP', 'SB', 'CS', 'HBP', 'SO', 'Pitches']]
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

    #Combine CSV
    Rankings = pd.merge(bstats, pstats, left_on=['Name', 'Points', 'Season', 'Age', 'Team'], right_on=['Name', 'Points', 'Season', 'Age', 'Team'], how='outer', suffixes=('_bat', '_pit'))
    Rankings = Rankings.sort_values('Points', ascending=False)
    Rankings = Rankings.reset_index(drop=True)
    Rank = Rankings.index
    Rankings.insert(0, 'Rank', Rank)
    Rankings.drop(labels=['Unnamed: 0_bat', 'Unnamed: 0_pit'], axis=1,inplace = True)

    Rankings.to_csv('data/Rankings.csv', sep=',', index=False, encoding='utf-8')


####################################

#### Creating Marcel Projections ###

####################################

# runs points on current and past 2 season
# merges all files into one document
# ranks by projection for the upcoming year

def marcelCalculations():

    MarcelProjection = pd.read_csv('data/marcel/MarcelProjection.csv')





def marcelRankings():

    # Current or Season before Projection
    currentYear = 2019
    previousYear = (currentYear - 1)
    TwoYear = (currentYear - 2)

    points(currentYear)
    combinePoints()
    currentYear = pd.read_csv('data/Rankings.csv')
    currentYear = currentYear.add_suffix('_Year1')
    currentYear.to_csv('data/marcel/currentYear.csv', sep=',', index=False, encoding='utf-8')



    # Previous Seasons stats

    points(previousYear)
    combinePoints()
    previousYear = pd.read_csv('data/Rankings.csv')
    previousYear = previousYear.add_suffix('_Year2')
    previousYear.to_csv('data/marcel/previousYear.csv', sep=',', index=False, encoding='utf-8')


    # Two Seasons ago stats

    points(TwoYear)
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
    MarcelProjectionTable.to_csv('data/marcel/MarcelProjection.csv', sep=',', index=False, encoding='utf-8')









#####################

#### Run Programs ###

#####################


# Creates files for batting and pitching
#points(2019)


# Combines batting an dpitching files together
#combinePoints()

# Run Marcel Projections
marcelRankings()


