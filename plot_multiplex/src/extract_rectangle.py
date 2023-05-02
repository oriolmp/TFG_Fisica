import pandas as pd
import numpy as np

def extract_stories_dfs_answered_by_all_of_N_pa_participants(df_C_yo, df_C_otro, list_of_C_stories, N_pa = 50, randomize=False):
    """
    extract stories that were answered by all participants of a fixed subset of participants
    
    N_pa ::Number of participant that answered the story (at least)
    """
    print(df_C_yo.count()[df_C_yo.count()>=N_pa].index)

    # list of stories with more than N_pa answers
    """df_num_answered_C_wo_id = df_num_answered_C.set_index("index")
    list_stories_mt_Npa = df_num_answered_C_wo_id.index[df_num_answered_C_wo_id["answered"]>=N_pa]"""
    list_stories_mt_Npa = list(df_C_yo.count()[df_C_yo.count()>=N_pa].index)
    n_stories = len(list_stories_mt_Npa)
    # extract only particpants that answered ALL these stories
    sub_df_these_stories_yo   = df_C_yo[list_stories_mt_Npa].dropna()
    sub_df_these_stories_otro = df_C_otro[list_stories_mt_Npa].dropna() # logic: stories that have answer yo, necessarily have answer otro
    if randomize==True:
        for row in sub_df_these_stories_yo.index:
            for column in sub_df_these_stories_yo.columns:
                if not sub_df_these_stories_yo.loc[row, column] =="nay":
                    sub_df_these_stories_yo.loc[row, column] = random.choice(("A", "B", "C"))
        for row in sub_df_these_stories_otro.index:
            for column in sub_df_these_stories_otro.columns:
                if not sub_df_these_stories_otro.loc[row, column] =="nay":
                    sub_df_these_stories_otro.loc[row, column] = random.choice(("A", "B", "C"))
    return sub_df_these_stories_yo, sub_df_these_stories_otro, n_stories, list_stories_mt_Npa
