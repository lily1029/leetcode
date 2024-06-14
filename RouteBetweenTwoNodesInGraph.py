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


class Solution:
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        queue = collections.deque([s])
        visited = set()
        visited.add(s)

        while queue:
            node = queue.popleft()
            if node == t:
                return True
            for neighbor in node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return False
if __name__ == '__main__':
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


    ll = Solution()
    x = ll.hasRoute(graph, ll4, ll2)
    print(x)