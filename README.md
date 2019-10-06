# PNation
Procrastination Fantasy Baseball


The following project was created with the sole intent
in creating a Editable Fantasy baseball Ranking System specific to league settings:

http://fantasy.espn.com/baseball/league?leagueId=25593

to replace our current system located here:

https://docs.google.com/spreadsheets/d/1Z08eDxf6zWTdcBjk0MuLqNrRBqT6nPLhd_In45e8W0I/edit?usp=sharing




## -- Understanding the Draft Calculator --

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

### -- Salary Roll Down

Before the draft remaining faab is used to evenly pay down player salaries (of keepers). If you had $15 remining of faab, the
first 15 players, over $1, on your roster would subtract $1 from each of their salaries. If a player's salary is already at $1
then that players salary is skipped and applied to the following player. (No player may have less than a $1 salary)

If, in the example provided above, you only kept 10 players then all 10 would lose $1 and then the first five would lose another $1.
So the first 5 players would decrease by $2 and the last 5 would decrease by only $1. If money remains it rolls over to the Keeper costs.

### -- Keeper Costs

After the faab is applied then the keeper cost is applied to the player's salary. To keep a player, their salary will increase by $5
(after the faab is applied). If any faab remains player's salaries could be rolled down with any remaining faab until player's
salaries reach $1. If any faab is left it is applied to the team's draft budget.

### -- Draft Budget

Once the team's salary is finalized the teams cost is subtracted from the yearly draft budget (which has now decreased to $300 a year).
Teams draft any remaining players with any remaining cash (teams must have at least $1 per remaining draft spot to complete the draft).
And once the draft is completed, and remaining draft money is rolled into the team's faab account.



Some areas the League is looking to make some changes possibly in the future:

Salary roll down -- salaries only roll down $2 for $1. This will limit the lowering of salaries
keeper costs -- increasing keeper costs
increasing roster spots -- to 26 like MLB is thinking about doing
faab not being applied after the keeper costs
losing faab not used that year?
lowering draft budgets further

### -- Additions needed

- Eventual incorporation into the User Interface to allow teams to see simulations of team costs/player salaries based on different keeper selections (or impacts of trades)





## -- Understanding the File Management --

This file is used to manage all the files especially during software development. However, some of its functions may be utilized
in the future for various portions of the system such as updating team rosters.

This File may become out of date once the use of GSpread and accessing the teams Google Sheet file is complete

Future additons will include:
Team Name change function




## -- Understanding the GooglePULL --

This file is attempting to access the team's current Google Sheet file. This will pull current team rosters, FAAB, Keeper Selections, and player salaries. 
This information will be what is fed through the draft calculator and then re-uploaded to the GoogleSheet. This will eliminate all human errors and create instantaneously team rosters than canbe used for projections and teram analysis.




## -- Understanding the GooglePUSH --

This file is attempting to access the team's current Google Sheet file. This will push current team rosters, FAAB, Keeper Selections, and player salaries back to the League Google Sheet after Calculations on player Salaries prior to the draft are copmleted.




## -- Understanding the Rankings File --

The rankings File attempts to quantify a players production. This is done by creating an editable point system that can then be used to examine player's production throughout any year using pybaseball.


The File is also attempting to create Marcel projections and use other resources to create player projections and rankings specific to the desired league settings. 


-Eventual Addition
It is hoped that various projection system data can be scraped in order to create an aggregate ranking of multiple sources.
By creating a aggregate it should neautralize any one system to create  one that is hopefully more accurate.

It is also desired to add the ability to look at stats for several upcoming years to create a proper dynaty ranking system.




## -- Understanding the RotoRankings File --

The RotoRankings File attempts to quantify a players production for Rotisserie Rankings. This is used primarily for comparison to points based leagues.




## -- Understanding the TeamAnalysis File --

The TeamAnalysis file compares the team rosters created by the GooglePull Program. It compares the estimated point totals for both the current year and based on the Marcel Projections.




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





