import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns

# reading csv file and selecting the column
df = pd.read_csv('/Users/philmoon/Documents/rna_pracitce_mac/vdj_cellranger/csv/IgHJ2_summary_113020_PM.csv', index_col = 'IGHV')

# outputting figure and axes using matplotlib
fig, ax = plt.subplots(figsize = (6, 18))

# creating colormap/heatmap using seaborn
sns.heatmap(df, cmap = "vlag", square = True, linewidth = 0.3, cbar_kws = {"shrink": 0.4})

# labeling titles and axes.
ax.set_title("V-J2 Heavy Chains", fontsize = 22, fontweight = "bold")
plt.ylabel("IgHV", fontsize = 22 ,fontweight = "bold")
plt.xlabel("IgHJ2", fontsize = 22, fontweight = "bold")

# saving the plot
plt.savefig("vj2_heavy_wt.png")