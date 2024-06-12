from collections import deque
import collections
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.append(end)

        queue = collections.deque([start])
        visited = set([start])

        distance = 0 

        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()

                if word == end:
                    return distance


                for next_word in self.get_next_words(word, dict):
                    if next_word not in dict or next_word in visited:
                        continue 
                    queue.append(next_word)
                    visited.add(next_word)
        return 0 

     
    def get_next_words(self, word, dict):
        words = []

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words
if __name__ =='__main__':
    solution = Solution()
    start ="hit"
    end = "cog"
    dict =["hot","dot","dog","lot","log"]
    x = solution.ladderLength(start, end, dict)
    y = print(x)
