#Binary search algorithm:
#Used when array is sorted. Is very fast.
#First search the search elemnent in the middle of the array. If it is greater than mid element search the right portion, vice versa

#Use Recursive function:
def binarySearchHelper(lst, elt, left, right):
    # 0 <= left <= right < len(lst):
    if left > right:
        print(left, right)
        return None
    mid = (left+right)//2 #// is integer division
    if lst[mid] == elt:
        #print("mid: ",mid)
        return mid #we found the number, elt.
    elif lst[mid] < elt:
        #print("greater than: ", lst[mid])
        return(binarySearchHelper(lst, elt, mid+1, right))
    else:
        #print("less than: ", lst[mid])
        return(binarySearchHelper(lst, elt, left, mid-1))

lst = [1, 2, 4, 7, 9, 12, 20, 45]
elt = 9
binarySearchHelper(lst, elt, 0, (len(lst)-1))

#Running time analysis of binary search
#In binary search algorithm, in each iteration the size becomes halved.
# #If n = 2 power k. then each iteration goes: n/2 or, 2(k-1); n/4 or, 2(k-2) ....so on until 1 or 2(k-k)
#At most k+1 steps: where  k = log2(n). BigO(log2(n))

# Search in array with  10 billion [(10^9) ~ 2^30] elements. k = 30
#Worst case: In 31 binary search steps: you can either find the element or conclude it does not exists

# Search 1 trillion (10^12) #just 41 steps
