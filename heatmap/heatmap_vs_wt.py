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

def top_clonotypes_vs_vac():
	fig = plt.figure()

	f, axes = plt.subplots(1, 3)

	csv_test = pd.read_csv('top_clonotypes_vs_wt.csv',index_col = 'v_gene' )
	#code.interact(local=dict(globals(), **locals()))
	plt.ylabel("Clonotypes", fontsize=18)

	#============= plotting A ==============
	df_A = csv_test.loc[:,('A.1')]
	df_A_np = df_A.to_numpy().reshape(200,1) # for add dimension (200,) -> (200,1)
	df_A = pd.DataFrame(df_A_np, index =  df_A.index)
	df_A = df_A.sort_values(by=[0], ascending=True) # False for descending.

	fig = plt.figure(1, figsize=(25, 25)) # now let's create clustermap.
	ax1 = sns.heatmap(data = df_A,cmap="YlGnBu",ax=axes[0])
	ax1 = sns.clustermap(data = df_A,cmap="YlGnBu",ax=axes[0])
	ax1.xaxis.set_label_text('A')
	ax1.yaxis.set_label_text('Clonotypes')

	plt.xlabel('A', fontsize=18)
	plt.show()
	plt.savefig("ascending_wt.png")

top_clonotypes_vs_vac()
