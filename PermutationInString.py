class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def checkInclusion(self, s1, s2):
        # write your code here
        
        target = s1 
        source = s2 
        
        if len(target) > len(source):
            
            return False 
            
        target_hash = {} 
        source_hash = {}
        
        for i in range(len(target)):
            #这里计算每个字母在target长度里在hash里出现的次数
            target_hash[target[i]] = target_hash.get(target[i], 0) + 1 
            source_hash[source[i]] = source_hash.get(source[i], 0) + 1 
            
        if target_hash == source_hash:
            
            return True 

        #这里是sliding window 滑的范围    
        for window_start in range(1, len(source) - len(target) + 1):
            #here we get sliding window end position
            window_end = window_start + len(target) - 1 
            #here we can get sliding window end position in source position as a key in source_hash value
            source_hash[source[window_end]] = source_hash.get(source[window_end], 0) + 1 
            #此时sliding window_start 的前一位对应的source_hash里的value值减1
            source_hash[source[window_start - 1]] -= 1 
            
            #当前一位对应的value=0时，我们delete这个前一值，因为我们只search和target一样长度的substring
            if source_hash[source[window_start - 1]] == 0: 
                del source_hash[source[window_start - 1]]
            #当source_hash 和 target_hash的值完全一样时，target一定在source里   
            if source_hash == target_hash:
                
                return True 
                
        return False
if __name__ == '__main__':
    ll = Solution()
    s1 = "ab" 
    s2 = "eidbaooo"
    x = ll.checkInclusion(s1, s2)
    print(x)

