
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

#Using approximate match algorithm using segmentation by applying Pigeonhole algorithm
#segment the pattern by 1 + max no. of mismatches. Even in worst case senario one segment should has exact match to the text.
#So perform exact matching (BoyerMoore) on all the segements generated from pattern 'p'.
def approximate_match(p, t, n): #n: max no. of mismatches
#how many segments = no. of mismatches + 1
    segment_length = int(round(len(p)/ (n+1)))
    all_matches = set() #would only store unique matches not duplicates
    for i in range(n+1):
        start = i*segment_length
        end = min((i+1)* segment_length, len(p)) #resizing the last lenght of segment
        p_bm = BoyerMoore(p[start:end], alphabet='ACGT')#makes the good character and bad suffix rule matrices
        matches = boyer_moore(p[start:end], p_bm, t)

        for m in matches:
            if m < start or m+len(p)-start > len(t): #to make sure our pattern does not run off in the begininning or the end of t
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


p = 'AACTTG'
t = 'CACTTAATTG'
print(approximate_match(p, t, 2))
