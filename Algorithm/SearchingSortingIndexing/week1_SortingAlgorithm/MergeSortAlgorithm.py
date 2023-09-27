#Merge sort algorithm: Sorting the given array by
# dividing/splitting the array into smaller subsets and performing a basic operation or base case. Then merge the sorted subsets.

#       1. Split the list into two sublists of size n/2
#       2. Sort the sublists
#       3. Merge the result

#The following Python code has three functions.
#       1) mergesort(array): takes in a list or array and returns the sorted array. Calls function mergesortHelper.
#       2) mergesortHelper(array, left, right): recursive function that splits the array into sublists, 
#          #performs comparison and swapping to sort, and merging of the sorted sublists. Calles mergeLists function. 
#       2) mergeLists(array, left, mid, right): compares two sorted sublists, 
#       ```#sorts and makes a temporary list to store the sorted elements; copies it to the array

def mergeLists(array, left, mid, right): #Performs merge on sublists lst[left:mid+1] and lst[mid+1:right+1]
    if left > mid or mid > right: #one of the two sublists is empty
        return
    i = left
    j = mid + 1
    tmp_store = []
    while (i <= mid or j <= right):
        if (i <= mid and j <= right):
            if (array[i] < array[j]):
                tmp_store.append(array[i]) #copy the i element the move the pointer one step forward
                i = i + 1
            else:
                tmp_store.append(array[j])
                j = j + 1
        elif i <= mid:
            tmp_store.append(array[i])
            i = i + 1
        else:
            tmp_store.append(array[j])
            j = j + 1
    #copy back to the arrays
    assert(len(tmp_store) == right - left + 1)
    for i in range(left, right+1): #including the right: (4,7+1) so it goes from 4 to 7
        array[i] = tmp_store[i - left] # temp_store[4-4], ..[5-4], [6-4] ...
    return array

#Sorts the array/list provided
def mergesortHelper(array, left, right):
    #base case
    if left >= right: #empty if subarray=left>right
        return
    #base case
    elif (left + 1 == right): #if array has two elements
        if array[left] > array[right]: #compare
            n = len(array)
            assert (left >= 0 and left < n)  # checks the conditions are met or not. If not raises 'AssertionError'.
            assert (right >= 0 and right < n)
            array[left], array[right] = array[right], array[left] #swap to sort
        return
    else:
        mid = (left + right)//2
        mergesortHelper(array, left, mid) #Sort the left half recursively
        mergesortHelper(array, mid+1, right) #Sort the right half recursively
        mergeLists(array, left, mid, right) #merge the right and left half together

def mergesort(array):
    if len(array) <= 1:
        return #nothing to do
    else:
        mergesortHelper(array, 0, len(array)-1) #if len(array) = 10 then left:right = 0:9


#Let us run a few tests:
array = [0, 5, 6, 2, 19, -1, 2, 3, 0, 4, 5, 8]
mergesort(array)
print(array)
#[-1, 0, 0, 2, 2, 3, 4, 5, 5, 6, 8, 19]

array = [0, 1, 2, 6, 18, 19, -20, -45, -23, 25, 56, 19, 81, 123, 122]
mergesort(array)
print(array)
#[-45, -23, -20, 0, 1, 2, 6, 18, 19, 19, 25, 56, 81, 122, 123]

array = [1]
mergesort(array)
print(array)
#[1]

array = []
mergesort(array)
print(array)
#[]


#How fast is the mergeSort algorithm:

# opertions: comparison between left and right elements and copying in the temp store--> these are constant though
# So, running time of merge = size of array (n) = (right-left+1) : 9-0+1 =10
# Suppose, n = 2^k. In each iteration, n is split into n/2 (2^k-1); then n/4 (2^k-1); then  n/8 (2^k-1)... n (2^k-k)
# cost of merge sort = n* no. of steps/recursion levels it undergoes = n* k = n* log2(n)
# cost of merge sort = theta/bigO (nlog2(n)) (cost is equal to or upper bound/ less than equal to (nlog2(n))

#If you want to sort an array of with 1 million elements, the merge cost will take 19 million time units.
#If n = 1 million (10^6); n ~ 2^19.93 ; k = 19.93
#cost of merge sort = 10^6 * 19.93 or, 10^6 * log2(10^6) = 19 million

#How does it compare with insertion sort, whose cost = n^2. Note: this is after disregarding the constants.
#insertion cost = 10^12 (trillion) vs. merge sort = 19^6 (19 million)
