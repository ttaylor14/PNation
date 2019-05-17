# File Management


import pandas as pd


# Combine individual csv team files into the roster file


def combine_Teams_to_Roster():

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

    full_roster = pd.concat([team_1, team_2, team_3, team_4, team_5,
                             team_6, team_7, team_8, team_9, team_10, team_11, team_12, team_13, team_14])

    full_roster.to_csv('data/rosters.csv')


def Rosters_To_Team_Files():

    # Temporary Team Place Holder

    full_roster = pd.read_csv('data/rosters.csv')

    # This should be a seperate function that takes the full_roster and divides it out one the for loop is complete.

    # create each team
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

# at the end export each team to own file in teams Folder
    team_1.to_csv('teams/team1_Draft.csv', encoding='utf-8')
    team_2.to_csv('teams/team2_Draft.csv', encoding='utf-8')
    team_3.to_csv('teams/team3_Draft.csv', encoding='utf-8')
    team_4.to_csv('teams/team4_Draft.csv', encoding='utf-8')
    team_5.to_csv('teams/team5_Draft.csv', encoding='utf-8')
    team_6.to_csv('teams/team6_Draft.csv', encoding='utf-8')
    team_7.to_csv('teams/team7_Draft.csv', encoding='utf-8')
    team_8.to_csv('teams/team8_Draft.csv', encoding='utf-8')
    team_9.to_csv('teams/team9_Draft.csv', encoding='utf-8')
    team_10.to_csv('teams/team10_Draft.csv', encoding='utf-8')
    team_11.to_csv('teams/team11_Draft.csv', encoding='utf-8')
    team_12.to_csv('teams/team12_Draft.csv', encoding='utf-8')
    team_13.to_csv('teams/team13_Draft.csv', encoding='utf-8')
    team_14.to_csv('teams/team14_Draft.csv', encoding='utf-8')
