from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        #Hashmap, count each characters
        #s = "aab" count: Counter({'a':2, 'b':1})
        count = Counter(s)

        # this is just a list e.g [[-3, 'a'], [-1, 'b'], [-1, 'c']]
        maxHeap = [[-cnt, char] for char, cnt in count.items()]

        # here turn the list to maxHeap, here use minus, it is minHeap
        heapq.heapify(maxHeap)

        #store the previous character temporarily
        prev = None

        # the string we try to build
        res = ""

        #either the condition is true, can continue
        while maxHeap or prev:
            #corner case, 
            #prev is not none and maxHeap is empty
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char 
            cnt += 1

            #if the prev is not None, we push back 
            # the prev to maxHeap in order to pop
            if prev:
                heapq.heappush(maxHeap, prev)
                #当prev被push到maxHeap后，prev设置为None
                prev = None
            
            #if the cun != 0, we put them in prev
            if cnt != 0:
                prev = [cnt, char]
        
        #return result
        return res
        


if __name__ == '__main__':
    # Example usage:
    ll = Solution()
    #s = "aab"
    s = "aaabc"
    x = ll.reorganizeString(s)
    print(x)