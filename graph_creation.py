import pandas as pd
import networkx as nx
import numpy as np
import os
from utils import weight

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
df_C_yo = df_C.yo_final
# df_C_otro = df_C.otro_final

# Get only stories with more than N_PA answers and drop rows that cotanin null values
subset_df = df_C_yo.loc[:, df_C_yo.count() > N_PA]
subset_df = subset_df.dropna(how='any')

# Generate list of 3-D tuples containing (user_id_1, user_id_2, weight_1_2) for all stories
elist_yo = {}
story_count = 1
for column in subset_df.columns:
    print(f'Computing weights for story number {story_count}: {column}...')
    
    elist_yo[column] = []
    for i, id1 in enumerate(subset_df.index):
        for j, id2 in enumerate(subset_df.index):
            if j > i:
                pair = (id1, id2, weight(subset_df[column][id1], subset_df[column][id2]))
                elist_yo[column].append(pair)

    # limit the number of stories to analyze to fasten computation
    if story_count == 1:
        break
    story_count += 1
print('Weights computation complete!')

# Generate graph
story = 'capacitation_Teatre_Amigues'
ans_lst = elist_yo[story]
G = nx.Graph()
G.add_weighted_edges_from(ans_lst)

# Save graph
i = 0
graph_path = GRAPH_DIRECTORY + f'graph_{i}.graphml'
while os.path.exists(graph_path):
    i += 1
    graph_path = GRAPH_DIRECTORY + f'graph_{i}.graphml'

nx.write_graphml(G, graph_path)
print(f'Graph saved at {graph_path}')