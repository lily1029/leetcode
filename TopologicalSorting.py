
import collections
import networkx as nx
#Definition for a Directed graph node

class DirectedGraphNode1:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class DirectedGraphNode2:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class DirectedGraphNode3:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class DirectedGraphNode4:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class DirectedGraphNode5:
    def __init__(self, x):
        self.label = x
        self.neighbors = []




import collections


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def get_indegree(self, graph):
        
        indegrees = {node : 0 for node in graph}
        
        for node in graph:
            for neighbor in node.neighbors:
                indegrees[neighbor] += 1 
        return indegrees

    def topSort(self, graph):
        # write your code here
        indegrees = self.get_indegree(graph)
        
        queue = collections.deque([node 
                                   for node in graph 
                                   if indegrees[node] == 0
                                  ])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            
            for neighbor in node.neighbors:
                indegrees[neighbor]  -= 1 
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return topo_order
if __name__ == '__main__':
    # Create nodes
    graph = nx.DiGraph()
    graph.add_edges_from([("A", "B"), ("A", "D"), ("B", "D"), ("B", "C"), ("D", "E")])
    print(graph.in_edges("E"))  # => [('a', 'e'), ('d', 'e')]

    ll1 = DirectedGraphNode3(1)
    ll1.label = 'C'
    ll1.neighbors = []

    ll2 = DirectedGraphNode5(2)
    ll2.label = 'E'
    ll2.neighbors = []

    ll3 = DirectedGraphNode4(3)
    ll3.label = 'D'
    ll3.neighbors = [ll2]

    ll4 = DirectedGraphNode2(4)
    ll4.label = 'B'
    ll4.neighbors = [ll1, ll3]


    ll5 = DirectedGraphNode1(5)
    ll5.label = 'A'
    ll5.neighbors  = [ll4, ll3]
    
    solution = Solution()
    x = solution.topSort(graph)
    print(x)




    