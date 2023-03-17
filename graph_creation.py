import pandas as pd
import networkx as nx
import numpy as np

# This file generates a graph from the answers to different stories.

ANSWERS_TYPE_C_PATH = './data/Answers_to_Microstories/answers_stories_C.pkl'
SOCIODEMOGRAPHIC_DATA_PATH = './data/Sociodemographic_survey/answers_sociodemographic_survey.pkl'
N_PA = 50

# load data
df_C = pd.read_pickle(ANSWERS_TYPE_C_PATH)
df_sociodem = pd.read_pickle(SOCIODEMOGRAPHIC_DATA_PATH)

# preprocess answers dataframe 
df_C.columns = df_C.columns.swaplevel(0, 1)
df_C_yo = df_C.yo_final
# for the moment, we only work with "yo" answers
# df_C_otro = df_C.otro_final

# Get only stories with more than N_PA answers and drop rows that cotanin null values
subset_df = df_C_yo.loc[:, df_C_yo.count() > N_PA]
subset_df = subset_df.dropna(how='any')


