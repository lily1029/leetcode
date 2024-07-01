class Soultion:

    def find_index_with_equal_sum(self, nums):
        #Calculate the total sum of all elements in the list.
        total_sum = sum(nums)
        #Initialize a variable to keep track of the left sum 
        #as we iterate through the list.
        left_sum = 0
        
        #Iterate through each index of the list
        for i in range(len(nums)):
            #Subtract the current element from the total
            # sum to get the right sum
            right_sum = total_sum - left_sum - nums[i]
            #If the left sum equals the right sum,
            #return the current index.
            if left_sum == right_sum:
                return i
            #Otherwise, update the left sum and continue.
            left_sum += nums[i]
        
        return -1
if __name__ == '__main__':
    ll = Soultion()
    nums1 = [1, 2, 4, 2, 1]
    x = ll.find_index_with_equal_sum(nums1)
    print(x)


# Example usage:
# nums1 = [1, 2, 3, 4, 3, 2, 1]
# nums2 = [1, 2, 3, 4, 5]
# nums3 = [2, 1, 1, 2, 1, 1]

# print(find_index_with_equal_sum(nums1))  # Output: 3 (sum of left half [1, 2, 3] = sum of right half [3, 2, 1])
# print(find_index_with_equal_sum(nums2))  # Output: -1 (no such index where left sum equals right sum)
# print(find_index_with_equal_sum(nums3))  # Output: 2 (sum of left half [2, 1] = sum of right half [1, 1])
