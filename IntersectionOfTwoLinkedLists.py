
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        #a, b为两个同向双指针从左往右走，分别指向两个linkedlists
        a, b = headA, headB
        
        #这里用while 循环比较头指针，当头指针不相等时，挪动到下一个链表节点
        while a != b:
            #a指向a的下个链表节点如果a存在否则指向headB链表，当多次循环后相遇
            #intersection 节点
            a = a.next if a else headB
            b = b.next if b else headA

        #最后返回链表头节点及返回整个链表
        return a
if __name__ == '__main__':
    # Create the lists and their intersection
    # List A: a1 -> a2 -> c1 -> c2 -> c3
    # List B: b1 -> b2 -> b3 -> c1 -> c2 -> c3

    # Create common intersection nodes
    c3 = ListNode("c3")
    c2 = ListNode("c2", c3)
    c1 = ListNode("c1", c2)

    # Create list A
    a2 = ListNode("a2", c1)
    a1 = ListNode("a1", a2)

    # Create list B
    b3 = ListNode("b3", c1)
    b2 = ListNode("b2", b3)
    b1 = ListNode("b1", b2)

    # Instantiate the solution and find the intersection
    ll = Solution()
    x = ll.getIntersectionNode(a1, b1)

    # Print the result
    print(x.val)