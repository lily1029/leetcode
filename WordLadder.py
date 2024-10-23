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
        #we put end in dict in order to compare with start
        dict.append(end)

        #put the first word start in queue
        queue = collections.deque([start])
        #as long as we put it in queue, we set it as a visited node
        #we use a set to keep track
        visited = set([start])

        #set variable as a distance,这里是所求的结果
        distance = 0 

        #go through the queue, while queue is not empty 
        while queue:
            distance += 1
            #go through the queue
            for i in range(len(queue)):
                #pop out the word and compare it with end, 
                #if equal, return distance
                word = queue.popleft()

                if word == end:
                    return distance

                #if word != end, we look for the next words which is one bit different
                #from the word, actually we list all the words and check whether it is 
                #appear in dict or not 
                for next_word in self.get_next_words(word, dict):
                    if next_word not in dict or next_word in visited:
                        continue 
                    queue.append(next_word)
                    visited.add(next_word)
        return 0 

    # O(26 * L^2)
    # L is the length of word 
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
