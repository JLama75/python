#A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
#For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
#Write a function:
#def solution(N)
#that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
#For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
#Write an efficient algorithm for the following assumptions:
#N is an integer within the range [1..2,147,483,647].

def solution(N):
    integer = int(N)
    #convert integer to binary
    binary = format(integer, 'b')
    k = len(binary)
    print(N, binary, k)
    CountZeros = [] #list to store the total zeros counted after 1
    strings = [] #list to store the string of numbers
    if len(binary) == 1:
        return 0
    for i in range(0, k-1): #if k = 5,then 0 to 4
        count = 0 #initialize count to 0
        #print("outer loop: ",i)
        if not binary[i] == '1':
            #print("binary is not equal to 1: skip")
            continue
        s = '1'  # initialize string
        #starting inner loop that checks whether values after 1 is zero or not and counts the number of zeros
        for j in range(1, k): #if k = 5, then 1 to 4
            if (i + j) > k - 1:
                #print("break as ", i+j, " exceed", k-1)
                break
            if binary[i + j] == '0':
                s = s + binary[i + j]
                #print("Inside loop: i= ", i, "s = ", s)
                continue
            count = j-1
            s = s + binary[i + j]
            #print("After last pattern match: count and string is ",count, s)
            break
        strings.append(s)
        CountZeros.append(count)
    #print("All counts: ", CountZeros)
    BinaryGap = max(CountZeros)
    return BinaryGap

#Generating random numbers and calling the function using them
import random
def randomNumbers(r, t):  #648, 20
    for i in range(t):
        num = random.randint(1, r)
        print(solution(num))
randomNumbers(1000, 20)

#Additional validation using tricky numbers
print("Binary Gap value is: ",solution(32))
print("Binary Gap value is: ",solution(1041))
print("Binary Gap value is: ",solution(15))
print("Binary Gap value is: ",solution(1))
print("Binary Gap value is: ",solution(652))
