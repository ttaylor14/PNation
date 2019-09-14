# Googlesheet File management

# last Update : 9.1.19

# See: http://www.indjango.com/access-google-sheets-in-python-using-gspread/

# Goal is to pull google sheet information and place them in the appropriate csv file.
# Later a sperate file will be created to run this process backwards to replace the relevent information back onto the excell sheet1)


### To DO
# Pull this data and place in csv files?
# create a loop that will repeat the team1 code with all teams
# create second file that replaces values backwards from csv file (test after hard copy made)



import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

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

# Pulls Information for Team 1 Master Info
team1 = masterInfo.acell('A13').value
team1Acronym = masterInfo.acell('A13').value
team1Faab = masterInfo.acell('A13').value
team1Owner = masterInfo.acell('A13').value

# Finds Team 1 Tab
team1page = sheet.worksheet(team1)
# team1page = team1page.get_all_records()
team1playerList = team1page.range('C5:E36')

print( type(team1playerList) )



'''
for ind in team1playerList:
    text = team1playerList[ind]
    head, sep, tail = text.partition('/n')
    print(head)
'''


pp.pprint(team1playerList)

# Remove all contents after player name



# sheet.update_cell(1, 1, "2019 Procrastination Fantasy Baseball")
#row = ["I'm","inserting","a","new","row","into","a,","Spreadsheet","using","Python"]
#index = 3
#sheet.insert_row(row, index)

#result = worksheet1.get_all_records()
#result = sheet.row_values(2)

