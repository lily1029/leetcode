class Solution:
    #此题的做法就是用hashmap统计重新排序后的这个单词出现的次数
    def anagrams(self, strs):
        hashmap = {}
        result = []
        
        #go throug the input
        for string in strs:
            # e.g: lint  sorted to ilnt
            string = ''.join(sorted(string))
            # hashmap: {'ilnt': 3, 'cdeo' : 1}
            hashmap[string] = hashmap.get(string, 0) + 1 

        #go through the origin str    
        for string in strs:
            #把每一个单词sort 一次，并join后
            sortedstring = ''.join(sorted(string))
            #查看这个单词是否在哈希表里出现过大于一次，然后放入结果中
            if sortedstring in hashmap and hashmap[sortedstring] > 1:
                #result: ['lint', 'intl', 'inlt']
                result.append(string)

        return result
if __name__ == '__main__':
    ll = Solution()
    strs = ["lint", "intl", "inlt", "code"]
    x = ll.anagrams(strs)
    print(x)


