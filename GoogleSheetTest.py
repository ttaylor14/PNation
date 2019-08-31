# Googlesheet File management

# last Update : 8.27.19

# See: http://www.indjango.com/access-google-sheets-in-python-using-gspread/

# Goal is to pull google sheet information and place them in the appropriate csv file.
# Later a sperate file will be created to run this process backwards to replace the relevent information back onto the excell sheet1)


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('pnation-6409ef8b6f8a.json', scope)
client = gspread.authorize(creds)

sheet = client.open("2019 Procrastination Fantasy Baseball").sheet1

pp = pprint.PrettyPrinter()

# sheet.update_cell(1, 1, "2019 Procrastination Fantasy Baseball")
#row = ["I'm","inserting","a","new","row","into","a,","Spreadsheet","using","Python"]
#index = 3
#sheet.insert_row(row, index)

result = sheet.get_all_records()
#result = sheet.row_values(2)

pp.pprint(result)
