import collections
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        #根据有几门课的数量在图中建几个点
        graph = [[] for _ in range(numCourses)]
        #并统计每门课的入度
        in_degree = [0] * numCourses
        
        #建图
        #根据依赖关系建图，
        #这里边有个地方需要注意明白，这里是用adjacency list建图
        #这里的node_out 代表学的具体课程 like 0, 1, 2 是graph的index
        #这个graph的label是 node_in, 表示下一个要学的课程（也是neighbor)
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in] += 1 

        #define 需要学习的课程    
        num_choose = 0 
        # 建queue
        queue = collections.deque()
       
        #put all nodes which have in_degree 0 in queue
        # 将入度为 0的点放入队列中学习掉,入度为0的点表示可以学习的课程
        #它没有prerequisite的要求
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # 对queue进行循环
        while  queue:
            node = queue.popleft()
            #当从queue中跳出来，表示这门课学完了，所以 num_chose + 1
            num_choose += 1 
            
            #相应这个点所对应的邻居也就是边要去掉了
            for neighbor in graph[node]:
                #这个边的in_degree -1，因为课学完了，没有依赖关系了
                in_degree[neighbor] -= 1 
                #如果课程1 的in_degree 变为0，课程一也可以学习了，没有prerequisite了
                #放入队列去学习
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        #最后判断学习的课程是不是等于已有课程数
        return num_choose == numCourses
if __name__ == '__main__':
    ll = Solution()
    # n = 2
    # prerequisites =  [[1,0]] 
    n = 3
    prerequisites = [[1,0], [2, 1]]
    x = ll.canFinish(n, prerequisites)
    print(x)


