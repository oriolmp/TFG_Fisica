"""Node assortativity coefficients and correlation measures.
"""
from networkx.algorithms.assortativity.pairs import node_degree_xy

__all__ = [
    "degree_pearson_correlation_coefficient",
    "degree_assortativity_coefficient",
    "attribute_assortativity_coefficient",
    "numeric_assortativity_coefficient",
]


def node_attribute_xy(G, attribute, nodes=None):
    """Returns iterator of node-attribute pairs for all edges in G, with the weight of the edge connecting them.

    Parameters
    ----------
    G: NetworkX graph

    attribute: key
       The node attribute key.

    nodes: list or iterable (optional)
        Use only edges that are incident to specified nodes.
        The default is all nodes.

    Returns
    -------
    (x, y, z): 2-tuple
        Generates 2-tuple of (attribute, attribute, weight) values.

    Examples
    --------
    >>> G = nx.DiGraph()
    >>> G.add_node(1, color="red")
    >>> G.add_node(2, color="blue")
    >>> G.add_edge(1, 2)
    >>> weight = 0.1
    >>> G.add_weighted_edges_from(list((1, n, weight) for n in G.nodes))
    >>> list(nx.node_attribute_xy(G, "color"))
    [('red', 'blue', 0.1)]

    Notes
    -----
    For undirected graphs each edge is produced twice, once for each edge
    representation (u, v) and (v, u), with the exception of self-loop edges
    which only appear once.
    """
    if nodes is None:
        nodes = set(G)
    else:
        nodes = set(nodes)
    Gnodes = G.nodes
    for u, nbrsdict in G.adjacency():
        if u not in nodes:
            continue
        uattr = Gnodes[u].get(attribute, None)
        if G.is_multigraph():
            for v, keys in nbrsdict.items():
                vattr = Gnodes[v].get(attribute, None)
                for _ in keys:
                    yield (uattr, vattr)
        else:
            for v, w in nbrsdict.items():
                vattr = Gnodes[v].get(attribute, None)
                uvweight = w['weight']
                yield (uattr, vattr, uvweight)



def attribute_assortativity_coefficient(G, attribute, nodes=None):
    """Compute assortativity for node attributes.

    Assortativity measures the similarity of connections
    in the graph with respect to the given attribute.

    Parameters
    ----------
    G : NetworkX graph

    attribute : string
        Node attribute key

    nodes: list or iterable (optional)
        Compute attribute assortativity for nodes in container.
        The default is all nodes.

    Returns
    -------
    r: float
       Assortativity of graph for given attribute

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_nodes_from([0, 1], color="red")
    >>> G.add_nodes_from([2, 3], color="blue")
    >>> G.add_edges_from([(0, 1), (2, 3)])
    >>> print(nx.attribute_assortativity_coefficient(G, "color"))
    1.0

    Notes
    -----
    This computes Eq. (2) in Ref. [1]_ , (trace(M)-sum(M^2))/(1-sum(M^2)),
    where M is the joint probability distribution (mixing matrix)
    of the specified attribute.

    References
    ----------
    .. [1] M. E. J. Newman, Mixing patterns in networks,
       Physical Review E, 67 026126, 2003
    """
    M = attribute_mixing_matrix(G, attribute, nodes)
    return attribute_ac(M)

