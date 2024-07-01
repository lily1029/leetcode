class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:

    def find_last_node(self, head):
        # If the list is empty (head is None), return None
        if not head:
            return None
        
        # Traverse the list until we reach the last node
        current = head
        while current.next:
            current = current.next
        
        # current now points to the last node
        return current
if __name__ == '__main__':
    ll = Solution()
    # Example usage:
    # Create a linked list: 1 -> 2 -> 3 -> None
    head = ListNode(1, ListNode(2, ListNode(3)))
    last_node = ll.find_last_node(head)

    if last_node:
        print(f"The value of the last node is: {last_node.value}")
    else:
        print("The list is empty.")
