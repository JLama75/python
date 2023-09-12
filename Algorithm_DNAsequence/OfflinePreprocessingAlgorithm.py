
#Preprocessing.
#Algorithm that preprocesses Text 'T' is offline. Otherwise, the algorithm is online

#Web search engine and Read alignment is offline algorithms. 
#Exact matching and Boyer-Moore algorithms is online algorithms as they do no use preprcessed texts.

#Offline algorithms: Taking the reference genome and preprocessing it somehow in a way it matches many different reads faster
#Gnerating Index of Text/T: List of pairs of substring of cetain length(kmer) and corresponding offsets/positions in the genome where they occur
#You querry the substring (k-mer) of pattern into the index. You get an index hit and it provides you the offset value: Basically tells you where in the text do you find that pattern
#Then next step is verification: Does the remaining of the substring also match or not.

#Data structure: Multimap: its a map that associates k-mers (keys) with values (offsets in the genome)
#Data structure could be implemented by a) Ordered list b) Hash table (more used)

#a) Ordered list: presents a map that associates k-mers (keys) with values (offsets in the genome) that is ordered alphabetically
#In this case Query is done through binary search: total bisection ~ log2(n) bisections per query
#We can use in-built python module: bissect (collection of related python functions and classes)

#bisect.bisect_left(a,x) #where a is the list and x is the pattern

#Following is an example of how bisect_left works
a = [1, 3, 3, 6, 8, 8, 8, 9, 10] #ordered list
import bisect
bisect.bisect_left(a,2) ## Gives leftmost offset where x can be inserted into 'a' to maintain order in a sorted list. a must be a sorted/ordered list!
#output: 1
#a.insert(bisect.bisect_left(a,2), 2)
#Now in case the x matches the value in a
bisect.bisect_left(a,8) 
#output: 4
# gives the offset where 8 is present. So this can be used in substring matching too as used later.

#Example 2 using tupules of substring of 3-mer length 

table = [('GAA', 2), ('GAG', 3), ('GGG', 4)]
bisect.bisect_left(table, ('GGG', -1))
#output: 2 #Its giving the position of (GGG,4) in the list. So, we can use this method for matching.
bisect.bisect_left(table, ('GGC', -1))
#output: 2 # There is no GGC in the list but also it gives the same offset as before because GGC would be ordered before GGG. 
#So be careful when using bisect to match you must do additional validation.

#b) Hash table
#has an array of empty buckets. As we add items to the hash bucket it becomes a list.
# #We use hash function h that maps 3-mers(keys) to buckets.
# #Each bucket will have key-value pair + additional empty bucket that can be also filled with key-value pair
#Each bucket is like a Aisle in a grocery store with a group of items
#hash collision- the key being added falls in the same bucket as a different key added previously

t = 'GTGCGTGTGGGGG' #text
#lets make hash with the above text with the use of dictionary. Taking substring of 3-mers associated with a list of offsets/positions where the substring is found in the text
table = {'GTG': [0, 4, 6], 'TGC' : [1],
         'GCG' : [2], 'CGT': [3], 'TGT' : [5],
         'TGG':[7], 'GGG':[8, 9, 10]}

table['GGG'] #dic[key] gives value
table['CGT']

import bisect
#Now make a class index that preprocesses the text into hash and then if given a pattern also querries the index 
########################
class Index(object):
    #two methods: one that preprocesses the text into index, second method that querries the index
    def __init__(self, t, k): #t is the text/string, k is the k-mer for indexing
        self.k = k #set variables
        self.index = [] #list
        #loop through the text t, take every k-mer of length k and add to the index along with their offset
        #makes this index at the construction of the class
        for i in range(len(t) - k + 1): #gives all index such that k-mer doesn't go past the text
            self.index.append((t[i:i+k], i)) #appending. if i =0 and k=3, then we have tuppule (t[0:3], 0) = (GTG, 0)
        self.index.sort() #order them #might take some time

# takes in the pattern 'p' as query, makes a substring of k-mer length, searches it in index, checks if pattern matches in that position, if matched appends on hits
#takes in 'p' and returns all positions where k-mers of p matches k-mers of T.
# Its not a complete match as it still requires verification later on (does all characters in p, not just substring, match that position in T).
    def query(self, p):
        kmer = p[:self.k]
        #bisect_left(index, 'GTG')
        i = bisect.bisect_left(self.index, (kmer, -1)) #sending tupules in the module bisect. -1: all indices in the list > -1
        #bisect_left gives info about the bucket number
        hits = []
        while i < len(self.index): #since the offset provided by bisect could mean a match or not. There could also be multiple matches beyond the bisect position. Therefore performing additional validation starting from left to end
            if self.index[i][0] != kmer: #compares text substring in index at i position to the pattern substring 
                break
            hits.append(self.index[i][1]) #append the offset which is the second value of tupule
            i += 1
        return hits #could have multiple offsets/positions in the hits

#####################

def queryIndex(p, t, index): #index is an object of class Index
    k = index.k #accessing index class variable 'k'. #object.variable
    offsets = []
    #verification step
    for i in index.query(p): #calling query function within the index class. #object.function(parameters)
         #looping through the multiple offsets/positions and performing additional verification
        if p[k:] == t[i+k:i+len(p)]: # if k =3, len(p) = 6, i = 100 then, t[103:106]
            offsets.append(i)
    return offsets #is the final position where pattern matches text

##########################

t = 'GCTACGATCTAGAATCTA'
p = 'TCTA'

index = Index(t, 2) #create an object index in class Index. #index is created
print(queryIndex(p, t, index)) #The function queryIndex calls query function of Index class within it. 

#verify the patterns
t[7:11]
t[14:18]
