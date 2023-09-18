#adapt the editDistance function we saw in practice to answer questions 1 and 2 below.
# #Your function should take arguments p (pattern), and t (text) and should return the edit distance of the match
# between P and T with the fewest edits.

#Recall that: Rows of the dynamic programming matrix are labeled with bases from P and columns with bases from T
#Elements in the first row are set to 0
#Elements in the first column are set to 0, 1, 2, ..., as for edit distance
#Other elements are set in the same way as elements of a standard edit distance matrix
#The minimal value in the bottom row is the edit distance of the closest match between P and T


def readGenome(filename):
    genome= ''
    with open(filename, 'r') as fh:
        for line in fh:
            # Ignore the header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

genome = readGenome('chr1.GRCh38.excerpt.fasta')

def editDistance(x, y):
    # Create distance matrix
    D = []
    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))
    # Initialize first row and column of matrix
    for i in range(len(x)+1):
        D[i][0] = i
    for i in range(len(y)+1):
        D[0][i] = 0
    # Fill in the rest of the matrix
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
    # Returning the minimum edit distance between x and y, which is the minimum score in the last row.
    print(min(D[-1]))
    return min(D[-1])

# P =GCGTATGC within T =TATTGGCTATACGGTT had 2 edits
P = 'GCGTATGC'
T ='TATTGGCTATACGGTT'
print(editDistance(P,T))
##################################
P = 'GCTGATCGATCGTACG'
print(editDistance(P,genome))
##################################
P = 'GATTTACCAGATTGAG'
print(editDistance(P,genome))


#Say we are concerned only with overlaps that (a) are exact matches, and (b) are at least k bases long.
# To make an overlap graph, we could call overlap(a, b, min_length=k) on every possible pair of reads from the dataset.
#But that becomes very slow. Say if k = 6 and read 'a' suffix= GTCCTA. Say GTCCTA does not occur in any other read in the dataset.
#So, 'a' suffix cannot possibly overlap with the prefix of any other read.
# So, to save work we can ignore reads that don't contain suffix of a to begin with.
#So make a function that first searches whether the k-mer suffix of reads match any of the k-mer substrings, if it does then use the overlap function.

#Hint: Can make a set of all k-mer substrings of reads. Make a dictionary that associates the reads to their k-mer substrings.
#For 'a' give a check if suffix of 'a' matches with any of the substrings in the set.
#If it does then perform overlap between 'a' and 'b' ('b' being the read associated with the matched substring in the set)

#Find all pairs of reads with an exact suffix/prefix match of length at least 30. Don't overlap with itself.

#####################################################
def overlap(a, b, min_length): #b comes after a
    start = 0
    #find minimum overlap of 3 between suffix of a to the prefix of b
    while True:
        start = a.find(b[:min_length], start) #find prefix of 'b' of length 3 in 'a'. Start finding from 0
        if start == -1: #find function returns -1 if it cannot find that pattern in 'a'
            return 0 #exits the function and returns 0
        if b.startswith(a[start:]): #verify if prefix of 'b' is equal to suffix of 'a' starting from position 'start' (till the end)
            return len(a)-start #length of the overlap
        start += 1

def naive_overlap_map(reads, k):
    olaps = {}
    for a,b in permutations(reads, 2): #looping through the tuples
        olen = overlap(a, b, min_length=k)
        if olen > 0:
            olaps[(a,b)] = olen #dict[key] = value
    return olaps

olaps = naive_overlap_map(seqs, 30)

##########################################
#Picture the overlap graph corresponding to the overlaps just calculated.
##How many edges are in the graph? In other words, how many distict pairs of reads overlap?
##How many nodes in the graph have at lease one outgoing edge? (How many reads have a suffix involved in an overlap)
EdgesCount = 0
k = set() #To only store unique reads whoes suffix overlaps
values = [] #Edit distance
for key, value in olaps.items():
    EdgesCount += 1
    values.append(value)
    k.add(key[0])

OutgoingEdge = len(k)
print(OutgoingEdge)

print("EdgesCount: ", EdgesCount)
print("EditDistances: ", values)

#Minimum maximum overlaps or readPairs with overlap
min(values)
max(values)
n = set(olaps.keys())
print("keys", len(n))


