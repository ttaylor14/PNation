# Creating Roto Rankings

# last Update : 10.13.19

# Creating Chart to Visually Show how Points are distributed for the top 10 ranked players each year


# libraries
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import seaborn as sns


currentYear = 2019

AllTeam = pd.DataFrame()

yearRange = list(range(2000, currentYear + 1))
# print(yearRange)
for x in yearRange:

    filename = "%s.csv" % x
    team = pd.read_csv(filename, sep=',', encoding='utf-8')

    team = team[:50]
    #print(team)

    AllTeam = pd.concat([AllTeam, team])






AllTeam = AllTeam[['Rank', 'Total_Points', 'Season_bat']]

AllTeam.rename(columns={'Season_bat':'Season'}, inplace=True)

AllTeam.rename(columns={'Rank':'Player_Ranking'}, inplace=True)



pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                    '#78CA50',
                    '#F08630',
                    '#6896F0',
                    '#A87820',
                    '#A88878',
                    '#AAA878'
                   ]


sns.lineplot(data= AllTeam, x="Player_Ranking", y="Total_Points", hue="Season", palette=pkmn_type_colors, markers=True, dashes=True, sort=False)

plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.title('Historical Points Scored by Top 50 Ranked Players Each Year')
plt.show()
