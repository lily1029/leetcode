import collections


class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        root = node 
        
        if not node:
            return node 
        
        nodes = self.getNodes(node)
        
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        
        
        
        #copy all the deges
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        return mapping[root]
       
        
    #get all nodes
    def getNodes(self, node):
        queue = collections.deque([node])
        visited = set()
        
        while queue:
            head = queue.popleft()
            visited.add(head)
            
            for head in head.neighbors:
                if head not in visited:
                    visited.add(head)
                    queue.append(head)
        return visited

# Example usage
if __name__ == '__main__':
    # Create nodes
    ll1 = UndirectedGraphNode(1)
    ll2 = UndirectedGraphNode(2)
    ll3 = UndirectedGraphNode(3)

    # Set neighbors
    ll1.neighbors = [ll2, ll3]
    ll2.neighbors = [ll1, ll3]
    ll3.neighbors = [ll1, ll2]

    # Initialize the solution and clone the graph
    solution = Solution()
    cloned_graph = solution.cloneGraph(ll1)

    # Print the label of the cloned graph's root node to verify
    print(f"Cloned node label: {cloned_graph.label}")
    for neighbor in cloned_graph.neighbors:
        print(f"Neighbor of cloned node: {neighbor.label}")
