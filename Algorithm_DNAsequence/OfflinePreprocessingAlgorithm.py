
#Preprocessing.
#Algorithm that preprocesses T is offline. Otherwise, the algorithm is online

#Web search engine and Read alignment is offline algorithms
#Taking the reference genome and preprocessing it somehow in a way it matches many different reads faster
#offline algorithm: Preprocess T
#Index of T: List of pairs of substring of cetain length(kmer) and offsets of genome where they occur
#You querry the substring (k-mer) of pattern into the index. You get an index hit and it provides you the offset value
#Then next step is verification: Does the remaining of the substring also match or not.

#Data structure: Multimap: its a map that associates k-mers (keys) with values (offsets in the genome)
#Data structure could be implemented by a) Ordered list b) Hash table (more used)
#Ordered list presents a map that associates k-mers (keys) with values (offsets in the genome) that is ordered alphabetically
#Query is done through binary search: total bisection ~ log2(n) bisections per query
#Module: bissect (collection of related python functions and classes)
#bisect_left(index, 'GTG')

a = [1, 3, 3, 6, 8, 8, 8, 9, 10] #ordered list
import bisect
bisect.bisect_left(a,2)
#bisect_left(index, 'GTG')
#bisect.bisect_left(a,x)
#leftmost offset where x can be inserted into a to maintain order

#Hash table
#has an array of empty buckets. As we add items to the hash bucket it becomes a list.
# #We use hash function h that maps 3-mers(keys) to buckets.
# #Each bucket will have key-value pair+ additional empty bucket that can be also filled with key-value pair
#Each bucket is like a Aile in a grocery store.
#hash collision- the key being added falls in the same bucket as a different key added previously
t = 'GTGCGTGTGGGGG'
table = {'GTG': [0, 4, 6], 'TGC' : [1],
         'GCG' : [2], 'CGT': [3], 'TGT' : [5],
         'TGG':[7], 'GGG':[8, 9, 10]}
table['GGG']
table['CGT']


import bisect
########################
class index(object):
    #two methods: one that preprocesses the string, second that querries the index
    def __intit__(self, t, k): #t is the text/string, k is the k-mer for indexing
        self.k = k #set variables
        self.index = [] #
        #loop through the text t, take every k-mer of length k and add to the index along with their offset
        for i in range(len(t) - k + 1): #gives all index such that k-mer doesn't past the text
            self.index.append((t[i:i+k], i)) #appending. if i =0 and k=3, then we have tuppule (t[0:3], 0)
        self.index.sort() #order them #might take some time

# takes in the pattern 'p' as query, makes a substring o length kmer, searches it in index, checks if pattern matches in that position, if matched appends on hits
#takes in 'p' and returns all positions where k-bases of p matches k-bases of T.
# Its not a complete match as it still requires verification later on (does all p match that position in T).
    def query(self, p):
        kmer = p[:self.k]
        i = bisect.bisect_left(self.index, (kmer, -1)) #sending tupules in the module bisect. -1: all indices in the list > -1
        #bisect_left gives info about the bucket number
        hits = []
        while i < len(self.index):
            if self.index[i][0] != kmer: #if that location in the index is not equal to kmer
                break
            hits.append(self.index[i][1]) #append the offset which is the second value of tupule
        return hits

#####################

def queryIndex(p, t, index):
    k = index.k
    offsets = []
    for i in index.query(p): #verification
        if p[k:] == t[i+k:i+len(p)]:
            offsets.append(i)
    return offsets

##########################

t = 'GCTACGATCTAGAATCTA'
p = 'TCTA'

index = Index(t, 2)
print(queryIndex(p, t, index))

#verify
t[7:11]
t[14:18]
