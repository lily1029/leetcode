class Node:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def __init__(self):
        #这里定义一个全局变量,key是old node, value是new node 
        #self.visitedDict = {OldNode : NewNode}
        self.visitedDict = {}

    def copyRandomList(self, head):
        # if head is None, return None
        if not head:
            return None
        
        #如果这个点(head)已经被复制在dict()里，只需直接拿出即可
        if head in self.visitedDict:
            #new_node就是old node 所对应的哈希值
            new_node = self.visitedDict[head]
            #并返回这个new_node，给对应的新的copy的node加上这个哈希值（either: next or random）
            return new_node
        else:
            #否则这个new_node还没有被复制,创建一个新的new_node 
            new_node = Node(head.label)
            #并把这个new_node放入到哈希表中
            self.visitedDict[head] = new_node
            
            #下面用递归去创建new_node.next node 和 random 
            new_node.next = self.copyRandomList(head.next)
            new_node.random = self.copyRandomList(head.random)
            
            #最后返回new_node 头节点
            return new_node

if __name__ == '__main__':
    # Step 1: Create the original nodes
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)

    # Step 2: Setup next pointers
    node1.next = node2
    node2.next = node3

    # Step 3: Setup random pointers
    node1.random = None
    node2.random = node1
    node3.random = node2

    # Step 4: Make the deep copy
    solution = Solution()
    copied_head = solution.copyRandomList(node1)

    # Step 5: Print original and copied lists for verification
    def print_list(head):
        current = head
        while current:
            rand_label = current.random.label if current.random else None
            print(f"Node label: {current.label}, Random label: {rand_label}")
            current = current.next

    print("Original list:")
    print_list(node1)

    print("\nCopied list:")
    print_list(copied_head)
