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
        #root是clone graph新图的根结点，copy原图的根结点node
        root = node 
        
        #如果此根结点为空，就返回这个点（node)就行了
        if not node:
            return node 
        
        #这里use bfs algorithm to traverse the graph and get
        #all nodes,这些只是原图的结点，并没有边
        nodes = self.getNodes(node)
        
        #这里复制所有的点，并把映射关系存下来： old --> new
        #copy nodes {old node: new node}
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label) 
        
        #copy all the deges
        #copy neighbors(edges),这里复制所有的边，copy边的时候，for
        #循环所有的点，然后又for循环每个点的邻居
        for node in nodes:
            new_node = mapping[node]
            #The neighbors attribute is typically a list of nodes
            #that are directly connected to the current node
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                #将mapping的新边放入new_node的neighbors,从而达到复制边
                new_node.neighbors.append(new_neighbor)
        return mapping[root]
         
    #get all nodes
    #bfs algorithm
    def getNodes(self, node):
        #初始化一个queue
        queue = collections.deque([node])
        visited = set()
        
        #循环这个queue
        while queue:
            node = queue.popleft()
            visited.add(node)
            
            for node in node.neighbors:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
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
