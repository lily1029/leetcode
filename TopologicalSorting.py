import collections
# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    
    def topSort(self, graph):
        # write your code here
        # 这里统计图中所有点的入度，这里是有向图
        node_to_indegree = self.get_indegree(graph)

        # bfs begins here
        # we use order to store the result topological sorting order
        order = []

        # we put all nodes which have in-degree = 0 here in start_nodes
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]

        # put all start_nodes in queue which the in-degree = 0
        queue = collections.deque(start_nodes)
        # go through the queue and pop out the first one and append to order list
        while queue:
            node = queue.popleft()
            order.append(node)
            # then we go through this node's all neighbours, because this node is               
            # been poped out, so all this node 's neighbours' in-degree should - 1                  
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                # if this node 's neighbor node in-degree = 0, it should put it in queue            
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order 


    def get_indegree(self, graph):
        # we use a hashmap to record each node 's in-degree
        # for x in graph , here x means each node in graph
        # graph = [0, 1, 2, 3, 4, 5], after go through all nodess in graph
        # {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        node_to_indegree = {x: 0 for x in graph}

        # we go through each node in the graph
        for node in graph:
            # we go through each node 's neighbours
            for neighbor in node.neighbors:
                # in the hashmap, the key is neighbor (node), if this node
                # has a neighbor , this neighbor 's in-degree should + 1
                node_to_indegree[neighbor] += 1

        # after this above for loop, we can get all nodes' in-degree, and 
        # we return  to the beginning in order to execute the rest code
        return node_to_indegree

if __name__ == '__main__':
    # Create nodes
    node0 = DirectedGraphNode('0')
    node1 = DirectedGraphNode('1')
    node2 = DirectedGraphNode('2')
    node3 = DirectedGraphNode('3')
    node4 = DirectedGraphNode('4')
    node5 = DirectedGraphNode('5')

    # Define neighbors
    node0.neighbors = [node1, node2, node3]
    node1.neighbors = [node4]
    node2.neighbors = [node4, node5]
    node3.neighbors = [node4, node5]

    # Create graph
    graph = [node0, node1, node2, node3, node4, node5]

    # Perform topological sort
    solution = Solution()
    topo_order = solution.topSort(graph)
    print(topo_order)



