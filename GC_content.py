#Lets read a fastq file, store the sequences and base quality info of the reads into a list
#Convert the ASCII value of base quality into an integer score and create a histogram
#
def readFastq(filename):
    sequences = [] # empty list
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(seq)
    return sequences, qualities

seqs, quals = readFastq('SRR835775_1.first1000.fastq')

print(seqs[:5])
print(quals[:5])

# Let's first work with the base qualities 
def phred33toQ(quals):
    return ord(quals) - 33

phred33toQ('#')
#2 --> low quality score.
phred33toQ('J')
#41
def createHist(qualities):
    hist = [0] * 60 #length of the hist list is set to 60
    for qual in qualities: # one string of qualities in a list of qualities
        for phred in qual: # each base in each qual string
            q = phred33toQ(phred) # convert character to quality score
            hist[q] += 1 # Count the number of times with that quality score and store the count in 'q' position of list 'hist'
    return hist
h = createHist(quals)
print(h)

#Plot the histogram
import matplotlib.pyplot as plt
plt.bar(range(len(h)), h)
plt.show()

#GC contents
def findGCByPos(reads):
    gc = [0] * 100 #length of each sequence is 100. So putting gc counts in 100 positions (x-axis)
    totals =  [0] * 100 # total number of bases at each position #should be equal to total number of reads

    for read in reads: #looping through each sequence in list reads. reads is a list of 1000s of sequences
        for i in range(len(read)): #looping through each base position 'i' in the selected sequence read
            if read[i] == 'C' or read[i] == 'G': #seeing if that base position 'i' has C or G
                gc[i]  += 1                      #counting incase it is a G or C
            totals[i] += 1 #regardless what that base is, counting the total bases in position 'i'

    for i in range(len(gc)): #Now calculating average GC content
        if totals[i] > 0: # So, we won't get error by dividing by zero
            gc[i] /= float(totals[i]) #total CG count at that position/ Total bases at that position
    return gc
  
# Gererating histogram of GC content
gc = findGCByPos(seqs)
plt.plot(range(len(gc)), gc)
plt.show()

#Distributions of bases in the sequences.
import collections
count = collections.Counter() #counts the number of each bases
for seq in seqs:
    count.update(seq)
print(count)
#N base is when the base caller has no confidence at all and doesn't want to make a call.
