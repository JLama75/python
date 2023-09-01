#solutions('cdeo', [3, 2, 0, 1]) should return 'code'
def solutions(S, A):
    if not len(S) == len(A):
        #print("break")
        return {}
    i = 0 #should be updated position to find the next 'S' value
    s = ''
    for j in range(0, len(A)):
        s = s+ S[i] #c + o + d + e
        value = A[i]  #3, 1, 2, 1
        i = value #the next position where we can find the 'S' value 
        #print("next i: ", i, s)
    return s
solutions('cdeo', [3, 2, 0, 1])

##################################################################################################################################################

#A = [1, 2, 3, -4, 5, -5]: solutions(A) should return (5,-5). Should return the largest value (A>0) and its opposite/negative value.
#If the -ve value does not exist for the largest value, the function should return zero.

def solution(A):
  """ Finds the largest and smallest numbers in a list."""
  largest = None
  for num in A:
    if largest is None:
      largest = num
    elif num > largest:
      largest = num
  if -largest in A:
      return largest, -largest
  return 0

A = [1, 2, 3, -4, 5, 99]
B = [1, 2, 3, -4, 5, -5]

print(solution(A))
print(solution(B))
