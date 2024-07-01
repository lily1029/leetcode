class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    (1) 先建一个dummy node , 用 cur 指针指向 dummy
    (2) 循环链表，条件是：
    while l1 and l2:
    (3). 比较l1.val 和 l2.val , 并和cur.next 链接， 同时更新l1 和 l2 的下个节点
    （4）还有一种情况是，一个链表长，一个链表短， 所以跳出循环后， 要加上
    cur.next = l1 or l2
    (5） 最后返回dummy.next
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2 

        return dummy.next
if __name__ == '__main__':
    # Example usage:
    ll = Solution()
    # Creating example linked lists
    list1 = ListNode(1, ListNode(5))
    list2 = ListNode(2, ListNode(6))
    x = ll.mergeTwoLists(list1, list2)
    while x:
        print(x.val, end="->")
        x = x.next
    print("null")