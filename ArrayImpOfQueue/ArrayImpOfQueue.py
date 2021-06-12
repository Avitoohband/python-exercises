class Queue:
    def __init__(self, capacity):
        self.size = 0  # number of items in queue
        self.capacity = capacity  # n
        self.items = [None] * capacity
        self.front = 0
        self.rear = capacity - 1  # equals n-1 so if we add 1 and % in n we will get 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.isFull():
            print("Full!")
            return
        self.rear = (self.rear + 1) % self.capacity  # to go in circles
        self.items[self.rear] = value
        self.size += 1
        print(str(value) + " has enqueued to the queue")

    def dequeue(self):
        if self.isEmpty():
            print("Empty!")
            return
        temp = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return temp

    def peek_front(self):
        if self.isEmpty():
            print("Empty!")
            return
        print("front is: " + str(self.items[self.front]))

    def peek_rear(self):
        if self.isEmpty():
            print("Empty!")
            return
        print("rear is: " + str(self.items[self.rear]))











