# PNation
Procrastination Fantasy Baseball


The following project was created with the sole intent
in creating a Fantasy baseball salary calculator for the
Procrastination Fantasy League. 

-- Future project additions include:

1. a user interface for direct interaction with the league owners for team manipulation
    - Addition of a League Manager Dashboard and team sign-in

2. A MILB team draft capabilities - to replace the current system and allow for future expansion

3. Integration of historical baseball data for player projections, comparisons, etc... (use of the lahman database)
    - If I can find a MILB historical database that intergration would be desired as well.
    
4. Trade Block and interaction system... possible trade analyzer at least for league owners??

5. League predictive analytics, projections, and analysis of team dynamics
    -  Do certain characteristics or team make up/keeper selections/etc.. have a direct impact?
    - how would changes to scoring, keeper costs, etc... effect the league?
    
    
    
    
    
-- Understanding the Calculator -- 

The Procrastination League utilizes a very specific calculation to determine player salaries.

I created and the league currently uses a Google Sheet to calculate team salaries, draft budgets, etc...
for reference you can view the sheet here: 
https://docs.google.com/spreadsheets/d/1Z08eDxf6zWTdcBjk0MuLqNrRBqT6nPLhd_In45e8W0I/edit?usp=sharing

The league began in 2016. It was a auction system draft and each team recieved $400 for the draft.
  - Teams are made up of 25 roster spots and 5 il spots.

Teams can keep up to 25 players going into the following year's draft. The salaries from the previous year's draft
are used when calculating the upcoming year's team budget.

Cash remining after the draft is rolled into the teams faab account. This money is used for wavier wire pick ups, trades,
or as we will discuss player salary roll downs. 

-- Salary Roll Down

Before the draft remaining faab is used to evenly pay down player salaries. If you had $15 remining of faab, the 
first 15 players, over $1, on your roster would subtract $1 from each of their salaries. If a player's salary is already at $1
then that players salary is skipped and applied to the following player. (No player may have less than a $1 salary)

If, in the example provided above, you only kept 10 players then all 10 would lose $1 and then the first five would lose another $1. 
So the first 5 players would decrease by $2 and the last 5 would decrease by only $1. If money remains it rolls over to the Keeper costs.

-- Keeper Costs

After the faab is applied then the keeper cost is applied to the player's salary. To keep a player, their salary will increase by $5 
(after the faab is applied). If any faab remains player's salaries could be rolled down with any remaining faab until player's 
salaries reach $1. If any faab is left it is applied to the team's draft budget.

-- Draft Budget

Once the team's salary is finalized the teams cost is subtracted from the yearly draft budget (which has now decreased to $300 a year).
Teams draft any remaining players with any remaining cash (teams must have at least $1 per remaining draft spot to complete the draft).
And once the draft is completed, and remaining draft money is rolled into the team's faab account.



Some areas the League is looking to make some changes:

Salary roll down -- salaries only roll down $2 for $1. This will limit the lowering of salaries
keeper costs -- increasing keeper costs
increasing roster spots -- to 26 like MLB is thinking about doing
faab not being applied after the keeper costs
losing faab not used that year?
lowering draft budgets further

