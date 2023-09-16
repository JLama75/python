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

def overlap(a, b, min_length=3): #b comes after a
    start = 0
    #find minimum overlap of 3 between suffix of a to the prefix of b
    while True:
        start = a.find(b[:min_length], start) #find prefix of 'b' of length 3 in 'a'. Start finding from 0
        if start == -1: #find function returns -1 if it cannot find that pattern in 'a'
            return 0 #exits the function and returns 0
        if b.startswith(a[start:]): #verify if prefix of 'b' is equal to suffix of 'a' starting from position 'start' (till the end)
            return len(a)-start #length of the overlap
        start += 1

overlap('TTACGT','CGTACCGT')
#3
overlap('TTACGT','CTTACCGT')
#0
