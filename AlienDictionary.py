from heapq import heappush, heappop, heapify
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # first, we need to build a graph
        # we use a method to build a graph
        graph = self.build_graph(words)
        graph = self.build_graph(words)
        
        # if the graph is empty, return ""
        if not graph:
            return ""
        # finally, we return topological sort of this graph
        return self.topological_sort(graph)
    
    
    # here, we build a graph, the input is a list of words
    def build_graph(self, words):
        # key is node, value is neighbors(next word in Alien lexicographically order)
        # we use a hashmap to store
        graph = {}

        # initialize graph
        # go through each word one by one in words list
        for word in words:
            # go through each word's character one by one to compare in two neighbouring words
            for c in word:
                # if this character is not in graph dictionary, put it in, the key is each character
                # the value is we set up a set in order not to have the repeated characters
                if c not in graph:
                    graph[c] = set()

        # add edges
        # get the number of different words in words list
        n = len(words)
        # go through each word
        for i in range(n - 1):
            # compare two neighbouring words 's fist character to see it is same or not
            for j in range(min(len(words[i]), len(words[i + 1]))):
                # if two neighbour words the same position's characters are not same
                if words[i][j] != words[i + 1][j]:
                    # we put the next neighbour words[i + 1][j] into words[i][j]] 's set to build up an edge
                    graph[words[i][j]].add(words[i + 1][j])
                    # if they are equal, skip the rest of codes
                    break
                if j == min(len(words[i]), len(words[i + 1])) - 1:
                    if len(words[i]) > len(words[i + 1]):
                        return None

        return graph

    def topological_sort(self, graph):
        # initialize indegree
        # initialize all nodes ' in-degree
        # after this code, we have
        # indegree = {w: 0, r: 0, t: 0, f: 0, e: 0}
        indegree = {
            node: 0
            for node in graph
        }

        # calculate indegree
        # here we calculate indegree, eg, first node is 'w'
        # graph[w] = {e} , so , the neighbor is 'e', so ,
        # e's in-degree + 1 cuzz w ---> e
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] = indegree[neighbor] + 1

        # use heapq instead of regular queue so that we can get the
        # smallest lexicographical order
        # find the indegree = 0 's node go into the queue
        queue = [node for node in graph if indegree[node] == 0]
        heapify(queue)

        # regular bfs algorithm to do topological sorting
        topo_order = ""
        while queue:
            node = heappop(queue)
            topo_order += node
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(queue, neighbor)

        # if all nodes popped
        if len(topo_order) == len(graph):
            return topo_order

        return ""
    
if __name__ =='__main__':
    ll = Solution()
    words = ["wrt","wrf","er","ett","rftt"]
    x = ll.alienOrder(words)
    print(x)
