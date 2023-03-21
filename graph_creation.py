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

# Get only stories with more than N_PA answers and drop rows that contain null values
subset_df = df_C_yo.loc[:, df_C_yo.count() > N_PA]
subset_df = subset_df.dropna(how='any')

# Generate list of 3-D tuples containing (user_id_1, user_id_2, weight_1_2) for all stories
elist_yo = {}
story_count = 1
for column in subset_df.columns:
    elist_yo[column] = []
    for i, id1 in enumerate(subset_df.index):
        for j, id2 in enumerate(subset_df.index):
            if j > i:
                pair = (id1, id2, weight(subset_df[column][id1], subset_df[column][id2]))
                elist_yo[column].append(pair)
    story_count += 1
print('Weights computation complete!')

# Compute average weights from each pair of nodes among all stories
sample_key = list(elist_yo.keys())[0]
weights_matrix = np.empty((len(elist_yo), len(elist_yo[sample_key])))

for i, story in enumerate(elist_yo):
    for j, pair in enumerate(elist_yo[story]):
        weights_matrix[i-1][j-1] = pair[2]

avg_weights = np.mean(weights_matrix, axis=0)

# Get a list with all nodes pairs and their average weight
avg_list = []
for i, pair in enumerate(elist_yo[sample_key]):
    avg_list.append((pair[0], pair[1], avg_weights[i]))


# Generate graph
G = nx.Graph()
G.add_weighted_edges_from(avg_list)

# Save graph
i = 0
graph_path = GRAPH_DIRECTORY + f'graph_{i}.graphml'
while os.path.exists(graph_path):
    i += 1
    graph_path = GRAPH_DIRECTORY + f'graph_{i}.graphml'

nx.write_graphml(G, graph_path)
print(f'Graph saved at {graph_path}')