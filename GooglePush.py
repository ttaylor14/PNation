# GooglePush.py

# last Update : 9.27.19

# Goal is to push csv File information to Google Sheet

##### To DO
## finish update cell code
#### Test and Verify success


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
List_of_Tabs = sheet.worksheets()

# Opens Master Info Tab
masterInfo = sheet.worksheet("Master Info")

# intialise data of lists.
TeamPositions = {'TeamNumber':['Team1', 'Team2', 'Team3', 'Team4', 'Team5', 'Team6', 'Team7', 'Team8', 'Team9', 'Team10', 'Team11', 'Team12', 'Team13', 'Team14'], 'TeamPosition':[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]}
TeamPositions = pd.DataFrame(TeamPositions)

# print(TeamPositions)

# Read team_info csv file
teamCSV = pd.read_csv('data/team_info.csv')



########## Update Master Info Tab from team_info csv

# Update Master Info Page
GGteamName = masterInfo.range('A13:E26')
CSVteamName = teamCSV['team_id']

#### Still needs work....

# Create Loop to update GoogleSheet
for i, val in enumerate(CSVteamName):  #gives us a tuple of an index and value
    GGteamName[i].value = val    #use the index on cell_list and the val from cell_values

masterInfo.update_cells(cell_list)


#########################

###### Update each teams roster in Google Sheet from Each Teams csv file
##### Needs work

# Loop through each Team Sheet to push data to team page
for teamNumber in TeamPositions['TeamNumber']:
    # print(teamnumber)

    # Find Team Information form Master File based on Team Position
    id = TeamPositions.loc[TeamPositions['TeamNumber'] == teamNumber, 'TeamPosition'].iloc[0]
    # print(id)

    # Pulls Information for Master Info
    teamName = masterInfo.acell(Info).value

    # Finds Team Tab
    teampage = sheet.worksheet(teamName)

    # Update Team Roster Info
    # Use that teams csv file....



print('Success')


