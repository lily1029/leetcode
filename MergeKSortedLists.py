import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Define less than comparison for ListNode
    #比较两个linkedlist上nodes值大小
    def __lt__(self, other):
        return self.val < other.val
    
#这里也可以使用lambad表达式去对2个数做比较，uncomment 下下面这个line
#并且comment out 上面的比较method 就可以了      
#ListNode.__lt__ = lambda x, y: (x.val < y.val)

class Solution:
    def mergeKLists(self, lists):
        # Handle empty input case
        #如果lists为空，返回None
        if not lists:
            return None
        
        # Create a dummy node to connect merged nodes
        #建一个dummy node 来连后面merge好的nodes
        dummy = ListNode()

        # Tail points to the dummy node initially
        #尾巴节点也指向dummy node
        tail = dummy

        # Create a min heap
        #建一个heap
        heap = []
        
        #用for循环go throug lists, 并且把所有lists都放入heap中
        # Push the heads of all non-empty lists into the heap
        for head in lists:
            if head:
                heapq.heappush(heap, head)
        
        # While there are elements in the heap
        #然后循环heap, 只要heap不为空
        while heap:
            # Pop the smallest node from the heap, 并记录它是smallest_node
            #这里从heap里pop出来的一定是heap里最小的数
            smallest_node = heapq.heappop(heap)

            # Connect the smallest node to the tail
            #尾巴节点连上这个smallest_node节点
            tail.next = smallest_node

            # Move tail to the newly added node
            #更新尾巴节点
            tail = tail.next

            # If there's a next node in the popped node, push it to heap
            #如果smallest_node节点的下个节点不为空，将smallest_node.next推入到heap里
            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next)
        
        #最后返回dummy.next
        # Return the merged list starting from the dummy node's next
        return dummy.next

if __name__ == '__main__':
    # Example usage:
    ll = Solution()
    
    # Creating example linked lists
    list1 = ListNode(1, ListNode(5))
    list2 = ListNode(2, ListNode(6))
    list3 = ListNode(7)
    
    # Example input as a list of linked lists
    lists = [list1, list2, list3]
    
    # Merge the lists
    merged_list = ll.mergeKLists(lists)
    
    # Print the merged list
    while merged_list:
        print(merged_list.val, end=" -> ")
        merged_list = merged_list.next
    print("null")
