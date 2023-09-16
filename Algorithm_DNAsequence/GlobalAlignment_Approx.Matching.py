#Global and local alignment using edit distance

#Global Alignment: This is concerned with the overall similarity between two strings X and Y.

#Penalties:
#Substitution types: Transitions (purine to purine) and Transversions (purine to pyrimidine): Transitions are more frequent than transversions
#A:G (purines), C:T (pyrimidines)--> Transitions
#Gaps(Indel rates) are less frequent than substitution rates
#Panalties of Tranversions and gaps should be more
#So we make a penalty matrix that has penalty scores for gaps and substitutions.

#Local alignment:
#We do not look for edit distances between two strings in local alignments.
#We look for substrings of X and Y which are most similar to each other.
#Uses scoring matrix instead of penalty matrix. In the scoring matrix, matches are positive and differences are negative.
#The goal is to pop out the matches.


#Let's start with global alignment:
#Panalities for purine to purine or pyrimidine to pyrimidine substitution = 2; rest 4. Gaps = 8
# Two-dimensional (4X4) array penalty scores for different mismatches and gaps
#      A  C  G  T  Gap
#   A  0  4  2  4   8
#   C  4  0  4  2   8
#   G  2  4  0  4   8
#   T  4  2  4  0   8
#  Gap 8  8  8  8   8

alphabet = ['A', 'C', 'G', 'T']
score = [[0, 4, 2, 4, 8], \
         [4, 0, 4, 2, 8], \
         [2, 4, 0, 4, 8], \
         [4, 2, 4, 0, 8], \
         [8, 8, 8, 8, 8]]

def globalAlignment(x, y):
    D = []
    for i in range(len(x) + 1):
        D.append([0]* (len(y)+1)) #making a matrix for x and y including empty string/gaps, where x is pattern and y is text/genome with elements '0'

    for i in range(1, len(x) + 1):
        # when skipping characters in 'y'. #D[i][0] corresponds to all rows of 1st column (empty String/gap of y/text) except '0'th row
        #To calculate the penalty score look at the rows of the penalty matrix corresponding to the character in the pattern or x
        D[i][0] = D[i-1][0] + score[alphabet.index(x[i-1])][-1] #alphabet.index gives you the position/index of that xth character in the list, alphabet(0 to 3). score[][-1] searches in the last column of the matrix, score
    for i in range(1, len(y) + 1):
        # when skipping characters in 'x'. #D[0][i] corresponds to all columns of 1st row (empty String/gap of x/text) except '0'th column
        D[0][i] = D[0][i-1] + score[-1][alphabet.index(y[i-1])]

    for i in range(1, len(x) + 1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + score[-1][alphabet.index(y[j-1])]
            distVer = D[i-1] [j] + score[alphabet.index(x[i-1])][-1]
            if x[i-1] == y[j-1]:
                distDiag = D[i-1] [j-1]
            else:
                distDiag = D[i - 1][j - 1] + score[alphabet.index(x[i-1])][alphabet.index(y[j-1])]
            D[i][j] = min(distHor, distVer, distDiag)
    return D[-1][-1]
  
x = 'TACCAGATTGA'
y = 'TACCAAATTG'
print(globalAlignment(x,y))
#10
