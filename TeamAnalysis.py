# Team Analysis

# last Update : 9.29.19


import pandas as pd
import numpy as np

################################

### Data import and Cleaning ###

################################



# Pull Full Rosters
roster = pd.read_csv('data/FullRoster.csv')
# print(roster.head())

# Deletd row with no name and are not begin kept
roster['Player'].replace('', np.nan, inplace=True)
roster['Player Salary'].replace('', np.nan, inplace=True)
roster.dropna(subset=['Player'], inplace=True)
roster.dropna(subset=['Player Salary'], inplace=True)



##################################

### Create Current Year Rankings ###

##################################

# Pull Projection
Rankings = pd.read_csv('data/Rankings.csv')
# print(marcel.head())

# merge csv together
TeamStats_current = pd.merge(roster, Rankings, left_on=['Player'], right_on=['Name_bat'], how='inner')
# print(TeamStats.head())

# Clean Data
TeamStats_current.drop(labels=['Trade Block'], axis=1,inplace = True)
TeamStats_current = TeamStats_current[['team_id', 'Player', 'Player Salary', 'Age_bat', 'Team_bat', 'Positions', 'Total_Points']]
# print(TeamStats.head())

TeamStats_current.to_csv('data/TeamAnalysis/TeamPoints_Current.csv', sep=',', index=False, encoding='utf-8')



######################################

### create Team Rosters by team_id ###

######################################



AllTeams = list(range(1,  15) )
Rankings = []

for x in AllTeams:
    total = TeamStats_current[TeamStats_current['team_id'].notnull() & TeamStats_current['Player'].notnull() & (TeamStats_current['team_id'] == x)].sum()

    NumPlayers = len(TeamStats_current[TeamStats_current['team_id'].notnull() & TeamStats_current['Player'].notnull() & (TeamStats_current['team_id'] == x)])

    Team = "Team%s" % x

    Rankings.append((x, Team, total['Total_Points'], total['Player Salary'], NumPlayers))

headers = ['team_id', 'Team_Name', 'Total_Points', 'Total_Salary', 'Number_Players']
Rankings = pd.DataFrame(Rankings, columns=headers)

Rankings['Avg_Salary'] = Rankings['Total_Salary']/Rankings['Number_Players']
Rankings['Avg_Player_Score'] = Rankings['Total_Points']/Rankings['Number_Players']

# Pull Team Names
team_info = pd.read_csv('data/Teams/Team_info.csv')
team_info = team_info[['team_id', 'Team Name']]
#print(team_info.head())

#merge csv together
Rankings = pd.merge(team_info, Rankings, left_on=['team_id'], right_on=['team_id'], how='inner')
# print(TeamStats.head())




Rankings = Rankings.sort_values('Total_Points', ascending=False)
Rankings = Rankings.reset_index(drop=True)
Rank = Rankings.index
Rankings.insert(0, 'Rank', Rank)


# print(projection)

Rankings.to_csv('data/TeamAnalysis/CurrentRankings.csv', sep=',', index=False, encoding='utf-8')


print("Success")







##################################

### Create Projection Rankings ###

##################################

# Pull Projection
marcel = pd.read_csv('data/marcel/MarcelResultTotal.csv')
# print(marcel.head())

# merge csv together
TeamStats = pd.merge(roster, marcel, left_on=['Player'], right_on=['Name'], how='inner')
# print(TeamStats.head())

# Clean Data
TeamStats.drop(labels=['Trade Block'], axis=1,inplace = True)
TeamStats = TeamStats[['team_id', 'Player', 'Player Salary', 'Age', 'Team', 'Positions', 'Total_Points']]
# print(TeamStats.head())

TeamStats.to_csv('data/TeamAnalysis/TeamPoints_Proj.csv', sep=',', index=False, encoding='utf-8')



######################################

### create Team Rosters by team_id ###

######################################



AllTeams = list(range(1,  15) )
projection = []

for x in AllTeams:
    total = TeamStats[TeamStats['team_id'].notnull() & TeamStats['Player'].notnull() & (TeamStats['team_id'] == x)].sum()

    NumPlayers = len(TeamStats[TeamStats['team_id'].notnull() & TeamStats['Player'].notnull() & (TeamStats['team_id'] == x)])

    Team = "Team%s" % x

    projection.append((x, Team, total['Total_Points'], total['Player Salary'], NumPlayers))

headers = ['team_id', 'Team_Name', 'Total_Points', 'Total_Salary', 'Number_Players']
projection = pd.DataFrame(projection, columns=headers)

projection['Avg_Salary'] = projection['Total_Salary']/projection['Number_Players']
projection['Avg_Player_Score'] = projection['Total_Points']/projection['Number_Players']

# Pull Team Names
team_info = pd.read_csv('data/Teams/Team_info.csv')
team_info = team_info[['team_id', 'Team Name']]
#print(team_info.head())

#merge csv together
projection = pd.merge(team_info, projection, left_on=['team_id'], right_on=['team_id'], how='inner')
# print(TeamStats.head())




projection = projection.sort_values('Total_Points', ascending=False)
projection = projection.reset_index(drop=True)
Rank = projection.index
projection.insert(0, 'Rank', Rank)


# print(projection)

projection.to_csv('data/TeamAnalysis/ProjectionRankings.csv', sep=',', index=False, encoding='utf-8')


print("Success")
