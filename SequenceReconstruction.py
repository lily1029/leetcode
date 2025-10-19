class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        #这里build graph根据seqs的依赖关系
        graph = self.build_graph(seqs)
        #根据build 好的graph进行topological sort(BFS算法)
        topo_order = self.topological_sort(graph)
        #最后topo_order 为none org:[1, 2, 3], 所以返回false, test1 data
        return topo_order == org 

    #这里要先通过依赖关系把图建好        
    def build_graph(self, seqs):
        #initialize graph 这里的graph我们用一个hashmap. key是每个节点，value是一个set,
        #set里的值是key的依赖关系e.g: graph: {1: {2, 3}} 要先学完1，才能学2或是3, test1 data
        #这里代码完后得到这个：graph: {1: {}, 2: {}, 3: {}}
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
        
        #将建好的图中放入依赖关系的边
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph
    
    #建好图后，因为是有向图，统计每个点的入度
    #indegrees: {1: 0, 2: 0, 3: 0}
    def get_indegrees(self, graph):
        indegrees = {
            node: 0
            for node in graph
        }
        
        #得到具体的indegrees: {1:0, 2:1, 3:2} test 2 data
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
                
        return indegrees

    #建好的图有，而且知道每个点的入度，这时进行topological sort   
    def topological_sort(self, graph):
        #当做topological sort时第一步时统计图中的入度(indegrees)
        indegrees = self.get_indegrees(graph)

        #用queue做topological sorting, 将入度为0的点放入queue
        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
        
        topo_order = []
        while queue:
            #如果queue的size 大于1，说明不止一条topological sort orders, return false
            if len(queue) > 1:
                # there must exist more than one topo orders
                return None

            #bfs    
            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(topo_order) == len(graph):
            return topo_order
            
        return None
    
if __name__ =='__main__':
    soultion = Solution()
    #test 1
    org = [1,2,3]
    seqs = [[1,2],[1,3]]
    x = soultion.sequenceReconstruction(org, seqs)
    y = print(x)

    #test 2
    # org = [1,2,3]
    # seqs = [[1,2],[1,3],[2,3]]
    # x = soultion.sequenceReconstruction(org, seqs)
    # y = print(x)

        







