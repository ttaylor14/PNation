# File Management Repository

# last Update : 8.27.19



import pandas as pd

#######################

#### Pull to Roster ###

#######################

# Combine individual csv team files into the roster file


def combine_Teams_to_Roster():

    full_roster = []
    # at the end export each team to own file in teams Folder
    team_1 = pd.read_csv('teams/team1_Draft.csv', encoding='utf-8')
    team_2 = pd.read_csv('teams/team2_Draft.csv', encoding='utf-8')
    team_3 = pd.read_csv('teams/team3_Draft.csv', encoding='utf-8')
    team_4 = pd.read_csv('teams/team4_Draft.csv', encoding='utf-8')
    team_5 = pd.read_csv('teams/team5_Draft.csv', encoding='utf-8')
    team_6 = pd.read_csv('teams/team6_Draft.csv', encoding='utf-8')
    team_7 = pd.read_csv('teams/team7_Draft.csv', encoding='utf-8')
    team_8 = pd.read_csv('teams/team8_Draft.csv', encoding='utf-8')
    team_9 = pd.read_csv('teams/team9_Draft.csv', encoding='utf-8')
    team_10 = pd.read_csv('teams/team10_Draft.csv', encoding='utf-8')
    team_11 = pd.read_csv('teams/team11_Draft.csv', encoding='utf-8')
    team_12 = pd.read_csv('teams/team12_Draft.csv', encoding='utf-8')
    team_13 = pd.read_csv('teams/team13_Draft.csv', encoding='utf-8')
    team_14 = pd.read_csv('teams/team14_Draft.csv', encoding='utf-8')

    header = ["team_id", "roster_id", "player_Fname", "player_Lname", "salary", "player_id"]

    full_roster = pd.concat([team_1, team_2, team_3, team_4, team_5,
                             team_6, team_7, team_8, team_9, team_10,
                             team_11, team_12, team_13, team_14], ignore_index=True, axis=0)

    full_roster.to_csv('data/rosters.csv', index=False)

    # Print Success when complete
    print("Success")


############################

#### Roster to Team Files###

############################

def Rosters_To_Team_Files():

    full_roster = pd.read_csv('data/rosters.csv')

    # This seperates full_roster into each team

    # create each team roster as an object
    team_1 = full_roster[full_roster['team_id'] == 1]
    team_2 = full_roster[full_roster['team_id'] == 2]
    team_3 = full_roster[full_roster['team_id'] == 3]
    team_4 = full_roster[full_roster['team_id'] == 4]
    team_5 = full_roster[full_roster['team_id'] == 5]
    team_6 = full_roster[full_roster['team_id'] == 6]
    team_7 = full_roster[full_roster['team_id'] == 7]
    team_8 = full_roster[full_roster['team_id'] == 8]
    team_9 = full_roster[full_roster['team_id'] == 9]
    team_10 = full_roster[full_roster['team_id'] == 10]
    team_11 = full_roster[full_roster['team_id'] == 11]
    team_12 = full_roster[full_roster['team_id'] == 12]
    team_13 = full_roster[full_roster['team_id'] == 13]
    team_14 = full_roster[full_roster['team_id'] == 14]

    # Export Each Roster into own CSV File
    header = ["team_id", "player_Fname", "player_Lname", "salary", "player_id"]

    team_1.to_csv('teams/team1_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_2.to_csv('teams/team2_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_3.to_csv('teams/team3_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_4.to_csv('teams/team4_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_5.to_csv('teams/team5_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_6.to_csv('teams/team6_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_7.to_csv('teams/team7_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_8.to_csv('teams/team8_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_9.to_csv('teams/team9_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_10.to_csv('teams/team10_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_11.to_csv('teams/team11_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_12.to_csv('teams/team12_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_13.to_csv('teams/team13_Draft.csv', encoding='utf-8', columns=header, index=False)
    team_14.to_csv('teams/team14_Draft.csv', encoding='utf-8', columns=header, index=False)

    # Print Success when complete
    print("Success")

#######################################

#### Add Lahman Tag to Toster Names ###

########################################

# Goal is to find lahman tag for each rostered player
# if tag already exists skip
# if not found leave blank


def Roster_lahman_tag():
    roster = pd.read_csv('data/rosters.csv')
    lahman = pd.read_csv('data/baseballdatabank-2019.2/core/People.csv')

    print(roster.head())
    # print(lahman.head())

####### replace the current_year with a global variable fromt he master file? or pull the date from the clock?

    current_year = 2019             # current year
    too_old = 50                    # oldest a player could be and play
    max_birth_year = current_year - too_old

    # Filters out all player who have died and limits search to players who are not too_old
    lahman = lahman[lahman.birthYear >= max_birth_year]
    lahman = lahman[lahman.deathYear.isnull()]

    # print(lahman.head())
    # print(lahman.describe())

    # searches lahman database for matches

    for ind in roster.index:

        Fname = roster['player_Fname'][ind]
        Lname = roster['player_Lname'][ind]

        match = lahman[(lahman.nameFirst == Fname) & (lahman.nameLast == Lname)].head(1)

        # print(match)

        pID = match['playerID'].values
        rID = match['retroID'].values
        bbID = match['bbrefID'].values

        # print(pID, rID, bbID)

        roster.at[ind, 'lahmanID'] == pID
        # roster.at[ind, 'retroID'] == rID

        # roster.loc[ind]['lahmanID'] = pID
        # roster.ix[ind]['retroID'] = rID
        # roster.ix[ind]['bbrefID'] = bbID


    print(roster.head())


# Pull Team csv files to roster.csv
# combine_Teams_to_Roster()

# Push roster.csv rosters to individual files
# Rosters_To_Team_Files()



# Pulls Lahman Tags (playerID) for rosters (and: retroID   bbrefID)
Roster_lahman_tag()
