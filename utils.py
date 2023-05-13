import networkx as nx
import numpy as np
import pandas as pd

# Custom library with some useful functions realted to the graph
COLORS = { "pp"    : {"Sí":'#d7191c', "No":'#2c7bb6', "nvr":'#ffffbf'}, 
           "p_cuid": {"Sí":'#d7191c', "No":'#2c7bb6', "nvr":'#ffffbf'},
           "genere": {"m":"#2c7bb6", "f":"#d7191c", "d":"#fdae61", "nvr":"#abd9e9"},
           "edat"  : {'1':"#d73027", '2':"#fc8d59", '3':"#fee090", '4':"#e0f3f8", '5':"#91bfdb", '6':"#4575b4", 'nvr':"gray"},
           "age_bracket": {"old": "#2c7bb6", "young": "#d7191c", 'nvr':"gray"}
      }

def color_coding(
        G: nx.graph,
        sociodem_df: pd.DataFrame,
        sociodem_entry: str,
        colors_dict: dict = COLORS
        ) -> list:
    """
    For each node in graph G, maps a specified attribute to a color.

    Args:
        - G: networkx graph that we want to color   
        - sociodem_df: dataframe containing sociodemographic info
        - sociodem_entry: key of the attribute that we want to color. Possible values: sociodem_df.keys()
        - colors_dict: dictionary which maps each sociodem_entry attribute to a color (see top)
    
    Returns:
        - color_map: list which contains the nodes colors ordered by graph node order
     """

    color_map = [colors_dict[sociodem_entry][sociodem_df[sociodem_entry].loc[node]] for node in G]

    return color_map


def one_pair_weight_for_one_story(
        ans1: str,
        ans2: str,
        alpha: float = 1.,
        beta: float = 2/3,
        gamma: float = 1/3
        ) -> float:
    """
    Computes one edge weigth among two nodes for a single story.
    The weight can be:
        - alpha if ans1 = 'A' and ans2 = 'A'
        - beta if (alpha if ans1 = 'A' and ans2 = 'B') or (alpha if ans1 = 'B' and ans2 = 'A')
        - gamma if ans1 = 'B' and ans2 = 'B'
        - 0 if ans1 = 'C' or ans2 = 'C'

    Args:
        ans1: Answer from node 1. Possible values are 'A', 'B' or 'C'
        ans2: Answer from node 2. Possible values are 'A', 'B' or 'C'
        alpha: Weight value when both answers are 'A'
        beta: Weight value when one answer is 'A' and the other is 'B'
        gamma: Weight value when both answers are 'B' 
    
    Returns:
        value: The edge weight for the given pair
    """

    value = 0
    if ans1 == 'A':
        if ans2 == 'A':
            value = alpha
        elif ans2 == 'B':
            value = beta
    elif ans1 == 'B':
        if ans2 == 'A':
            value = beta
        elif ans2 == 'B':
            value = gamma
    
    return value

def edge_weight(
        df: pd.DataFrame,
        pair: tuple,
        stories: list
    ) -> tuple:
    """
    Compute the average weight among some stories for an edge connecting two nodes.

    Args:
        - df: Pandas dataframe containing all nodes information
        - pair: the pair of nodes. (id1, id2)
        - stories: list containing the stories from which the average will be done
    
    Returns:
        - edge_value: the average edge weight among all stories
    """

    value_list = [one_pair_weight_for_one_story(df[story][pair[0]], df[story][pair[1]]) 
                  for story in stories]
    edge_value = np.mean(value_list)

    return edge_value 

def young_old(age_bracket: str) -> str:
    """
    Given an age interval, it returns classifies it as young or old.

    Args:
        - age_bracket: str with the indicator of the age interval given by de datset. I.e: '1' indicates interval '25-35'

    Returns:
        - 'young': if the age_bracket is '18-24', '25-34' or '35-44'
        - 'old': if the age_bracket is '45-54', '55-64' or '65+'
        - 'nay': if the user did not want to give his age information

    """
    if age_bracket in ["1", "2", "3"]:
        return "young"
    elif age_bracket in ["4", "5", "6"]: 
        return "old"
    else: 
        return "nay"
