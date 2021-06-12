class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    @staticmethod
    def detectLoop(head):
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


node0 = Node(1)
node1 = Node(50)
node2 = Node(20)
node3 = Node(15)
node4 = Node(4)
node5 = Node(10)

node0.next= node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None
print(Node.detectLoop(node0))
node5.next = node3
print(Node.detectLoop(node0))
