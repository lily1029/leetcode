class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        pre = None  
        while head:
            nextNode = head.next 
            head.next = pre     
            pre = head
            head = nextNode 
        return pre
if __name__ == '__main__':
    ll = Solution()
    # Example usage:
    # Create a linked list: 1 -> 2 -> 3 -> None
    head = ListNode(1, ListNode(2, ListNode(3)))
    x = ll.reverse(head)
    
    while x:
        print(x.val, end = "->")
        x = x.next
    print("null")