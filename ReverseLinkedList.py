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
        #链表头节点前加一个 pre 节点， 并付初始值为None,
        pre = None  

        #循环head 节点， 来遍历链表，
        while head:
            #use nextNode to denote the next node of head
            nextNode = head.next 
            #改变头指针的方向，指向pre,
            head.next = pre  
            #然后，pre 和 head 同时向前走一步，  
            pre = head
            head = nextNode 
        #最后return pre 因为head 节点最后走向None 了
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