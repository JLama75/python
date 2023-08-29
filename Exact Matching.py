#Naive exact matching
#wget --no-check https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/phix.fa
#read the fasta file and store the sequence in variable/string genome excluding the header
def readGenome(filename):
    genome= ''
    with open(filename, 'r') as fh:
        for line in fh:
            #ignore the header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

genome = readGenome('phix.fa')

#Now write a naive algorithm to do exact matching
def naive(p, t): #p--> pattern ; t: text file
    occurrences = [] #empty list to record all instances of matching
    for i in range(len(t)-len(p)+1): #outer loop to do alignments over t
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:#comparing for each position in t with all positions in j
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences

t = 'AGCTTAGATAGC'
p = 'AG'
naive(p,t)

import random
def generateReads(genome, numReads, readLen):
    #Generate artificial reads from random positions in the given genome.
    #numReads is the total number of different sequences you want to generate
    #readLen is the total length of each of the read sequence you generate
    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome)- readLen) -1 #random.randint generates integers at random starting from 0 to n
        reads.append(genome[start : start+readLen]) # append the randomly generated sequences in the list reads.
    return reads
reads = generateReads(genome, 100, 100)

#How many of the artifically generated reads match back to the genome using exact matching
#should match 100%
#naive(reads, genome)
numMatched = 0 #counting the total number of matches
for r in reads:
    matches = naive(r, genome) # matches is the list of indices where read matches the genome
    if len(matches) > 0:
        numMatched += 1
print('%d / %d reads matched exactly!' %(numMatched, len(reads))) # Now calculating matches out of total reads
