########################
#Write a program that performs index-assisted approximate matching. Make an 8-mer index of the text/genome and perform a query-based search in the index.
#Assume pattern P has length 24, and look for approximate matches up to 2 mismatches (substitutions)
class Index(object):
    def __init__(self, t, k): #t is the text/string, k is the k-mer for indexing. k-mer =8
        self.k = k 
        self.index = [] 
        #loop through the text t, take every k-mer of length k, and add to the index along with their offset
        for i in range(len(t) - k + 1):
            self.index.append((t[i:i+k], i)) #if i =0 and k=3, then we have tuple (t[0:3], 0) = (GTG, 0)
        self.index.sort() 

# takes in the pattern 'p' as query, makes a substring of k-mer length, searches it in the index, checks if the pattern matches in that position if matched appends on hits
    def query(self, p):
        kmer = p[:self.k]
        #bisect_left(index, 'GTG')
        i = bisect.bisect_left(self.index, (kmer, -1)) #sending tupules in the module bisect. -1: all indices in the list > -1
        hits = []
        while i < len(self.index): #since the offset provided by bisect could mean a match or not. There could also be multiple matches beyond the bisect position. Therefore performing additional validation starting from leftmost position to end
            if self.index[i][0] != kmer: #compares text/genome substring in the index of i position to the pattern substring
                break
            hits.append(self.index[i][1]) #append the offset, which is the second value of tuple
            i += 1
        print("hits: ", hits)
        print("length hits: ", len(hits))
        return hits #could have multiple offsets/positions in the hits

def queryIndex(p, t, index): #index is an object of class Index
    k = index.k 
    offsets = []
    #verification step
    for i in index.query(p): #calling query function within the index class. #object.function(parameters)
         #looping through the multiple offsets/positions and performing additional verification
        if p[k:] == t[i+k:i+len(p)]: # if k =3, len(p) = 6, i = 100 then, t[103:106]
            offsets.append(i)
    return offsets #is the final position/offset where the pattern matches the text/genome


#####################

def approximate_match(p, t, n): #n: max no. of mismatches
#how many segments = no. of mismatches + 1
    segment_length = int(round(len(p)/ (n+1)))
    all_matches = set() #would only store unique matches, not duplicates
    for i in range(n+1): #does alignment for each segment
        print("segment: ", i)
        start = i*segment_length
        end = min((i+1)* segment_length, len(p)) #resizing the last length of the segment as some segments might be shorter 
        index = Index(t,8) #k-mer = 8
        matches = queryIndex(p[start:end], t, index)
        #We now have one or more positions where the segment matches
        #Performing character alignment for the remaining segments of the pattern to the corresponding positions in the genome, counting the mismatches, and only reporting those with mismatches <= 2
        for m in matches:
            if m < start or m+len(p)-start > len(t): #to make sure our pattern does not run off at the beginning or the end of t
                continue
            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            for j in range(end, len(p)):
                if not p[j] == t[m-start+j]:
                     mismatches += 1
                     if mismatches > n:
                        break
            if mismatches <= n:
                all_matches.add(m - start)
    return list(all_matches)

p = 'GGCGCGGTGGCTCACGCCTGTAAT'
match = approximate_match(p, genome, 2)
len(match)
#19
#90
##################################################################################################
