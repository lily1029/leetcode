class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        #用hash记录{2: 0, 7: 1, 11: 2, 15: 3}
        hash = {}

        #这里i 是它的index， num 是真实的数
        for i, num in enumerate(numbers):
            if target - num in hash:
                return [hash[target - num], i]
            hash[num] = i
if __name__ == '__main__':
    ll = Solution()
    numbers = [2, 7, 11, 15]
    target = 13
    x = ll.twoSum(numbers, target)
    print(x)