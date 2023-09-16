#de novo shotgun assembly: from scratch random
#Coverage refers to the amount of reduntand information we have in the genome.
#Coverage of a specific base say, 'C'  = amount of aligned reads in that position  = 5
#Overall all converage: total length of aligned reads/ total length of genome. Average converage = 177 bases/35 bases = 5.So, 5 fold coverage

#First law of assembly:
#If a suffix of read A is similar to a prefix of read B ... then A and B might overlap in the genome.

#Second law of assembly:
#More coverage leads to more and longer overlaps.

#Directed graph/ overlap graph: with nodes and edges O-->O. Nodes corresponds to nodes.
#The pair of reads with overlaps will be represented by directed edges/arrows.
#The direction will be from the nodes that has overlapping suffix to the nodes that have overlapping prefix

#Nodes: all 6-mers from reads
#Edges: overlaps of length >= 4
############################################################################

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

overlap('TTACGT','CGTACCGT')
#3
overlap('TTACGT','CTTACCGT')
#0

#Now let's make a naive overlap map
from itertools import permutations

#list(permutations([1,2,3],2))
#gives you a list of tuples
#Outupt: [(1, 2), (1, 3), (2, 1)...]

#We need to find overlaps for all the reads. So, each read will compare itself with all the remaining reads to search for overlaps
#We can easily do this using permutations, which will give you all possible arrangements of elements/reads without repeating any.
def naive_overlap_map(reads, k):
    olaps = {} #dictionary holding sequences of two overlapping reads along with their overlap length
    for a,b in permutations(reads, 2): #looping through the tuples
        olen = overlap(a, b, min_length=k) #If overlaps happens returns overlap length else, returns 0
        if olen > 0:
            olaps[(a,b)] = olen #dict[key] = value
    return olaps

reads = ['ACGGATGATC', 'GATCAAGT', 'TTCACGGA']
print(naive_overlap_map(reads, 3))
#Outupt: {('ACGGATGATC', 'GATCAAGT'): 4, ('TTCACGGA', 'ACGGATGATC'): 5}
