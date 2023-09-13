# Let's read a fastq file, store the sequences, and base quality info of the reads into a list
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
            if len(seq) == 0: #after reaching the end of the file
                break
            sequences.append(seq)
            qualities.append(seq)
    return sequences, qualities

seqs, quals = readFastq('SRR835775_1.first1000.fastq')

print(seqs[:5])
print(quals[:5])

# Let's first work with the base qualities 
#This function converts phred33 value to quality scores
def phred33toQ(quals):
    return ord(quals) - 33
    
#2 --> low quality score.
#phred33toQ('J') --> 41

#Now create a histogram of quality scores
def createHist(qualities):
    hist = [0] * 60 #length of the hist list is set to 60, will the x-axis
    for qual in qualities: # one string of qualities in a list of qualities
        for phred in qual: # each base in each qual string
            q = phred33toQ(phred) 
            hist[q] += 1 # Count the number of times with that quality score and store the count in the 'qth' position of the list 'hist'. The count will be the y-axis
    return hist
h = createHist(quals)
print(h)

#Plot the histogram
import matplotlib.pyplot as plt
plt.bar(range(len(h)), h)
plt.show()

#GC contents
def findGCByPos(reads):
    gc = [0] * 100 #length of read sequence(100). So plotting GC counts in each of the 100 base positions (x-axis=base position of reads)
    totals =  [0] * 100 # total number of bases at each position #should be equal to total number of reads
    for read in reads: #looping through each sequence in list reads (millions). 
        for i in range(len(read)): #looping through each base position 'i' in the selected sequence read
            if read[i] == 'C' or read[i] == 'G': #seeing if that base position 'i' has C or G
                gc[i]  += 1                      #counting GC content
            totals[i] += 1 #regardless of what that base is, counting the total bases at position 'i'
    for i in range(len(gc)): #Now calculating average GC content
        if totals[i] > 0: # So, we won't get an error when dividing by zero
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


#Generating histogram of low quality score (q<=2)

def findQualsByPos(qualities):
    qualh = [0] * 100
    totals = [0] * 100

    for qual in qualities:
        i = 0
        for phred in qual:
            q = phred33toQ(phred)
            if q <= 10:
                qualh[i] += 1
            totals[i] += 1
            i += 1
        print("Readlength", i)
    for i in range(len(qualh)):
        if totals[i] > 0:
            qualh[i] /= float(totals[i])
    return qualh

qualh = findQualsByPos(quals)
plt.plot(range(len(qualh)), qualh)
plt.bar(range(len(qualh)), qualh)

