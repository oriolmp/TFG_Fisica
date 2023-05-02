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
import pickle

#from extract_df_C_last_answer import *
#from extract_df_sociodem import *
from src.extract_rectangle import extract_stories_dfs_answered_by_all_of_N_pa_participants
from src.plot_multiplex import LayeredNetworkGraph

# take only stories and (around) particpants that were answered by all/ answered all 
N_pa = 50
sociodem_entry = sys.argv[1]#"genere"
layer_tp = sys.argv[2]#uniplex


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
df_sociodem_coact = df_sociodem_coact.sort_values(by=sociodem_entry)
#print(df_sociodem_coact.index)
df_C_yo   = df_C_yo.reindex(df_sociodem_coact.index)
df_C_otro = df_C_otro.reindex(df_sociodem_coact.index)
#print(df_C_yo.index)

sub_df_these_stories_yo, sub_df_these_stories_otro, n_stories, list_stories_mt_Npa = extract_stories_dfs_answered_by_all_of_N_pa_participants(df_C_yo, df_C_otro, list_of_C_stories, N_pa, randomize=False)
print(len(sub_df_these_stories_yo), len(sub_df_these_stories_yo.T))
n_parties = len(sub_df_these_stories_yo)
#print(sub_df_these_stories_yo.index)

### Color coding
def color_coding(G, sociodem_entry, colors):
    """
    takes networkx Graph G with node id (= participant id for participant network, or story id for s.n.)
    
    and sociodem category as in df.sociodem_coact_columns

    returns list of colors in same order as nodes
    """   
    color_map = [colors[sociodem_entry][df_sociodem_coact[sociodem_entry].loc[node]] for node in G]
    return color_map

colors = { "pp"    : {"Sí":'#d7191c', "No":'#2c7bb6', "nvr":'#ffffbf', "nay":"lightgray"},
           "p_cuid": {"Sí":'#d7191c', "No":'#2c7bb6', "nvr":'#ffffbf', "nay":"lightgray"},
           "genere": {"m":"#2c7bb6", "f":"#d7191c", "d":"#fdae61", "nvr":"#abd9e9", "nay":"lightgray"},
           "edat"  : {'1':"#d73027", '2':"#fc8d59", '3':"#fee090", '4':"#e0f3f8", '5':"#91bfdb", '6':"#4575b4", 'nvr':"gray", "nay":"lightgray"},
           "p_g1"  : {"a":"#2c7bb6", "m":"#d7191c", "b":"#fdae61", "nvr":"#abd9e9", "nay":"lightgray"},
           "p_g2"  : {"a":"#2c7bb6", "m":"#d7191c", "b":"#fdae61", "nvr":"#abd9e9", "nay":"lightgray"},
           "p_l"   : {"Sí":'#d7191c', "No":'#2c7bb6', "nvr":'#ffffbf', "nay":"lightgray"},
           "p_ac" : {"Sí":'#d7191c', "No":'#2c7bb6', "nvr":'#ffffbf', "nay":"lightgray"}
      }

labels_ca = { "pp"    : {"Sí":'Sí', "No":'No', "nvr":'No vull respondre', "nay":"Encara no respost"},
           "p_cuid": {"Sí":'Sí', "No":'No', "nvr":'No vull respondre', "nay":"Encara no respost"},
           "genere": {"m":"home", "f":"dona", "d":"No binari", "nvr":"No vull respondre", "nay":"Encara no respost"},
           "edat"  : {'1':'18-24 anys', '2':'25-34 anys', '3':'35-44 anys', '4':'45-54 anys', '5':'55-64 anys', '6':'65+ anys', 'nvr':'No vull respondre', "nay":"Encara no respost"},
           "p_g1"  : {"a":"Alt", "m":"Mitjà", "b":"Baix", "nvr":'No vull respondre', "nay":"Encara no respost"},
           "p_g2"  : {"a":"Alt", "m":"Mitjà", "b":"Baix", "nvr":'No vull respondre', "nay":"Encara no respost"},
           "p_l"   : {"Sí":'Sí', "No":'No', "nvr":'No vull respondre', "nay":"Encara no respost"},
           "p_ac" : {"Sí":'Sí', "No":'No', "nvr":'No vull respondre', "nay":"Encara no respost"}  
           
           
      }

super_title_cat = {"genere":" pel seu gènere",
          "edat":" pel seu rang d'edat",
          "pp":" per si tenen o han tingut problemes de salut mental",
          "p_cuid":" per si són persones cuidadores d'una persona que té problemes de salut mental",
          "p_g1"  : " per seu grau de implicació amb els pSM del seu entorn",
          "p_g2"  : " pel grau de implicació del entorn amb pSM amb el seu benestar",
          "p_l"   : " per si té pp al ambit laboral",
          "p_ac" : " per si té pp al ambit d'oci" }  

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




#axes = [ax1, ax2, ax3, ax6]


for axi, story in enumerate(["Compartir", "Experiencia_aprenentatge", "Ingresada"]):#'capacitation_Teatre_Amigues', 'Obrir_camí', 'Experiencia_aprenentatge', 'Gossos', 'Sanglotant']):

    figure = plt.figure(figsize=(8,8), num=super_title_cat[sociodem_entry] )
    figure.gca().set_axis_off()
    ax = figure.add_subplot(projection='3d')
    ax.set_axis_off()
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
        #ax.set_title("Has tingut la mateixa vivència? >>> Sí.")
        LayeredNetworkGraph([G_yo_AA], 
                         node_labels=node_labels, 
                         node_color=color_coding(G_yo_AA, sociodem_entry, colors), 
                         plane_labels = ["Has tingut\nla mateixa vivència?\n>>> Sí.\n\n\n"
                         ], 
                         plane_colors = ["#fee090"],
                         ax=ax, 
                         layout=nx.circular_layout)
        ax.set_xlim([-1, 1.5])
        ax.set_ylim([-1, 1.5])
        ax.set_zlim([-0.25, 0.25])
    elif layer_tp=="multiplex":
        LayeredNetworkGraph([G_otro_AA, G_yo_AA], 
                         node_labels=node_labels, 
                         node_color=color_coding(G_yo_AA, sociodem_entry, colors), 
                         plane_labels = [
                         "Algú del teu entorn ha tingut\nla mateixa vivència?\n >>> Sí.",
                         "Has tingut\nla mateixa vivència?\n >>> Sí."], 
                         plane_colors = ["#fc8d59", "#fee090"],
                         ax=ax, 
                         layout=nx.circular_layout)
        ax.set_xlim([-1, 1.5])
        ax.set_ylim([-1, 1.5])
    
    ax.set_axis_off()
    pickle.dump(figure, open('FigureObject_'+sociodem_entry+'_'+layer_tp+"_"+story+'.pickle', 'wb')) 
plt.show()
fig = plt.figure(figsize=(8,8), num=super_title_cat[sociodem_entry] )#figsize=plt.figaspect(0.6))
#plt.title("- Comparació xarxes de "+str(n_parties)+" participants"+super_title_cat[sociodem_entry]+" -", pad=50)
plt.gca().set_axis_off()

ax0 = fig.add_subplot()
ax0.set_axis_off()
ax6 = ax0.inset_axes([0, 0., 0.75, 0.75])
    
df_sociodem_these_stories = df_sociodem_coact[df_sociodem_coact.index.isin(sub_df_these_stories_yo.index)]#[sociodem_entry]
startangle=60

df_sociodem_these_stories[sociodem_entry].value_counts().reindex(list(colors[sociodem_entry].keys())[::-1]).plot(kind="pie",
               labels = list(labels_ca[sociodem_entry].values())[::-1],
               colors = list(colors[sociodem_entry].values())[::-1], 
               autopct=lambda x: '{:.0f}'.format(x*df_sociodem_these_stories[sociodem_entry].value_counts().sum()/100),
               ax     = ax6,
               startangle=-30,
               fontsize=12)
               
titles = {"genere":"Quin és el gènere\namb què més et identifiques?",
          "edat":"A quin rang d'edat\npertanys (en anys)?",
          "pp":"Vius o has viscut\nproblemas de salut mental?",
          "p_cuid":"Ets persona cuidadora\nd'una persona que té\nproblemes de salut mental?",
          "p_g1"  : "En general, com definiries\nel teu grau d implicació en referència\nals problemes de salut mental del teu entorn social?",
          "p_g2"  : "En general, en relació amb\nel teu propi benestar, com definiries\nel grau d implicació de les persones\namb qui et relaciones i que tenen\nproblemes de salut mental?",
          "p_l"   : "Una o diverses persones\ndel teu entorn laboral\nté o tenen problemes de salut mental?",
          "p_ac" : "Una o diverses persones\namb qui et relaciones a través d'activitats culturals o d oci\nté o tenen problemes de salut mental?" }    
                           
ax6.set_title(titles[sociodem_entry], fontsize=10)
ax6.set_ylabel("")

pickle.dump(fig, open('FigureObject_'+sociodem_entry+'_'+layer_tp+'_pie.pickle', 'wb')) 
plt.show()

