class Solution(object):
    '''
    题意：找到数列中所有和等于目标数的四元组，需去重
    多枚举一个数后，参照3Sum的做法，O(N^3)    
    '''
    def fourSum(self, nums, target):

        # we sort nums first 
        nums.sort()
        # we use res to store final results in res 
        res = []
        # get length of nums
        length = len(nums)

        # go through the first number a 
        for i in range(0, length - 3):
            # here 去重
            if i and nums[i] == nums[i - 1]:
                continue

            # go through the second number b starting i + 1 
            for j in range(i + 1, length - 2):
                # 正常情况 j = i + 1, 但是如有重复出现的 j != i + 1, so continue
                #当  j != i + 1 and nums[j] == nums[j - 1]说明有重复出现
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # get sum result 
                sum = target - nums[i] - nums[j]

                # two pointer algorithms
                left, right = j + 1, length - 1

                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
                        
        return res

if __name__ == '__main__':
    ll = Solution()
    nums = [1,0,-1,0,-2,2]
    target = 0
    x = ll.fourSum(nums, target)
    print(x)




