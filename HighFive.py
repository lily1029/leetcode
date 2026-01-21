#利用map，找到对应的人的成绩，然后暴力比较出前5个。

#Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        #初始化一个哈希表
        hash = dict()
        #用for循环go through 整个成绩表
        for r in results:
            #如果这个学生的id不再哈希表里，要放进去
            if r.id not in hash:
                hash[r.id] = []

            #如果这个学生的id已经在哈希表中，把他成绩放进去
            hash[r.id].append(r.score)
            #当这个学生的成绩数超过5门
            if len(hash[r.id]) > 5:
                #把第一门成绩设为index = 0
                index = 0
                #for循环剩下的从index = 1 到5
                for i in range(1, 6):
                    #如过index = i 的成绩小于index 的成绩
                    if hash[r.id][i] < hash[r.id][index]:
                        #index 换成 i 
                        index = i
                
                #for循环结束后，pop（）出这个index的值
                hash[r.id].pop(index)
        
        #初始化一个新的字典存answer
        answer = dict()
        #用for循环 go through 每个学生的平均成绩
        for id, scores in hash.items():
            answer[id] = sum(scores) / 5.0

        return answer


if __name__ == '__main__':
    ll = Solution()
    results = [
        Record(1,91), Record(1,92), Record(2,93), Record(2,99),
        Record(2,98), Record(2,97), Record(1,60), Record(1,58),
        Record(2,100), Record(1,61), Record(1, 62)
    ]
    x = ll.highFive(results)
    print(x)

   



