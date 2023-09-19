#Greedy shortest common superstring algorithm:
#locate the edge that corresponds to the greatest overlap. Then combine the two nodes/strings together to have a new string.
#Then using the new string search for the edit distance/edge with the greatest overlap again. Repeat the process.
#Cost: not always the correct answer. Also not applicable when we have repetitive regions as is true with the genome.

#              AAA AAB ABB BBA BBB
#merging nodes#AAAB ABB BBA BBB
#              |
#scs: AAABBABBB <-- length = 9
#true scs: AAABBBA <-- length = 7

def pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    for a,b in itertools.permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen

def greedy_scs(reads, k):
    read_a, read_b, olen = pick_maximal_overlap(reads, k)
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads) #even though there are no more overlaps/edges in the overlap graph but there still are reads/nodes left we would concatinate them as well.

greedy_scs(['ABC', 'BCA', 'CAB'], 2)
#'CABCA'
greedy_scs(['ACGGTACGAGC', 'GAGCTTCGGA', 'GACACGG'], 2)
#'GACACGGTACGAGCTTCGGA'
'GACACGGTACGAGCTTCGGA' == 'GACACGGTACGAGCTTCGGA'

greedy_scs(['ABCD', 'CDBC', 'BCDA'], 1)
#output: 'CDBCABCDA'
#True short superstring. (#for scs function please view GenomeAssembly_ShortestCommonSuperstring.py file.)
scs(['ABCD', 'CDBC', 'BCDA'])
#output: 'ABCDBCDA' 
