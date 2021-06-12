# Selection sort ,this sort works with two sub-arrays,
# the sorted one and the unsorted one
# it find the minimum number in the given array and swap
# it with the new beginning of the sorted array
# there are two nested loops so the
# Running Time = O(n^2)
# Auxiliary Space = O(1)
# the good thing about selection sort that it'll do max of O(n) swaps
# can be used when memory wise is costly operation

def selection_sort(given_array):
    i = 0
    while i < len(given_array):  # running through the array
        smallest_pos = i  # the current pos of the element we're looking of
        for j in range(i+1, len(given_array)):  # running through the items that after i
            if given_array[smallest_pos] > given_array[j]:
                smallest_pos = j  # updating the pos of the new smaller element
        given_array[i], given_array[smallest_pos] = given_array[smallest_pos], given_array[i]  # swapping
        i += 1
    return given_array

# bubble sort is the most simple one, comparing one value to the adjacent one
# if it smaller then its following value, swapping them and checks the value with its new following
# comparing[this][with this][][]
# comparing[]][this][with this][]
# comparing[]][]][this][with this]
# Running Time = O(n^2)
# Auxiliary Space O(1)

def bubble_sort(given_array):
    for i in range(len(given_array)):  # running n times, for each element
        for j in range(len(given_array) -1 -i):  # check one element with all of the elements
            if given_array[j] > given_array[j+1]:  # if i bigger than my following
                given_array[j], given_array[j+1] = given_array[j+1], given_array[j]  # swap
    return given_array

# insertion sort , comparing the element with the one b4 him, if
# he is bigger than it, going backward and keep comparing
# with the previous elements, when reaches the start of the array or
# find elements that is not smaller than it self
# place it there and "pushes the afterward elements forward
# Running Time = O(n^2)
# Auxiliary Space = O(1)

def insertion_sort(given_array):
    for i in range(len(given_array)-1):  # going n times
        key = given_array[i + 1]  # store the key to compare with others
        j = i + 1  # the index of the current key
        while (j > 0 and key < given_array[j-1]):  # if we're smaller than our previous and
            # there are still items before us, "push" previous, one step forward
            given_array[j] = given_array[j-1]
            j -= 1  # decrement the j
        given_array[j] = key  # put the key at its place
    return given_array

# merge sort is a divide and conquer method, it takes the array and
# divide it by two halves, then it combine it to one merged array
# by taking the lower value from both of the sub arrays
# Running Time = O(nlogn)
# Auxiliary Space = O(n)

def merge_sort(arr, l, r):
    if l < r:  # stop case
        m = l+(r-l)//2  # find the middle


        # half the array to left-sub-array and right-sub-array
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)

        # combine the two halves
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    n1 = m - l + 1  # size of the left sub-array
    n2 = r - m   # size of the right sub-array
    left_array = [0] * n1  # create the left sub-array
    right_array = [0] * n2  # create the right sub-array

    # fill the sub-arrays
    for i in range(0, n1):
        left_array[i] = arr[l+i]
    for j in range(0, n2):
        right_array[j] = arr[m + 1 + j]

    left_p = right_p = 0  # pointers for the right and left sub arrays
    merge_p = l  # pointer for the merged array, starts from the l

    #  put the smaller number from both of the arrays in the merge sub array
    while left_p < n1 and right_p < n2:
        if left_array[left_p] <= right_array[right_p]:
            arr[merge_p] = left_array[left_p]
            left_p += 1
        else:
            arr[merge_p] = right_array[right_p]
            right_p += 1
        merge_p += 1

    # where there are items left, fill the merge array with them
    while left_p < n1:
        arr[merge_p] = left_array[left_p]
        left_p += 1
        merge_p += 1
    while right_p < n2:
        arr[merge_p] = right_array[right_p]
        right_p += 1
        merge_p += 1

# quick sort, it takes an elements as a pivot, in our case we takes the
# last element to be the pivot, than we call to the partition method
# which is rearrange the elements that are smaller to be to the left side of the
# pivot and the rest (bigger) to be to the right side of the pivot
# than put the pivot in between so it is in its right place in the array
# it is repeating until the whole array is sorted
# Running Time = best O(n) average O(nlogn) worst O(n^2)
# Auxiliary Space = O(n)

def quick_sort(given_array, low, high):
    if low < high:
        par_index = partition(given_array, low, high)
        quick_sort(given_array, low, par_index -1)  # b4 the partition index
        quick_sort(given_array, par_index + 1 , high)  # after the partition index

def partition(given_array, low, high):
    pivot = arr[high]  # takes the last element to be the pivot
    i = low - 1  # index of the smaller than the pivot element

    for j in range(low, high):  # from low to high - 1
        if arr[j] <= pivot:
            i += 1  # increment the index of the smaller element
            arr[i], arr[j] = arr[j], arr[i]  # swap the elements, put
            # the smaller element from the right side of the pivot
            # if the element is bigger than the pivot, wew do nothng and
            # leave it as it is, now we got all the elements that are
            # smaller or equal to the pivot to its left side
            # and all the elements that are bigger than the pivot to
            # its right side
    arr[i+1], arr[high] = arr[high], arr[i + 1]  # puts the pivot in its right place
    return i+1  # returns the pivot index(partition index)

# counting sort is finding the starting point for each number,
# we counting the occurrences  of times for each number and put in in another array
# which its length is in the size of the amount of different numbers we have in the
# original array
# the second step after we have the numbers of occurrences for each number
# is it add each number to the right of it in the array cumulatively
# the third step will be to shift the numbers one spot to the right
# so:
# 1) new array with the number of occurrences for each number
# 2) adding every occurrences to its right value in the array cumulatively
# 3) shift the elements one index to the right
# than we're going to the count array in the given_array-element
# starting position value, and put the given_array_element in its
# index in the sorted array
# than we decrees the count for the number we added
# n is the numbers of elements in the original array
# r is the numbers of the range we could have for each element in the array
# Running Time = O(n+r)
# Auxiliary Space = O(n+r)
# stable

def counting_sort(given_array):
    # the sorted array to return, in the size of the original array
    sorted_array = [0] * len(given_array)

    # first step: initiate array to count the occurrences
    # of each element , assuming we know the range of the value
    # that we could have in the array
    # this is arbitrary range
    count = [0] * 10  # if we have one digits numbers only, so 0-9

    # second step: store the count for each elements
    for item in given_array:
        count[item] += 1

    # third step: adding cumulatively the numbers to its right element
    # to get the starting index for each number
    # in other words, we know how many numbers should be before the
    # current number in the indexes array
    # [1][4][5] = count for each number
    # [0][1][2] = indexes
    # we know that 2 has 5 numbers before him
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # build the sorted array

    i = len(sorted_array) - 1
    while i >= 0:
        # going to the given array in the index i - 1, will point
        # to the its index in the indexes array
        #sorted      indexes  given_aray          # the numbers to insert
        sorted_array[count[given_array[i]] - 1] = given_array[i]
        count[given_array[i]] -= 1   # dec the count of the number we added
        i -= 1
    return sorted_array

arr = [5, 7, 8, 4, 3, 1, 5, 7, 9, 6]
arr1 = [5, 7, 8, 4, 3, 1, 5, 7, 9, 6]
arr2 = [1, 1, 1, 1, 1, 1]
arr3 = [5]
arr4 = [1,2,3,4,5,6,7,8,9]
arr5 = [9, 8, 7, 3, 5, 4, 3, 2, 1]

print(counting_sort([2,1]))
# print(selection_sort(arr1))

# print(bubble_sort(arr1))

# print(insertion_sort(arr1))

# merge_sort(arr, 0, len(arr) - 1)

# quick_sort(arr, 0 , len(arr)-1)
# print(arr)

