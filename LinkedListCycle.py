
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    #此题的做法是用两个同向双指针fast, slow指向头指针，快指针每次
    #走2步，慢指针走一步，如果链表是一个cycle,那么这两个指针最终会
    #相遇，相遇的时候就是证明存在环的时候，如果没有cycle，这两个指针不会相遇
    def hasCycle(self, head):
        # 两个指针同时指向链表表头
        fast, slow = head, head 
        
        #循环当快指针和快指针的下一个点存在时，快指针 走2步，慢指针走一步
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
            
            #如果两个指针相等，表明两个指针相遇，返回true,否认则false
            if fast == slow:
                return True 
            
        return False
if __name__ == '__main__':
    # Create a list
    # a->b->c->d->b
    # 21 -> 10 -> 4 -> 5 -> 10
    

    # Create common intersection nodes
    d = ListNode("5")
    c = ListNode("4", d)
    b = ListNode("10", c) 
    a = ListNode("21", b)
    d.next = b

  
    ll = Solution()
    x = ll.hasCycle(a)

    # Print the result
    print(x)


