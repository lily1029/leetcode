#使用 append + pop 的方式
class Solution:

    def partition(self, s):
        #results 存最终的结果
        results = []
        #这里只能进行dfs先是一个一个字母的切，当切一个字母时，对剩下的
        #string进行同样的dfs操作，这里是string 长度为1的sub string
        #然后进行一次切2个字母的字符串，重复上面的操作
        #然后进行一次切3个字母的字符串，同上操作，直到切到整个string的长度
        self.dfs(s, [], results)
        
        return results
    
    #定义dfs() stringlist: 相当于一个短期存的list 
    def dfs(self, s, stringlist, results):
        #当len(s)==0时，说明该切割的字符串已经都出去了
        #如果有palindrome,we put it in results,then,return 
        if len(s) == 0:
            results.append(list(stringlist))
            return
        
        #从这里切割s,s切割字符串长度为依次1，2，3从1 开始   
        for i in range(1, len(s) + 1):
            #切下来的sub string 放到prefix里
            prefix = s[:i]
            #判断它是否是palindrome,如果是，会放入stringlist中
            if self.is_palindrome(prefix):
                stringlist.append(prefix)
                #然后在切掉这个字符的剩下字符串中进行DFS
                self.dfs(s[i:], stringlist, results)
                #DFS之后出栈
                stringlist.pop()
    
    #判断它是否是palindrome,看它的反串是否和原串相等
    def is_palindrome(self, s):
        return s == s[::-1]
if __name__ == '__main__':
    ll = Solution()
    s = "aab"

    x = ll.partition(s)
    print(x)
 




