# this program manage open stack, open stack can have additional
# option and it is to insert key to the middle of the stack
# so, POP, PUSH, PUSH-MIDDLE
# all of the action should run in O(1)
# implement with DUE-QUEUE+STACK+ (optional)boolean

class OpenStack:

    def __init__(self):
        self.dq = DueQueue()
        self.s = Stack()
        self.even_deployment = True  # stars with 0 elements
        self.N = 0

    def OS_EMPTY(self):
        return self.N == 0

    def OS_PUSH(self, value):
        if self.even_deployment:
            self.dq.ENQUEUE_TAIL(value)
        else:   # not even
            self.dq.ENQUEUE_TAIL(value)
            temp = self.dq.DEQUEUE_HEAD()
            self.s.PUSH(temp)
        self.N += 1
        self.even_deployment = False if self.even_deployment else True

    def OS_POP(self):
        temp = None
        if not self.OS_EMPTY():
            if not self.dq.QUEUE_EMPTY():
                temp = self.dq.DEQUEUE_TAIL()
            elif not self.s.STACK_EMPTY():
                temp = self.s.POP()
            self.N -= 1
            self.even_deployment = False if self.even_deployment else True
            return temp
        print("Open Stack is empty!")
        return None

    def OS_MID_PEEK(self):
        if self.OS_EMPTY():
            print("Open Stack is empty!")
            return None
        if self.even_deployment:
            temp = self.s.peek()
            return temp
        else:  # not even
            temp = self.dq.head.value
            return temp

    def OS_PUSH_IN_MIDDLE(self, value):
        if self.OS_EMPTY():
            print("Open Stack is empty!\nmaking normal PUSH")
            self.OS_PUSH(value)
        else:
            if self.even_deployment:
                self.dq.ENQUEUE_HEAD(value)
            else:  # not even
                self.s.PUSH(value)
            self.even_deployment = False if self.even_deployment else True


class Stack:
    def __init__(self):
        self.bullets = []

    def STACK_EMPTY(self):
        return len(self.bullets) == 0 or self.bullets is None

    def PUSH(self, value):
        self.bullets.append(value)

    def POP(self):
        if not self.STACK_EMPTY():
            value = self.bullets[len(self.bullets) - 1]
            del self.bullets[len(self.bullets) - 1]
            return value
        else:
            print("Normal stack is empty")
            return None

    def peek(self):
        return self.bullets[len(self.bullets) - 1]

    def print_stack(self):
        for i in reversed(self.bullets):
            print(i)


class DueQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    # inset first item to the queue
    def ENQUEUE_FIRST(self, node):
        self.head = node
        self.tail = node

    # checks if the queue is empty, returns boolean
    def QUEUE_EMPTY(self):
        return self.head is None

    # insert anode at the head of the queue
    def ENQUEUE_HEAD(self, value):
        temp = Node(value)
        if self.QUEUE_EMPTY():
            self.ENQUEUE_FIRST(temp)
        else:  # queue is not empty, than insert at head
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    # remove a node from the head of the queue
    def DEQUEUE_HEAD(self):
        if not self.QUEUE_EMPTY():
            temp = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return temp.value
        return None

    # insert anode at the tail of the queue
    def ENQUEUE_TAIL(self, value):
        temp = Node(value)
        if self.QUEUE_EMPTY():
            self.ENQUEUE_FIRST(temp)
        else:  # queue is not empty, than insert at tail
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp

    # remove a node from the tail of the queue
    def DEQUEUE_TAIL(self):
        if not self.QUEUE_EMPTY():
            temp = self.tail
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
            return temp.value
        return None

    def print_queue(self):
        if not self.QUEUE_EMPTY():
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next
        else:
            print("Queue is empty!")

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


os = OpenStack()
os.OS_PUSH(5)
os.OS_PUSH(7)
os.OS_PUSH(4)
os.OS_PUSH(9)
print("Mid value is : " + str(os.OS_MID_PEEK()))
os.OS_PUSH(45)
print("Mid value is : " + str(os.OS_MID_PEEK()))
os.OS_POP()
print("Mid value is : " + str(os.OS_MID_PEEK()))
