# GooglePull.py

# last Update : 9.29.19


# Goal is to pull google sheet information and place them in the appropriate csv file.



import gspread
import pandas as pd

from oauth2client.service_account import ServiceAccountCredentials
import pprint

#Google API Credentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('pnation-6409ef8b6f8a.json', scope)
client = gspread.authorize(creds)

pp = pprint.PrettyPrinter()

# Opens Google File
sheet = client.open("2019 Procrastination Fantasy Baseball")

#Pulls List of Tabs
# List_of_Tabs = sheet.worksheets()

# Opens Master Info Tab
masterInfo = sheet.worksheet("Master Info")

# intialise data of lists.
TeamPositions = {'TeamNumber':['Team1', 'Team2', 'Team3', 'Team4', 'Team5', 'Team6', 'Team7', 'Team8', 'Team9', 'Team10', 'Team11', 'Team12', 'Team13', 'Team14'], 'TeamPosition':[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]}
TeamPositions = pd.DataFrame(TeamPositions)

# print(TeamPositions)

TeamMaster = pd.read_csv('data/team_info.csv')
# print(TeamMaster)



masterInfo = masterInfo.get_all_values()

# Adds headers and pushes data into a Pandas DF
headers = masterInfo.pop(11)
masterInfo = pd.DataFrame(masterInfo, columns=headers)

# Data Cleaning to only needed information
masterInfo = masterInfo.iloc[11:25, 0:6]
masterInfo['FAAB'] = masterInfo['FAAB'].str.split('$').str[1]
# print(masterInfo)


# Loop through each Team Sheet to pull data
for teamNumber in TeamPositions['TeamNumber']:
    # print(teamnumber)

    # Find Team Information form Master File based on Team Position
    id = TeamPositions.loc[TeamPositions['TeamNumber'] == teamNumber, 'TeamPosition'].iloc[0]

    # print(id)

    # Pulls Information for Master Info
    teamName = masterInfo['Team Name'].at[id]
    teamAcronym = masterInfo['Acronym'].at[id]
    teamFaab = masterInfo['FAAB'].at[id]
    teamOwner = masterInfo['Owner'].at[id]
    teamEmail = masterInfo['Email'].at[id]
    teamRank = masterInfo['Ranking'].at[id]

    #Find Team ID
    TeamID = TeamPositions.index[TeamPositions['TeamNumber'] == teamNumber].values.astype(int)[0] + 1
    # print(TeamID)

    # Finds Team Tab
    teampage = sheet.worksheet(teamName)

    # Pulls all data from Google Sheet
    data = teampage.get_all_values()

    # Adds headers and pushes data into a Pandas DF
    headers = data.pop(2)
    df = pd.DataFrame(data, columns=headers)

    # Data Cleaning to only needed information
    Team = df.iloc[3:36, 0:5]
    Team['Player'] = Team['Player'].str.split('\n').str[0]
    Team['Player Salary'] = Team['Player Salary'].str.split('$').str[1]


    # Add team_id to roster csv
    Team.insert(0, 'team_id', TeamID)

    # print(Team.head())

    # Save DF as file for each team
    filename = "data/Teams/%s.csv" % teamNumber
    Team.to_csv(filename, sep=',', index=False, encoding='utf-8')


team_id = masterInfo.reset_index().index + 1
masterInfo.insert(loc=0, column='team_id', value=team_id)

# Saves Team Info File
masterInfo.to_csv('data/Teams/team_info.csv', sep=',', index=False, encoding='utf-8')


print('Success')


