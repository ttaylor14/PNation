# Master.py

import GooglePull

from FileManagementTeams import combine_Teams_to_Roster, Rosters_To_Team_Files, Roster_lahman_tag

import GooglePush

from Rankings import PointCycle, points

from DraftCalculatorUpdate import draft_prep



###### Draft Calculator #######
# Pull data from Google, run Draft Calculations, return data to Google

def Draft():
    # Step 1: Pull Google Data
    GooglePull()

    # Step 2: Condense Rosters to FullRoster.csv File
    combine_Teams_to_Roster()

    # Step 3: Run Draft Calculator to process Draft Calculations
    draft_prep()

    # Step 4: Update Google Sheet with Updated
    GooglePush()



###### Team Analysis #######
# Pull Data from Google and run Team Analysis

def teamAnalysis():
    # Step 1: Pull Google Data
    GooglePull()

    # Step 2: Condense Rosters to FullRoster.csv File
    combine_Teams_to_Roster()

    # Step 3:

    # Step 4:


###### Point Cycle #######
# Create Files for each Season and add League Totals

def pointCycle():
    # Step 1: Pull Google Data
    PointCycle()

###### Current Point Rankings #######
# Create Current Year's Point Rankings

def pointRank():
    # Step 1: Run Points (change to current year)
    points(2019)

