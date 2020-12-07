import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

# load the dataset
j2_csv = pd.read_csv('/Users/philmoon/Documents/rna_pracitce_mac/cellranger_vdj/csv/IgHJ2_summary_113020_PM.csv')

# select the colums.
df = j2_csv.loc[:, ['WT', 'VAC', 'A', 'R']]

# create heatmap.

heatmap_df = pd.pivot_table(df, values = ['WT', 'VAC', 'A', 'R'], index = 'IGHV')

sns.clustermap(heatmap_data, cmap = "vlag")
plt.savefig('J2_VJ_wt.png', dpi = 150, figsize = (8,12))

#df = pd.read_csv('IgHJ2_summary_113020_PM.csv', 
#                usecols=[1,3], names=['IGHV', 'WT'], index_col = 0)