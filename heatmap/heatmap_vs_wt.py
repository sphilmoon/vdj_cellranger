from matplotlib import pyplot as plt
import seaborn as sns
#sns.set_theme()
import numpy as np
import code
import pandas as pd

#data = np.loadtxt("wt_comparison_vloupe-top-clonotypes.csv", delimiter=",",skiprows=1)
lines = open("top_clonotypes_vs_wt.csv").readlines()

values = []
tags = []
head= lines[0].strip().split(",")

for line in lines[1:]: # excluding the header. Starting from the 2nd row.
    parse = line.strip().split(",")
    values.append([float(i) for i in parse[-3:]])
    tags.append(parse[:-3])
    #print(parse[:-4])

tags = np.asarray(tags)
v_gene = tags[:,1]
#print(tags[1], values[1])
np_values = np.asarray(values)
#code.interact(local=dict(globals(), **locals())) # for interactive mode to monitor what has been processed.

np_values = pd.DataFrame(np_values,columns=list(head[-3:]), index = v_gene)

#print(type(np_values[0][0]))
plt.figure(1, figsize=(25, 25))

ax = sns.heatmap(np_values,cmap="RdYlGn")

plt.ylabel("IgH+L V genes vs WT", fontsize=22)
plt.xlabel("Conditions", fontsize=22)

ax.plot()
plt.savefig("clonotype_vs_wt.png")
