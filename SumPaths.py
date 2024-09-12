class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_paths(nums):
    if not nums:
        return 0
    
    # Build the tree structure from the list of numbers
    root = TreeNode(nums[0])
    if len(nums) > 1:
        root.left = TreeNode(nums[1])
    if len(nums) > 2:
        root.left.left = TreeNode(nums[2])
    
    # Helper function to calculate the sum of all paths
    def dfs(node, current_sum):
        if node is None:
            return 0
        
        # Calculate the current path sum
        current_sum = current_sum * 10 + node.val
        
        # If it's a leaf node, return the current path sum
        if node.left is None and node.right is None:
            return current_sum
        
        # Recursively calculate sum of left and right subtrees
        return dfs(node.left, current_sum) + dfs(node.right, current_sum)
    
    # Start DFS traversal from the root with initial path sum 0
    return dfs(root, 0)

# Example usage:
nums = [221, 113, 215]
print(sum_paths(nums))  # Output: 12


if __name__ =='__main__':
    ll = Soultion()

    # Example usage:
    nums = [221, 113, 215]
    x = ll.sum_paths(nums)
    print(x)  # Output: 12
