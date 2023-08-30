#Boyer-Moore:
#skipping some uneccessary alignment

#We will try alignments in left-to-right order, and try
#character comparisons in right-to-left order
#P:word
#T:There would have been a time for such a word
#   -------word---------------------------->
#           <--

#Bad character Rule:
#Upon mismatch, skip alignments until (a) mismatch becomes a match, or (b) P moves past mismatched character

#Good suffix rule: Let t=substring matched by inner loop: skip until (a) there are no mismatches between P and t or (b)
#P moves past t

#So, using those rules it skips alignments and is faster than naive exact matching

#Boyer-Moore:Prerocessing
#Pre-calculate skips. For bad character rule, P =TCGC: look up tables

#Creating a boyer_moore function that takes a pattern, text and preprocessed boyerMoore object
#This function does the alignment and character matching by skipping/shifting past unncessarry alignments using info provided by boyerMoore object

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

#double check the offset
t[7:11]
t[14:18]

