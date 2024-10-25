import collections
#Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
   
    def searchNode(self, graph, values, node, target):
        #如果图为空，返回none
        if not graph or not values:
            return None
        
        #将最开始给的初始点放入q中
        q = collections.deque([node])
        #这里要用set可以避免重复的点在次放入q中
        Set = set([node])

        #这里go through这个q,检查q中第一个点是不是等于target
        #如果等于，返回这个点，否则遍历这个点的所有边(邻居)，只要还不在
        #set里就放入q里，放入set里，pop出不符合条件的node, 继续
        #go through剩下的nodes在q里，直到找到满足条件的，这里
        #用的也是toplogical sort,这个过程找到的是最近的点
        while q:
            #找到结果
            if values[int(q[0].label) - 1] == target:
                return q[0]
            
            #遍历每个点的所有边
            for neighbor in q[0].neighbors:
                #如果此点不在set中，放入q和set中，继续遍历
                if neighbor not in Set:
                    q.append(neighbor)
                    Set.add(neighbor)
            #pop出不符合条件的node
            q.popleft()
        return None
if __name__ == '__main__':
    # Create nodes
    node1 = UndirectedGraphNode('1')
    node2 = UndirectedGraphNode('2')
    node3 = UndirectedGraphNode('3')
    node4 = UndirectedGraphNode('4')
    node5 = UndirectedGraphNode('5')

    # Define neighbors
    node1.neighbors = [node2, node3, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2]
    node4.neighbors = [node1, node5]
    node5.neighbors = [node4]

    # Create graph
    graph = [node1, node2, node3, node4, node5]
    values = [3,4,10,50,50]
    node = node1
    target = 50

    # Perform topological sort
    solution = Solution()
    x = solution.searchNode(graph, values, node, target)
    print(x.label)
