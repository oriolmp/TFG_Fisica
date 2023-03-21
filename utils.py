import networkx as nx
import numpy as np
import pandas as pd

# Custom library with some useful functions realted to the graph

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
