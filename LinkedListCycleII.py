
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    #此题的做法是用两个同向双指针fast, slow指向头指针，快指针每次
    #走2步，慢指针走一步，如果链表是一个cycle,那么这两个指针最终会
    #相遇，相遇的时候就是证明存在环的时候，如果没有cycle，这两个指针不会相遇
    #这里它们的相遇点正是cycle点开始的前一个点，所以快慢指针各自向前走一步
    #就找到了cycle的起始点
    def detectCycle(self, head):
        #corner case
        if not head or not head.next:
            return None 
        
        # 两个指针同时指向链表表头
        fast, slow = head, head 

        #循环当快指针和快指针的下一个点存在时，快指针 走2步，慢指针走一步
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next

            #如果两个指针相等，表明两个指针相遇，这时停下来，因为这个点是
            #cycle起始点的前一个点， 停在这个点
            if fast == slow:
                break 
        
        
        #判断slow=fast找到了两个指针相遇的点，是cycle起始点的前一个点
        if slow == fast: 
            
            #将慢指针归位于head，           
            slow = head 
            # 因为快慢指针指的不一样
            while slow != fast:
                #各自向前一步就是
                slow = slow.next 
                fast = fast.next 
            
            #此时找到了cycle 开始的点，并返回 slow 点或是fast点都可以
            return slow 
        
        #如果没有，返回none
        return None
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
    x = ll.detectCycle(a)

    # Print the result
    print(x.val)


