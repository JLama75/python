#"Algorithm for Searching, sorting and Indexing"- Sriram Sankaranarayanan from University of Colorado Boulder
#Coursera
#Types of sorting algorithm
#Insertion sort
#Merge sort
#Heap sort
#Quick sort

#Introduction to Insertion sort algrorithm
#[a[1]..., a[j]...a[n]]
#i) Find insert position
#ii) move elements over

#start scanning from right and swap the elements if A[j] < A[j-1]

A= [2,7,15,24,10,1]

def insert(A, j):
    for i in range(j-1,-1,-1): #start loop from j-1 till 0.
       if A[i] > A[i+1]:
          A[i], A[i+1] = A[i+1], A[i] #swap
          print(A)
       else:
           break
    return A
#insertionsort(A)
for j in range(len(A)):
    print(j)
    insert(A, j)
print("final array: ", A)

#Computation complexity (how many times does it take to run and how many space):
#measure time to be independent of the processor
# time and space in Best cases and worst cases. (Best cases complexity, Worst cases complexity)

#Best case for insert: immediately break from loop #when elements is sorted
#cost for insert(A,j): C3(cost for for loop) + C1 (cost of conditional statement) + C4(cost of calling break)
#cost for insertionsort(A): n * (cost of insert)

#Worst case of insert: when iteration has to go from j till the beginning
#cost: (j-1) (C1 +C2 + C3 )
#cost: n(n-1)/2 (C1+C2+C3)
