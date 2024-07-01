class Solution:

    def mark_lists(self, list1, list2):
        # Initialize pointers for list1 and list2
        i, j = 0, 0
        merged_list = []

        # Merge the two lists
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i] + "1")
                i += 1
            else:
                merged_list.append(list2[j] + "2")
                j += 1

        # Add remaining elements from list1
        while i < len(list1):
            merged_list.append(list1[i] + "1")
            i += 1

        # Add remaining elements from list2
        while j < len(list2):
            merged_list.append(list2[j] + "2")
            j += 1

        return merged_list
if __name__ == '__main__':
    ll = Solution()
    # Example usage
    list1 = ["apple", "cherry"]
    list2 = ["apricot", "blueberry"]
    merged_list = ll.mark_lists(list1, list2 )
    print(merged_list)
