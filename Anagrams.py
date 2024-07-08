class Solution:

    def anagrams(self, strs):
        hashmap = {}
        result = []
        
        for string in strs:
            string = ''.join(sorted(string))
            hashmap[string] = hashmap.get(string, 0) + 1 
            
        for string in strs:
            sortedstring = ''.join(sorted(string))
            if sortedstring in hashmap and hashmap[sortedstring] > 1:
                result.append(string)
        return result
if __name__ == '__main__':
    ll = Solution()
    strs = ["lint", "intl", "inlt", "code"]
    x = ll.anagrams(strs)
    print(x)
