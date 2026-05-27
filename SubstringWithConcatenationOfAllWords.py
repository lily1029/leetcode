# 导入 Counter，用于统计单词出现次数
from collections import Counter  

class Solution:
    def findSubstring(self, s, words):
        # 如果 s 或 words 为空，直接返回空列表
        if not s or not words:  
            return []
        
        # 每个单词的长度（所有单词等长）
        w = len(words[0]) 
        # words 里单词的总个数       
        k = len(words)  
        # 字符串 s 的总长度        
        n = len(s) 
        # 统计 words 里每个单词出现几次
        # 例如 ["foo","bar","foo"] → {"foo":2, "bar":1}             
        word_count = Counter(words)  
        # 存放所有合法起始索引                             
        result = []             

        # 以 w 为偏移起点，分成 w 组滑动窗口
        # 例如 w=3，就分 start=0, 1, 2 三组
        # 这样能覆盖所有可能的起始位置
        for start in range(w):
            # 窗口左边界，初始化为当前组的起点
            left = start 
            # 当前窗口内「有效匹配」的单词个数        
            count = 0  
            # 当前窗口内每个单词出现的次数          
            window = {}          

            # right 每次移动一个单词长度 w，从 start 开始到字符串末尾
            for right in range(start, n - w + 1, w):
                # 从 right 位置取出长度为 w 的单词
                word = s[right:right + w]  

                # 判断这个单词是否是 words 里的有效单词
                if word in word_count:   
                    # 把这个单词加入窗口计数  
                    window[word] = window.get(word, 0) + 1 
                    # 有效单词个数 +1 
                    count += 1             

                    # 如果窗口内某个单词出现次数超过了 words 里的次数
                    # 就需要从左边界开始缩小窗口
                    while window[word] > word_count[word]:
                        # 取出左边界的单词
                        left_word = s[left:left + w] 
                        # 把左边界单词从窗口移除 
                        window[left_word] -= 1  
                        # 有效单词个数 -1       
                        count -= 1     
                         # 左边界向右移动一个单词                
                        left += w                     

                    # 如果当前窗口内有效单词个数等于 k，说明找到一个合法窗口
                    if count == k:
                        # 记录左边界为合法起始索引
                        result.append(left)            

                        # 移动左边界，继续寻找下一个合法窗口
                        # 取出左边界的单词
                        left_word = s[left:left + w] 
                        # 把左边界单词从窗口移除  
                        window[left_word] -= 1 
                        # 有效单词个数 -1         
                        count -= 1 
                        # 左边界向右移动一个单词                     
                        left += w                       

                else:
                    # 遇到无效单词（不在 words 里），当前窗口作废
                    # 清空窗口计数
                    window.clear()   
                    # 有效单词个数归零
                    count = 0  
                    # 左边界跳到无效单词的下一个位置，重新开始      
                    left = right + w 
        # 返回所有合法起始索引
        return result  

if __name__ == '__main__':
    ll = Solution()
    # 测试用例 1，预期输出 [0, 9]
    print(ll.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    # 测试用例 2，预期输出 []
    print(ll.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
    # 测试用例 3，预期输出 [6, 9, 12]
    print(ll.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))