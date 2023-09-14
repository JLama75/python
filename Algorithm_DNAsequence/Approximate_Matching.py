#Check BoyerMooreClass.py to get the code where I defined the class called BoyerMoore, which is used later on.
def boyer_moore(p, p_bm, t):
    i = 0
    occurrences = [] #list to store indices that give matches
    while i < len(t) - len(p) + 1:
        shift = 1 #default shift is 1
        mismatched = False #initialize the boolean variable 'mismatch' to false
        for j in range(len(p) -1, -1, -1):#inner loop goes from len(p)-1 backwords until just before -1
            if not p[j] == t[i+j]: #incase there is a mismatch
                #Calculate how many alignments to shift. Using the preprocessing function
                skip_bc = p_bm.bad_character_rule(j, t[i+j]) #object.functionWithinClass(parameters)
                skip_gs = p_bm.good_suffix_rule(j, t[i+j]) #parameters= offset where mismatch occurs, mistmatching text 't'
                shift = max(shift, skip_bc, skip_gs) #whichever is the largest will save us the most time
                mismatched = True #set mismatch to True and break
                break
        if not mismatched: #If there was no mismatch
            occurrences.append(i) #gives the offset/postition where the match occured
            skip_gs = p_bm.match_skip() #still needs to shift using good suffix (gs) rule
            shift = max(shift, skip_gs)
        i += shift #make the shift
    return occurrences

t = 'GCTACGATCTAGAATCTA'
p = 'TCTA'
#creating BoyerMoore object that will preprocess the pattern p and gives you how many indices to skip
p_bm = BoyerMoore(p) #calling function
boyer_moore(p, p_bm, t)

#Using approximate match algorithm using segmentation by applying the Pigeonhole algorithm.
#Essentially we divide the pattern into segments (segment length = mismatches(n) + 1), such that worst case we still have one segment without any mismatches. 
#We check each segment through the typical exact matching algorithm (Naive or Boyer-Moore method), which returns you the positions in the genome/text where the matching occurred.
#Then we must align the rest of the segments that likely have the mismatches through character matching (matching each character of the remaining segments of the pattern with the corresponding character in the genome/text)
#and count the number of mismatches so that only reporting those offsets/GenomicPositions where the mismatches are <= n.


#segment the pattern by 1 + max no. of mismatches. Even in the worst-case scenario, one segment should have an exact match to the text.
#So perform exact matching (BoyerMoore) on all the segments generated from pattern 'p'.

def approximate_match(p, t, n): #n: max no. of mismatches
#how many segments = no. of mismatches + 1
    segment_length = int(round(len(p)/ (n+1)))
    all_matches = set() #would only store unique matches, not duplicates
    for i in range(n+1):
        start = i*segment_length
        end = min((i+1)* segment_length, len(p)) #resizing the last length of the segment since some segments would be short
        #Passing the specific segment to BoyerMoore 
        p_bm = BoyerMoore(p[start:end], alphabet='ACGT')#makes the good character and bad suffix rule matrices
        matches = boyer_moore(p[start:end], p_bm, t)
        #If perfect/exact match then it returns one or more positions/offsets in the genome where the start of the segment matched

        #Now using each of those genomic positions/offsets (m), we will do character matching of the remaining segments of the pattern to the corresponding regions in the genome
        for m in matches:
            if m < start or m+len(p)-start > len(t): #to make sure our pattern does not run off at the beginning or the end of t. (len(p) - start tells you the remaining characters to be matched)
                continue
            mismatches = 0
            for j in range(0, start): #Character matching the leftmost remaining segments
                if not p[j] == t[m-start+j]: #(m-start) takes it to the position corresponding to the starting point of the pattern. + j allows for matching of the next corresponding character
                    mismatches += 1 #counting mismatches
                    if mismatches > n:
                        break

            for j in range(end, len(p)): #Character matching the rightmost remaining segments
                if not p[j] == t[m-start+j]: #(m-start) takes it to the position corresponding to the starting point of the pattern. + j allows for matching of the next corresponding character
                     mismatches += 1 #counting mismatches
                     if mismatches > n:
                        break
            if mismatches <= n: #reporting only those with mismatches <= n
                all_matches.add(m - start)
    return list(all_matches)


p = 'AACTTG'
t = 'CACTTAATTG'
print(approximate_match(p, t, 2))
