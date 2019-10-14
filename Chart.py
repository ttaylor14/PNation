import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

roster = pd.read_csv('data/Rankings.csv')

roster = roster[['Total_Points', 'Age_bat', 'Points_bat', 'Points_pit', 'AB_bat', 'HR_bat', 'SB_bat', 'GS_pit', 'IP_pit', 'SO_pit']]

sns.pairplot(roster)


plt.show()
