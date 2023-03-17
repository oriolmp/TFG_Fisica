import networkx as nx
import numpy as np

# Custom library with some useful functions realted to the graph

def weight(
        ans1: str,
        ans2: str,
        alpha: float = 1.,
        beta: float = 2/3,
        gamma: float = 1/3
        ):
    """
    Computes the edge weigth among two nodes.

    Args:
        ans1: Answer from node 1. Possible values are 'A', 'B' or 'C'
        ans2: Answer from node 2. Possible values are 'A', 'B' or 'C'
        alpha: Weight value when both answers are 'A'
        beta: Weight value when one answer is 'A' and the other is 'B'
        gamma: Weight value when both answers are 'B' 
    
    Returns:
        weight: The edge weight
    """

    weight = 0
    if ans1 == 'A':
        if ans2 == 'A':
            weight = alpha
        elif ans2 == 'B':
            weight = beta
    elif ans1 == 'B':
        if ans2 == 'A':
            weight = beta
        elif ans2 == 'B':
            weight = gamma
    
    return weight
