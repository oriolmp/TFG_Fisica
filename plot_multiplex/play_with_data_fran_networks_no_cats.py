import numpy as np
import itertools
import networkx as nx
import random
import pandas as pd
import sys
# load plotting libraries
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import plotly.express as px
import matplotlib.font_manager as fm 
fm.findSystemFonts(fontpaths=None, fontext='otf')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Glacial Indifference'

#from extract_df_C_last_answer import *
#from extract_df_sociodem import *
from src.extract_rectangle import extract_stories_dfs_answered_by_all_of_N_pa_participants
from src.plot_multiplex import LayeredNetworkGraph

# take only stories and (around) particpants that were answered by all/ answered all 
N_pa = 50
story = sys.argv[1] # Experiencia_aprenentatge
layer_tp = sys.argv[2] # uniplex

ANSWERS_TYPE_C_PATH = '../data/Answers_to_Microstories/answers_stories_C.pkl'
SOCIODEMOGRAPHIC_DATA_PATH = '../data/Sociodemographic_survey/answers_sociodemographic_survey.pkl'
N_PA = 50

# Load data
df_C = pd.read_pickle(ANSWERS_TYPE_C_PATH)
df_sociodem = pd.read_pickle(SOCIODEMOGRAPHIC_DATA_PATH)

# Preprocess answers dataframe 
df_C.columns = df_C.columns.swaplevel(0, 1)
df_C_yo = df_C.yo_final
df_C_yo = df_C_yo.loc[:, df_C_yo.count() > N_PA]
df_C_yo = df_C_yo.dropna(how='any')
df_C_otro = df_C.otro_final
df_C_otro = df_C_otro.loc[:, df_C_otro.count() > N_PA]
df_C_otro = df_C_otro.dropna(how='any')
df_sociodem_coact= df_sociodem
list_of_C_stories     = list(df_C_yo.columns)

# sort participants by gender
#df_sociodem_coact = df_sociodem_coact.sort_values(by=sociodem_entry)
#print(df_sociodem_coact.index)
df_C_yo   = df_C_yo.reindex(df_sociodem_coact.index)
df_C_otro = df_C_otro.reindex(df_sociodem_coact.index)
#print(df_C_yo.index)

sub_df_these_stories_yo, sub_df_these_stories_otro, n_stories, list_stories_mt_Npa = extract_stories_dfs_answered_by_all_of_N_pa_participants(df_C_yo, df_C_otro, list_of_C_stories, N_pa, randomize=False)

n_parties = len(sub_df_these_stories_yo)
#print(sub_df_these_stories_yo.index)

### Color coding
def color_coding(G):
    """
    takes networkx Graph G with node id (= participant id for participant network, or story id for s.n.)
    
    and sociodem category as in df.sociodem_coact_columns

    returns list of colors in same order as nodes
    """   
    color_map = ['#ffbf00' for node in G]
    return color_map

def connect_pair(pair_answers, answers=["A","A"]):
    """
    connect pair if participants answered as "answers"
    """
    x = set(pair_answers)
    y = set(answers)
    if x==y:
        connection = 1
    else:
        connection = 0
    return connection

# weighted connection of participants according to their answers
def create_connection(sub_table_answers, n_stories, n_answers, answers=["A","A"], cutoff=1./2.):
    """
    create connections between participants according to their answers
    """
    weight = sum([connect_pair(sub_table_answers.loc[story], answers=answers) for story in sub_table_answers.index])
    weight = weight/len(sub_table_answers.index) # normalize by number of stories
    #print(weight)
    if weight > cutoff:
        return 1
    else:
        return 0



def generate_list_of_edges(sub_df_these_stories_yo, sub_df_these_stories_otro, n_stories, N_pa, answers=["A","A"]):
    """
    takes complete story df (without None/nay)
    and calculates a weight for each pair of participants
    stores the two participants and the weight in a tuple of length 3
    returns two list of all tuples, one for "yo" and one for "otro".
    """
    n_answers = len(sub_df_these_stories_yo.index)
    all_non_identical_2ples_N_pa = list(itertools.combinations(sub_df_these_stories_yo.index, 2))
    elist_yo = [(a, b, create_connection(sub_df_these_stories_yo.loc[[a, b]].T, n_stories, n_answers, answers=answers)) 
        for (a, b) in all_non_identical_2ples_N_pa if not create_connection(sub_df_these_stories_yo.loc[[a, b]].T, n_stories, n_answers, answers=answers)==0] # list of edges yo
    elist_otro = [(a, b, create_connection(sub_df_these_stories_otro.loc[[a, b]].T, n_stories, n_answers, answers=answers)) 
        for (a, b) in all_non_identical_2ples_N_pa if not create_connection(sub_df_these_stories_otro.loc[[a, b]].T, n_stories, n_answers, answers=answers)==0] # list of edges otro
    return elist_yo, elist_otro

# generate 3er tuples of (id_participant_1, id_participant_2, weight_p1_p2)



def create_graph_from_edges_and_nodes_list(elist, node_list):
    """
    creates graph and adds weighted edges from list of 3er tuples
    """
    G = nx.Graph()
    #for node in node_list:
    #    #print(df_sociodem_coact.loc[node, sociodem_entry])
    #    G.add_node(node, gender=df_sociodem_coact.loc[node, sociodem_entry])
    G.add_nodes_from(node_list)
    G.add_weighted_edges_from(elist)
    return G
if layer_tp=="uniplex":
    fig = plt.figure(figsize=(8,8), num=story)#figsize=plt.figaspect(0.6))
elif layer_tp=="multiplex":
    fig = plt.figure(figsize=(8,8), num=story)#figsize=plt.figaspect(0.6))
"""if layer_tp=="uniplex":
    plt.title("- Xarxes de "+str(n_parties)+" participants connectades si han viscut "+story+" -", pad=50)
elif layer_tp=="multiplex":
    plt.title("- Xarxes de "+str(n_parties)+" participants connectades si \no coneixen algú que hagi viscut \no han viscut els mateixos: relat "+story+" -", pad=50)
"""
plt.gca().set_axis_off()

ax = fig.add_subplot(projection='3d')

#print(sub_df_these_stories_yo)
sub_df_this_stories_yo   = pd.DataFrame(sub_df_these_stories_yo[story])
sub_df_this_stories_otro = pd.DataFrame(sub_df_these_stories_otro[story])
elist_yo_AA, elist_otro_AA = generate_list_of_edges(sub_df_this_stories_yo, sub_df_this_stories_otro, n_stories, N_pa, answers=["A","A"])
node_list = list(sub_df_this_stories_yo.index)
#print(node_list)
#print(elist_yo_AA)
G_yo_AA = create_graph_from_edges_and_nodes_list(elist_yo_AA, node_list)
G_otro_AA = create_graph_from_edges_and_nodes_list(elist_otro_AA, node_list)
#print(set(elist_yo_AA)-set(elist_otro_AA))

elist_yo_CC, elist_otro_CC = generate_list_of_edges(sub_df_this_stories_yo, sub_df_this_stories_otro, n_stories, N_pa, answers=["C","C"])
node_list = list(sub_df_this_stories_yo.index)
G_yo_CC = create_graph_from_edges_and_nodes_list(elist_yo_CC, node_list)
G_otro_CC = create_graph_from_edges_and_nodes_list(elist_otro_CC, node_list)
#print(set(elist_yo_CC)-set(elist_otro_CC))

node_labels = {nn : str(nn) for nn in range(len(G_yo_AA.nodes))}
# initialise figure and plot
#ax.set_title(story)
if layer_tp=="uniplex":
    LayeredNetworkGraph([G_yo_AA], 
                     node_labels=node_labels, 
                     node_color=color_coding(G_yo_AA), 
                     plane_labels = [
                     "Has tingut\nla mateixa vivència?\n >>> Sí."], 
                     plane_colors = ["#fee090"],
                     ax=ax, 
                     layout=nx.circular_layout)
    ax.set_zlim([-0.25, 0.25])
elif layer_tp=="multiplex":
    LayeredNetworkGraph([G_otro_AA, G_yo_AA], 
                     node_labels=node_labels, 
                     node_color=color_coding(G_yo_AA), 
                     plane_labels = [
                     "Algú del teu entorn\nha tingut\nla mateixa vivència?\n >>> Sí.",
                     "Has tingut\nla mateixa vivència?\n >>> Sí."], 
                     plane_colors = ["#fc8d59", "#fee090"],
                     ax=ax, 
                     layout=nx.circular_layout)

ax.set_axis_off()
    
import pickle
pickle.dump(fig, open('FigureObject_'+story+'_'+layer_tp+'.pickle', 'wb')) 

plt.show()


