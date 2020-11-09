import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Loading the dataset
vgene_csv = pd.read_csv('top_clonotypes_vs_wt.csv', index_col = 'v_gene')

# Selecting subsets of the networks.
df = vgene_csv.loc[:, ['A_wt', 'R_wt', 'VAC_wt']]

# Creating a heatmap using Seaborn's clustermap.
heatmap_data = pd.pivot_table(df, values=['A_wt', 'R_wt', 'VAC_wt'],
                              index='v_gene')
                              #columns='Conditions')
sns.clustermap(heatmap_data, cmap="vlag")
plt.savefig('hi_wt_vlag.png', dpi=150, figsize=(8,12))

#reference: https://cmdlinetips.com/2020/01/heatmaps-with-seaborns-clustermap/
