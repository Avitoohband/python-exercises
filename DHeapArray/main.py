import copy
class DArrayHeap:
#initiate the deap, declare number of children
    def __init__ (self, d):
        self.items = []
        self.d = d

#get the size of the array(heap)
    def get_size(self):
        return len(self.items)

#return the partent location of the given index(child)
    def get_parent(self, i):
        return (i - 1)//self.d

#get index of a parent and pos of a child(0-2) and returns the child index
    def get_child(self, i , pos):
        return (i * self.d + (pos +1))

#get the value of the current index
    def get_value(self, i):
        return self.items[i]

#get the max element of the heap(root)
    def get_max(self):
        if self.get_size() == 0:
            return None
        return self.items[0]

#return the max element in the array(heap) and removes it from the heap
#then, rearrange the heap to be and the appropriate order
    def extract_max(self):
        if self.get_size() == 0:
            return None
        max = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return max

#rearrange the heap as max heap
    def max_heapify(self, i):
        max = i
        for j in range(self.d):
            child = self.get_child(i, j)
            if(child < self.get_size() and self.get_value(child) > self.get_value(max)):
                max = child
        if (max != i):
            self.swap(max, i)
            self.max_heapify(max)


#get two indexes and swap between them
    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

#gets a value(key) and puts it in the  appropriate position of the heap
    def insert(self, key):
        i = self.get_size()
        self.items.append(key)
        while( i != 0 ):
            parent = self.get_parent(i)
            if self.get_value(parent) < self.get_value(i):
                self.swap(parent, i)
            i = parent

#change the numbers o children of the heap
    def change_num_children(self, d):
        self.d = d
        new_items = copy.deepcopy(self.items)
        self.items.clear()
        for item in new_items:
            self.insert(item)
#prints errors
def call_error(errorType):
    if(errorType == 0):
        print("A heap is already existed\n")
    if(errorType == 1):
        print("You need to create a Heap first\n")

# get numbers from the user and split it into list, then insert the numbers to the heap
# assuming the user insert appropriate input
def get_list_to_heap(h: DArrayHeap):
    numbers = input("Please enter numbers with SPACES in between!\n")
    lst = numbers.split(" ")
    for item in lst:
        h.insert(item)

#to know iuf there's already existing heap

isExistHeap = False
h = None


#while-loop for keep letting the user choose what option does he wants
while True:

#printing the menu
    print("""
Please choose one of the following:
1) Build-Heap
2) Insert
3) Extract-Max
4) Print-Heap
5) Change""")

#option No.1 , creating heap and filling it with numbers
    userOption = input()
    if userOption == "1":
        if isExistHeap:
            call_error(0)
        else:
            d = input("Please type down the number of children: ")
            h = DArrayHeap(int(d))
            isExistHeap = True
            get_list_to_heap(h)

#option No.2 , creating heap and filling it with numbers
    elif(userOption == "2"):
        if (not isExistHeap):
            call_error(1)
        else:
            num = input("please insert a number to add to the heap: ")
            h.insert(int(num))
# option No.3 , creating heap and filling it with numbers
    elif(userOption == "3"):
        if (not isExistHeap):
            call_error(1)
        else:
            print(h.extract_max())
# option No.4 , creating heap and filling it with numbers
    elif(userOption == "4"):
        if (not isExistHeap):
            call_error(1)
        else:
            print (h.items)
# option No.5 , creating heap and filling it with numbers
    elif(userOption == "5"):
        if (not isExistHeap):
            call_error(1)
        else:
            d = input("insert new number of children: ")
            h.change_num_children(d)
    else:
        print("Thank You")
        break

#Binadry cases
# Arr[(i-1)/2] Returns the parent node.dr
# Arr[(2*i)+1] Returns the left child node.
# Arr[(2*i)+2] Returns the right child node