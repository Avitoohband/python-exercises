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
        return(i - 1)//self.d

#get index of a parent and pos of a child(0-2) and returns the child index
    def get_child(self, i , pos):
        return (i * self.d + (pos +1))

#get the value of the current index
    def get_value(self,i):
        return self.items[i]

#get the max element of the heap(root)
    def get_max(self):
        if self.get_size() == 0:
            return None
        return self.items[0]

#return the max element in the array(heap) and removes it from the heap
#then, rearrange the heap to be and the appropriate order
    def extract_max(self):
        if self.get_size == 0:
            return None
        max = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify()
        return max

#rearrange the heap as max heap there is a problem here
    def max_heapify(self, i):
        while( i < self.get_size()):
            max = i
            for j in range(self.d):
                child = self.get_child(i, j)
                if(child < self.get_size() and self.get_value(child) > self.get_value(max)):
                    max = child
                if (max != i):
                    self.swap(max, child)
                    print(max)
                    self.max_heapify(max)
                i += 1

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
#change the number of children of the heap
    def change_num_children(self,new_d):
        self.d = new_d;
        self.max_heapify(0)

h = DArrayHeap(5)
h.insert(100)
h.insert(50)
h.insert(10)
h.insert(25)
h.insert(40)
h.insert(5)
h.insert(4)
h.insert(60)
h.insert(41)
h.insert(48)
h.insert(57)
h.insert(56)
h.insert(56)
h.insert(400)
h.insert(350)
h.insert(100)
print(h.items)
# print(h.d)
h.change_num_children(2)


#Binadry cases
# Arr[(i-1)/2] Returns the parent node.dr
# Arr[(2*i)+1] Returns the left child node.
# Arr[(2*i)+2] Returns the right child node

