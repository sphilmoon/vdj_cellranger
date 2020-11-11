from matplotlib import pyplot as plt
import seaborn as sns
#sns.set_theme()
import numpy as np
import code
import pandas as pd


#data = np.loadtxt("wt_comparison_vloupe-top-clonotypes.csv", delimiter=",",skiprows=1)
def wt_comparison_vloupe_top_clonotypes():
	lines = open("wt_comparison_vloupe-top-clonotypes.csv").readlines()

	values = []
	tags = []
	head= lines[0].strip().split(",")

	for line in lines[1:]:
		parse = line.strip().split(",")
		values.append([float(i) for i in parse[-4:]])
		tags.append(parse[:-4])
		#print(parse[:-4])


	tags = np.asarray(tags)
	v_gene = tags[:,1]
	#print(tags[1], values[1])
	np_values = np.asarray(values)


	np_values = pd.DataFrame(np_values,columns=list(head[-4:]), index = v_gene)


	#print(type(np_values[0][0]))
	plt.figure(1, figsize=(25, 25))


	ax = sns.heatmap(np_values,cmap="YlGnBu")

	plt.ylabel("Clonotypes", fontsize=18)
	plt.xlabel('Conditions', fontsize=18)



	ax.plot()
	plt.savefig("temp4.png")

def top_clonotypes_vs_vac():
	#fig = plt.figure()

	f, axes = plt.subplots(1, 3)

	csv_test = pd.read_csv('top_clonotypes_vs_vac.csv',index_col = 'v_gene' )
	#code.interact(local=dict(globals(), **locals()))
	#plt.ylabel("Clonotypes", fontsize=18)

	#============= plotting A ==============
	df_A = csv_test.loc[:,('A.1')]
	df_A_np = df_A.to_numpy().reshape(200,1) # for add dimension (200,) -> (200,1)
	df_A = pd.DataFrame(df_A_np, index =  df_A.index)
	df_A = df_A.sort_values(by=[0], ascending=True) # False for descending.

	fig = plt.figure(1, figsize=(25, 25)) # now let's create clustermap.
	#ax1 = sns.heatmap(data = df_A,cmap="YlGnBu",ax=axes[0])
	ax1 = sns.clustermap(data = df_A,cmap="YlGnBu",ax=axes[0])
	ax1.xaxis.set_label_text('A')
	ax1.yaxis.set_label_text('Clonotypes')

	#plt.xlabel('A', fontsize=18)
	#plt.savefig("ascending.png")

	#============= plotting R ==============

	df_R = csv_test.loc[:,('R.1')]
	df_R_np = df_R.to_numpy().reshape(200,1) # for add dimension (200,) -> (200,1)
	df_R = pd.DataFrame(df_R_np, index =  df_R.index)
	df_R = df_R.sort_values(by=[0], ascending=True)

	fig = plt.figure(1, figsize=(25, 25))
	ax2 = sns.heatmap(data=df_R,cmap="YlGnBu",ax=axes[1])
	ax2.xaxis.set_label_text('R')
	ax2.yaxis.set_label_text('')

	#============= plotting WT ==============

	df_WT = csv_test.loc[:,('WT.1')] # now create array below using reshape.
	df_WT_np = df_WT.to_numpy().reshape(200,1) # for add dimension (200,) -> (200,1)
	df_WT = pd.DataFrame(df_WT_np, index =  df_WT.index)
	df_WT = df_WT.sort_values(by=[0], ascending=True)

	fig = plt.figure(1, figsize=(25, 25))
	ax3 = sns.heatmap(data= dfcd_WT,cmap="YlGnBu",ax=axes[2])
	ax3.xaxis.set_label_text('WT')
	ax3.yaxis.set_label_text('')
	plt.show()
	plt.savefig("subplot_test.png")

def top_clonotypes_vs_vac_dendro():
	fig = plt.figure(1, figsize=(25, 25))
	from scipy.cluster.hierarchy import dendrogram, linkage
	csv_test = pd.read_csv('top_clonotypes_vs_vac.csv',index_col = 'v_gene' )
	df_A = csv_test.loc[:,('A.1')]
	df_A_np = df_A.to_numpy().reshape(200,1) # adding dimension (200,) -> (200,1)
	df_A = pd.DataFrame(df_A_np, index =  df_A.index)
	df_A = df_A.sort_values(by=[0], ascending=True)
	#del df_A.index.name

	Z = linkage(df_A, 'ward')

	# Make the dendro
	#labels=df_A.index
	#code.interact(local=dict(globals(), **locals()))
	#dendrogram(Z, leaf_rotation=0, orientation="left", color_threshold=240, above_threshold_color='grey')
	dendrogram(Z, labels=list(df_A.index), leaf_rotation=0, orientation="left", color_threshold=240, above_threshold_color='grey')
	plt.show()
	plt.savefig("dendrogram_only.png")
	"""
	# Create a color palette with 3 color for the 3 cyl possibilities
	my_palette = plt.cm.get_cmap("Accent", 3)

	# transform the 'cyl' column in a categorical variable. It will allow to put one color on each level.
	df['cyl']=pd.Categorical(df['cyl'])
	my_color=df['cyl'].cat.codes

	# Apply the right color to each label
	ax = plt.gca()
	xlbls = ax.get_ymajorticklabels()
	"""

	"""
	num=-1
	for lbl in xlbls:
		num+=1
		val=my_color[num]
		lbl.set_color(my_palette(val))

	"""




	pass

#top_clonotypes_vs_vac()
top_clonotypes_vs_vac_dendro()

#wt_comparison_vloupe_top_clonotypes()

"""
method=’single’
method=’complete’
method=’average’
method=’weighted’
method=’centroid’
method=’median’
method=’ward’
"""
