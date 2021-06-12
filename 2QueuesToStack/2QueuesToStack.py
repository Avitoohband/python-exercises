class TwoQueuesStack:
    def __init__(self):
        self.q1 = StackQueue()
        self.q2 = StackQueue()

    def isEmpty(self):
        return self.q1.isEmpty()

    # is stack is not empty, return first element
    def POP(self):
        if self.isEmpty():
            print("stack is empty!")
            return None
        return self.q1.dequeue()

    # is q 1 is empty ,enqueue there , else , move all elements to q2 than enqueue q1,
    # returns all element from q2 to q1
    def PUSH(self, value):

        if self.isEmpty():
            self.q1.enqueue(value)
        else:
            while not self.q1.isEmpty():
                self.q2.enqueue(self.q1.dequeue())

            self.q1.enqueue(value)
            while not self.q2.isEmpty():
                self.q1.enqueue(self.q2.dequeue())

class StackQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, value):
        node = QueueNode(value)
        if self.isEmpty():
            self.rear = self.front = node  # if q is empty, both rear and front are the new node
        else:  # the new node is the front
            node.next = self.front  # new node --> front
            self.front.prev = node  # node <-- front
            self.front = node  # front  = new node
        self.size += 1  # increment the size

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty!")
            return None
        temp = self.rear.value  # the value to return
        self.rear = self.rear.prev  # rear become its predecessor
        if self.rear is None:  # if the rear is None, it was the last element in the queue
            self.front = None  # the front and the rear are now both None
        else:
            self.rear.next = None  # if not, rear is the last element and his next is None rear --> None
        self.size -= 1  # decrement the size
        return temp

class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


tqs = TwoQueuesStack()
tqs.PUSH(1)
tqs.PUSH(2)
tqs.PUSH(3)
tqs.PUSH(4)
print(tqs.POP())
print(tqs.POP())
print(tqs.POP())
print(tqs.POP())