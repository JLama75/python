#Boyer-Moore: Does alignment while skipping some unnecessary alignments
#           : Does alignments in left-to-right order, and character comparisons in right-to-left order

#Rules:
#1) Bad character Rule:
#Upon mismatch, skip alignments until (a) mismatch becomes a match, or (b) P moves past mismatched character
#2) Good suffix rule: Let t=substring matched by inner loop: skip until (a) there are no mismatches between P and t or (b)P moves past t
#So, using these two rules it skips alignments and is faster than naive exact matching. Which rule to use depends on which rule gives maximum number of skips.

#Processing steps: Pre-calculates skips. For example, you can calculate the total number of shifts/skips using the two rules for the pattern(P) = TCGC. It makes a look-up table with the shift values

#Now let's create a boyer_moore function that takes a pattern, text, and preprocessed boyerMoore object
#This function does the alignment and character matching by skipping/shifting past unnecessary alignments using the info provided by the boyerMoore object

def boyer_moore(p, p_bm, t):
    i = 0
    occurrences = [] #list to store indices that give matches
    while i < len(t) - len(p) + 1:
        shift = 1 #default shift is 1
        mismatched = False # Initialize the boolean variable 'mismatch' to false
        for j in range(len(p) -1, -1, -1):#inner loop goes from len(p)-1 backward until just before -1
            if not p[j] == t[i+j]: #incase there is a mismatch
                #Calculate how many alignments to shift by calling the preprocessing function, bad character rule, and good suffix rule
                skip_bc = p_bm.bad_character_rule(j, t[i+j]) #object.functionWithinClass(parameters)
                skip_gs = p_bm.good_suffix_rule(j, t[i+j]) #parameters= offset where mismatch occurs, mismatching text 't'
                shift = max(shift, skip_bc, skip_gs) #whichever is the largest will save us the most time
                mismatched = True #set mismatch to True and break
                break
        if not mismatched: #If there was no mismatch
            occurrences.append(i) #gives the offset/position where the match occurred
            skip_gs = p_bm.match_skip() #still needs to shift using the good suffix (gs) rule
            shift = max(shift, skip_gs)
        i += shift #make the shift and skips unnecessary alignments
    return occurrences

t = 'GCTACGATCTAGAATCTA'
p = 'TCTA'
# Creating a BoyerMoore object that will preprocess the pattern p and give you how many indices to skip
p_bm = BoyerMoore(p) #creating p_bm object by calling the BoyerMoore class
boyer_moore(p, p_bm, t)

#double check the offset
t[7:11]
t[14:18]

