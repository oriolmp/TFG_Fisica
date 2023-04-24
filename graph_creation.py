import pandas as pd
import networkx as nx
import numpy as np
import os
import itertools
from utils import edge_weight, young_old

# This file generates a graph from the answers to different stories.

ANSWERS_TYPE_C_PATH = './data/Answers_to_Microstories/answers_stories_C.pkl'
SOCIODEMOGRAPHIC_DATA_PATH = './data/Sociodemographic_survey/answers_sociodemographic_survey.pkl'
GRAPH_DIRECTORY = './graphs/'
N_PA = 50


# Load data
df_C = pd.read_pickle(ANSWERS_TYPE_C_PATH)
df_sociodem = pd.read_pickle(SOCIODEMOGRAPHIC_DATA_PATH)

# Preprocess answers dataframe 
df_C.columns = df_C.columns.swaplevel(0, 1)

for ans_type in ['yo', 'otro']:
    if ans_type == 'yo':
        df_ans = df_C.yo_final
        graph_name = 'yo_'
    else:
        df_ans = df_C.otro_final
        graph_name = 'otro_'
        
    # Get only stories with more than N_PA answers and drop rows that contain null values
    subset_df = df_ans.loc[:, df_ans.count() > N_PA]
    subset_df = subset_df.dropna(how='any')

    # Compute list of 3-D tuples containing (user_id_1, user_id_2, avg_weight_1_2) for selected stories
    stories = subset_df.columns
    pairs = itertools.combinations(subset_df.index, 2)

    elist_yo = [(pair[0], pair[1], edge_weight(df_ans, pair, stories)) for pair in pairs]   

    # Generate graph
    G = nx.Graph()
    G.add_weighted_edges_from(elist_yo)

    # Set node attributes
    attrs = {node: {"age_bracket": young_old(df_sociodem.loc[node].edat)} for node in G.nodes()}
    nx.set_node_attributes(G, attrs)

    # Save graph
    i = 0
    graph_path = GRAPH_DIRECTORY + graph_name + f'{i}.graphml'
    while os.path.exists(graph_path):
        i += 1
        graph_path = GRAPH_DIRECTORY + graph_name + f'{i}.graphml'

    nx.write_graphml(G, graph_path)
    print(f'Graph saved at {graph_path}')