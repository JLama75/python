#Naive exact matching using randomly generated reads and actual reads from fastq file.

#The test genome we are using is phix.fa
#wget --no-check https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/phix.fa

#parsing a DNA reference genome form a file in FASTA format
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

#Now generate your own artificial random reads from a fasta file and use an exact matching algorithm to align them to the same fast file.
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
numMatched = 0 #counting the total number of matches
for r in reads:
    matches = naive(r, genome) # matches is the list of indices where read matches the genome
    if len(matches) > 0:
        numMatched += 1
print('%d / %d reads matched exactly!' %(numMatched, len(reads))) # Now calculating matches out of total reads
#100 / 100 reads matched exactly!

#Now let's try with an actual read from fastq file.
#wget --no-check https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/ERR266411_1.first1000.fastq

#Parsing the read and quality strings from a FASTQ file containing sequencing reads
#Read the fastq file and store the sequences into the list sequences[]
def readFastq(filename):
    sequences = []
    qualities = []
    n = 0
    l = []
    with open(filename, 'r') as fh:
        while True:
            fh.readline() #skip name line
            seq = fh.readline().rstrip() #read base sequences
            fh.readline() #skip placeholder line
            qual = fh.readline().rstrip() # read base quality line
            if len(seq) == 0:
                break #end of the file
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities
phix_reads, _ = readFastq("ERR266411_1.first1000.fastq")

#Reads can come from both the strands of the DNA
#Must match not only the forward but also the reverse direction of the genome
#Following function takes a DNA string and returns its reverse complement:
def reverseComplement(s):
    complement = {'A': 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

#Let's do exact matching and count them.
numMatched = 0 #counting the total number of matches
n = 0
for r in phix_reads:
    r = r[:30] #originally r length is 100 so might be too big for pattern matching
    matches = naive(r, genome) # matches is the list of indices where read matches the genome
    matches.extend(naive(reverseComplement(r), genome)) #matching the reverse complement of the read to the genome and adds to the list of matches
    n += 1 #n is the number of reads in the phix_reads
    if len(matches) > 0:
        numMatched += 1
print('%d / %d reads matched exactly!' %(numMatched, n))# Now calculating matches out of total reads
#932 / 1000 reads matched exactly!


genome = readGenome('lambda_virus.dnas')
numMatched = 0 #counting the total number of matches
r = 'AGGT'
r = 'TTAA'
r = 'ACTAAGT'
r = 'AGTCGA'
matches = naive(r, genome)
len(matches)
matchesR = naive(reverseComplement(r), genome) #matching the reverse complement of the read to the genome and adds to the list of matches
len(matchesR)
matches.extend(naive(reverseComplement(r), genome))



#What if we need to do approximate matching and include mismatches. mistmatches = 2
#updating the naive function.
def naive(p, t): #p--> pattern ; t: text file
    occurrences = [] #empty list to record all instances of matching
    for i in range(len(t)-len(p)+1): #outer loop to do alignments over t
        match = True
        count = 0
        for j in range(len(p)):
            if count > 2:
                match = False
                break
            if not t[i+j] == p[j]:#comparing for each position in t with all positions in j
                count += 1
        if match:
            occurrences.append(i)
    return occurrences

