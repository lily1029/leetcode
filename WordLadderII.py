from collections import deque 

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    #从 end 到 start 做一次 BFS，并且把所有点到 end 的距离都保存在 distance 中。
    #然后在从 start 到 end 做一次 DFS，每走一步必须确保离 end 的 distance 越来越近。
    def findLadders(self, start, end, dict):

        dict.append(start)
        dict.append(end)
        distance = {}

        self.bfs(end, distance, dict)
        results = []
        self.dfs(start, end, distance, dict, [start], results )
        return results

    #bfs algorithm 从end到start, 普通版本bfs  
    def bfs(self, start, distance, dict):
        distance[start] = 0 
        queue = deque([start])

        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1 
                    queue.append(next_word)
      
    
    #找到符合条件的下一个单词
    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words 
    
    #从start 点到end点左dfs,并确保和end离的越来越近                   
    def dfs(self, curt, target, distance, dict, path, results):
        if curt == target:
            results.append(list(path))
            return 
        
        for word in self.get_next_words(curt, dict):
            if distance[word] != distance[curt] - 1:
                continue 
            path.append(word)
            self.dfs(word, target, distance, dict, path, results)
            path.pop()

if __name__ == '__main__':
    ll = Solution()
    start ="hit"
    end = "cog"
    dict =["hot","dot","dog","lot","log"]
    x = ll.findLadders(start, end, dict)
    print(x)


