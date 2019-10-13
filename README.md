# PNation
Procrastination Fantasy Baseball


The following project was created with the sole intent
in creating a Editable Fantasy baseball Ranking System specific to league setting. The settings currently being utilize follow that of a customized ESPN league:

http://fantasy.espn.com/baseball/league?leagueId=25593

The system also incorporates a financial aspect to help accomodate/evaluate/calculate auction player values, dynasty team budgets, and player/team cost analysis. This system's aim is to enhance or replace the following system located on a Google Sheet here:

https://docs.google.com/spreadsheets/d/1Z08eDxf6zWTdcBjk0MuLqNrRBqT6nPLhd_In45e8W0I/edit?usp=sharing


Player Stats are gathered using the Python pybaseball package found here: 
https://github.com/jldbc/pybaseball

Adjustments could be made to use the Lahman Database (also accessed using the pybaseball package). Lahman Database, however, does not include the current year's statistics and is not updated until a few months after the season. To ensure the system utilizes the most up to date information I designed it around the pybaseball package. 

Lahman Database can be found here:

http://www.seanlahman.com/baseball-archive/statistics/





### * Issues found in the pybaseball package: *
* Many of these stats are included in Lahman Database which could be utilized for data prior to the current year 

- [ ] Stats do not include Quality Stats (QS)
- [ ] Stats do not include No Hitters (NH)
- [ ] Stats do not include Perfect Games (PG)
- [ ] Stats do not include Hitting for the Cycle (CYC)
- [ ] Stats do not include Errors (E)
- [ ] Stats do not include all Fielding Stats (Put Outs, Assists, Double PLays....)
- [ ] Does not include Games played by position
- [ ] Also the lack of a player code can make merging data slightly more difficult (looking at utilizing Lahman Player ID incorporation)



## Contributing
Pull requests are welcome. For changes, please open an issue first to discuss what you would like to change or add.

## License
[MIT](https://choosealicense.com/licenses/mit/)








# PYTHON FILES

Currently all Python Files are located the PNation Directory. Eventually all files should be moved to a python folder for ease of readability. All files are writted and executed using Sublime Text.



## -- Understanding the Master File --
The Master File's aim is to create a one stop shop for running and accessing all functions for data flow and task completions.
This file will be utilized to complete complex tasks such as League Draft processing.
Eventually the hope is to incorporate this system into a Visual User Interfafce, possibly using: tkinter?

### * Draft() *
In preperation for a draft this functions aim is to complete the calculations for draft preperations.

Step 1: Pull Current Data from the Google Sheet
Step 2: Run Draft Calculator to adjust team FAAB, Draft Budgets, and Player Salaries in accordance with league settings
Step 3: Update all Team CSV FIles
Step 4: Push current player Salaries and Team Faab to Google Sheet
Step 5: Run Team Analysis on adjusted teams?

Step 6: Final step must be completed manually:
   - Adjust new Salaries in League Site (ESPN) prior to draft with update player values


### * teamAnalysis() *
Runs a set of Analysis functions on current team rosters (Both current year stats and future projected stats)


### * pointCycle() *
Runs Point cycle function to create CSV files with league and player stats for each year since 2000.
Fills in lgAvg CSV file and create CSV for each year for further evaluation.

### * pointRank() *
Runs current point totals for a specific year (most likely the current season)



### * Additions needed *

- [ ] User Interface?
- [ ] Temp. Player Salary Calculations?
- [ ] League charts/stats for creating sharable information for league progress or projections...



## -- Understanding the Draft Calculator File --

The Procrastination League utilizes a very specific calculation to determine player salaries.

I created and the league currently uses a Google Sheet to calculate team salaries, draft budgets, etc...
for reference you can view the sheet here:
https://docs.google.com/spreadsheets/d/1Z08eDxf6zWTdcBjk0MuLqNrRBqT6nPLhd_In45e8W0I/edit?usp=sharing

The league began in 2016. It was a auction system draft and each team recieved $400 for the draft.
   - Teams are made up of 25 roster spots and 5 il spots.

Teams can keep up to 25 players going into the following year's draft. The salaries from the previous year's draft
are used when calculating the upcoming year's team budget.

Cash remining after the draft is rolled into the teams faab account. This money is used for wavier wire pick ups, trades,
or, as we will discuss, player salary roll downs.

### * Salary Roll Down *

Before the draft remaining faab is used to evenly pay down player salaries (of keepers). If you had $15 remining of faab, the
first 15 players, over $1, on your roster would subtract $1 from each of their salaries. If a player's salary is already at $1
then that players salary is skipped and applied to the following player. (No player may have less than a $1 salary)

If, in the example provided above, you only kept 10 players then all 10 would lose $1 and then the first five would lose another $1.
So the first 5 players would decrease by $2 and the last 5 would decrease by only $1. If money remains it rolls over to the Keeper costs.

### * Keeper Costs *

After the faab is applied then the keeper cost is applied to the player's salary. To keep a player, their salary will increase by $5
(after the faab is applied). If any faab remains player's salaries could be rolled down with any remaining faab until player's
salaries reach $1. If any faab is left it is applied to the team's draft budget.

### * Draft Budget *

Once the team's salary is finalized the teams cost is subtracted from the yearly draft budget (which has now decreased to $300 a year).
Teams draft any remaining players with any remaining cash (teams must have at least $1 per remaining draft spot to complete the draft).
And once the draft is completed, and remaining draft money is rolled into the team's faab account.



* Some areas the League is looking to make some changes possibly in the future: *

Salary roll down -- salaries only roll down $2 for $1. This will limit the lowering of salaries
keeper costs -- increasing keeper costs
increasing roster spots -- to 26 like MLB is thinking about doing
faab not being applied after the keeper costs
losing faab not used that year?
lowering draft budgets further

### * Additions needed *

- [ ] Complete Settings Confirmation Function
- [ ] Eventual incorporation into the User Interface to allow teams to see simulations of team costs/player salaries based on different keeper selections (or impacts of trades)





## -- Understanding the File Management File --

This file is used to manage all the files especially during software development. However, some of its functions may be utilized
in the future for various portions of the system such as updating team rosters.

This File may become out of date once the use of GSpread and accessing the teams Google Sheet file is complete

### * Additions needed *

- [ ] Team Name change function




## -- Understanding the GooglePULL File --

This file is attempting to access the team's current Google Sheet file. This will pull current team rosters, FAAB, Keeper Selections, and player salaries. 
This information will be what is fed through the draft calculator and then re-uploaded to the GoogleSheet. This will eliminate all human errors and create instantaneously team rosters than canbe used for projections and teram analysis.

### * Additions needed *

- [ ] Dealing with Duplicate player names
- [ ] Dealing with Player Teams



## -- Understanding the GooglePUSH File --

This file is attempting to access the team's current Google Sheet file. This will push current team rosters, FAAB, Keeper Selections, and player salaries back to the League Google Sheet after Calculations on player Salaries prior to the draft are copmleted.

### * Additions needed *

- [ ] Push New Salaries to Google Sheet
- [ ] Remove Players not kept
- [ ] Add Player Teams
- [ ] Add section on Player Position?



## -- Understanding the Rankings File File --

The rankings File attempts to quantify a players production. This is done by creating an editable point system that can then be used to examine player's production throughout any year using pybaseball.


The File is also attempting to create Marcel projections and use other resources to create player projections and rankings specific to the desired league settings. 


### * Additions needed *

- [ ] Combine several projection system to create an aggregate ranking of multiple sources which should neautralize any one system to create  one that is hopefully more accurate and consistant.
- [ ] Dynasty ranking system based on several upcoming years
- [ ] Incorporating MILB stats
- [ ] Incorporating Position aligibility and position scarcity
- [ ] Create Rankings cheatsheet file
- [ ] Create Position Tiers cheatsheet file



## -- Understanding the RotoRankings File File --

The RotoRankings File attempts to quantify a players production for Rotisserie Rankings. This is used primarily for comparison to points based leagues.


### * Additions needed *

- [ ] Adjust Z-score for Lowest values of ERA and WHIP
- [ ] Adjust for stat totals (someone batting .300 for 5 ab is not worth as much as someone over 300 ab)



## -- Understanding the TeamAnalysis File --

The TeamAnalysis file compares the team rosters created by the GooglePull Program. It compares the estimated point totals for both the current year and based on the Marcel Projections.

### * Additions needed *

- [ ] Adjust to include player positions/scarcity
- [ ] incorporate the fact that onyl a specific number of players can play at a time
- [ ] Add in MILB Players (if MILB stats can be accumulated)


## -- Understanding the CostAnalysis File --

The CostAnalysis file compares player point totals and attempts to calculate and assign an estimated player salary. 

### * Additions needed *

- [ ] Adjust to include player positions/scarcity
- [ ] Compare with team rosters and current salaries
- [ ] estimate player costs for the upcoming draft (based on all teams remaining budgets, number of players, positions needed, quality of players remaining...)
- [ ] Use the cost analysis to create a trade analysis function



## -- Future project additions include:

- [ ] 1. a user interface for direct interaction with the league owners for team manipulation
    - [ ] Addition of a League Manager Dashboard and team sign-in

- [ ] 2. A MILB team draft capabilities - to replace the current system and allow for future expansion

- [ ] 3. Integration of historical baseball data for player projections, comparisons, etc... (use of the lahman database)
    - [ ] If I can find a MILB historical database that intergration would be desired as well.

- [ ] 4. Trade Block and interaction system
    - [ ] Allows for a better system for sending trade offers that include MILB players, Cash, and communication
    - [ ] possible trade analyzer at least for league owners??

- [ ] 5. League predictive analytics, projections, and analysis of team dynamics
    - [ ] Do certain characteristics or team make up/keeper selections/etc.. have a direct impact?
    - [ ] How would changes to scoring, keeper costs, etc... effect the league?
    - [ ] Interesting Facts about each team...



# DATA FILES

All data files are currently stored as CSV files within the Data Folder in the PNation directory.

Data files will need to be reorganized, but the following explanation should help explain where and what each files contains.

## -- Data Folder --

-- team_info.csv
   - Contains Master Team Infor chart directly from the Google Sheet. THis file contains Player name, FAAB Budget, Owner etc..

-- pstats.csv
   - Contains the gathered pitching stats from pybaseball from the last year searched (typically the current or most reacent season)

-- bstats.csv
   - Contains the gathered batting stats from pybaseball from the last year searched (typically the current or most reacent season)
   
-- Rankings.csv
   - Contains the merged stats stats from the bstats.csv and pstats.csv files

-- FullRoster.csv
   - Contains the most recently pulled rosters from the Google Sheet. 
   - Which included player's name, Team Owner, Player Salary, Keeping Selection, Trade Block Indicator



## -- baseballdatabank-master --
contains the Lahman Databae files


## -- Test Folder --
contains all test data files from various search queries using the pybaseball package. 
This folder is primarily used for research and understanding of how to find needed statistics.


-- kershawLookUp.csv
   - Contains query based on a player lookup based on a name (pybaseball)

-- kershaw_stats.csv
   - Contains complete list of Kershaw Stats (pybaseball)

-- Sale_statcast_range.csv
   - Contains Chris Sale's statcast Data from a range of dates (pybaseball)

-- Pitching_Stats_range.csv
   - Contains pitching stats from a range (pybaseball)
   
-- bwar_pitch.csv
   - Contains complete bwar pitching stats from pybaseball

-- batting_stats_bref.csv
   - Contains complete brief batting stats from pybaseball
   
-- batting_stats2019.csv
   - Contains complete batting stats from 2019 (pybaseball)
   
-- pitching_stats2019.csv
   - Contains complete Pitching stats from 2019 (pybaseball)

-- lah_appearances.csv
   - Contains Lahman Database Player Position Apperances

-- lah_batting.csv
   - Contains Lahman Database Batting stats
   
-- lah_pitching.csv
   - Contains Lahman Database Pitching stats


## -- YearPoints Folder --

-- contains files from each year dating from 2000-2019 (current Year)
- Each file contains the Rankings.csv stats from that given year. 

- To make adjustments for your league specifics, adjust the Rankings file with the correct point selection then run the pointcycle function located in the Master.py file.

## -- marcel Folder --

-- contains files specific to the marcel Projection system

-- currentYear.csv
   - Contains File from the most recently selected year rankings stats in Marcel Function
   
-- previousYear.csv
   - Contains File from the previous year to the most recently selected year rankings stats in Marcel Function

-- TwoYear.csv
   - Contains File from two years ago to the most recently selected year rankings stats in Marcel Function

-- MarcelResultPit.csv
   - Marcel Projected pitching totals for the upcoming year
   
-- MarcelResultBat.csv
   - Marcel Projected batting totals for the upcoming year
   
-- MarcelResulTotal.csv
   - Marcel Projected totals for the upcoming year
   
-- MarcelTable.csv
   - Marcel Projections

-- lgAVGPit.csv
   - Contains total pitching stats for each year since 2000 (data obtained from pybaseball package
   - This data is utilized in the Marcel Projection
   
-- lgAVGBat.csv
   - Contains total batting stats for each year since 2000 (data obtained from pybaseball package
   - This data is utilized in the Marcel Projection

-- lgAVG.csv
   - Contains total combined stats of batting and pitching for each year since 2000 (data obtained from pybaseball package
   - This data is utilized in the Marcel Projection
   

## -- teamAnalysis Folder --

-- ProjectionRankings.csv
   - Ranking Teams by total projected point (based on marcel projections and team roster files pulled from the Google Sheet

-- TeamPoints_Proj.csv
   - Contains projected point totals for each player
   - organized by team_id
   
-- CurrentRankings.csv
   - Ranking Teams by total the current year's point (based on marcel projections and team roster files pulled from the Google Sheet

-- TeamPoints_Current.csv
   - Contains current year's point totals for each player
   - organized by team_id

## -- Teams Folder --

-- contains team rosters for each team.
-- files are names Team with team_id Number as an identifier.


## -- CostAnalysis Folder --

-- CostAnalysis_Bat.csv
   - Contains projected salary cost of position players based on point totals and available budget

-- CostAnalysis_Bat.csv
   - Contains projected salary cost of pitchers based on point totals and available budget
