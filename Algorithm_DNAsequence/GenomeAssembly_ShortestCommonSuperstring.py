#shortest common superstring problem (SCS)
#S: BAA AAB BBA ABA ABB BBB AAA BAB
#Concat(S): BAAAABBBAABAABBBBBAAABAB
#SCS(S): AAABBBABAA

#downside: not tractable for large sequences- NP-complete
#Try all possible orderings and pick shortest superstring
#If S contains n strings, n! orderings possible. Larger strings more time and slower.

#If a and b are two reads. Lets see if the prefix of b overlaps suffix of a and if they do return the overlap length.
def overlap(a, b, min_length=3): #b comes after a
    start = 0
    while True:
        start = a.find(b[:min_length], start) #find prefix of 'b' of length 3 in 'a'. Start finding from 0. Only finds the leftmost occurrence. (say start = 4)
        if start == -1: #the find function returns -1 if it cannot find that pattern in 'a'
            return 0 #exits the function and returns 0
        if b.startswith(a[start:]): #verify if the prefix of 'b' is equal to the suffix of 'a' i.e. pattern starting from position 'start = 4' till the end of 'a' == prefix of 'b'
            return len(a)-start #length of the overlap
        start += 1 #If not then find the pattern(prefix of 'b') again from the last position the find function returned (start = 4 + 1 = 5).


#To perform genome assembly, finding the shortest common superstirng (scs):
import itertools
from itertools import permutations

def scs(ss):
    shortest_sup = None
    #loop in through all possible orders of the string/reads
    for ssperm in itertools.permutations(ss): #Find the overlapped genome for each ordered string
        sup = ssperm[0] #start with the first read then add in the suffix of the adjacent overlapped read.
        for i in range(len(ss) -1):
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    return shortest_sup

scs(['ACGGTACGAGC', 'GAGCTTCGGA', 'GACACGG'])
#'GACACGGTACGAGCTTCGGA'
