
class DirectedGraphNode:
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
    