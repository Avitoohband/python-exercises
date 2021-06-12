# count how many numbers in the heap are bigger than the given value
def count_heap(given_heap, pos, size, value):
    if pos >= size:  # if we exceed the limits of the array
        return 0

    if given_heap[pos] > value:  # return 1 and make recursive call for the left and right children
        return (1 + count_heap(given_heap, 2*pos +1, size, value)  # right child
                + count_heap(given_heap, 2*pos + 2, size, value))  # left child

    else:  # we're smaller or equal to the key
        # return 0 and make recursive call for the left and right children
        return (0 + count_heap(given_heap, 2 * pos +1, size, value)  # right child
                + count_heap(given_heap, 2 * pos + 2, size, value))  # left child


# parent = (i-1)\\2
# left_child = 2*i + 1
# right_child = 2*i + 2

key = 4
h = [50, 40, 30, 15, 4, 29, 7]
print("the size of the heap: " + str(len(h)))
print("key: " + str(key) + "\namount of bigger elements: " + str(count_heap(h, 0, len(h) - 1, key)))
