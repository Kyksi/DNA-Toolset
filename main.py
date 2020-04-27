import random

from DNAToolkit import *

if __name__ == '__main__':
    dna_seq = ''.join([random.choice(Nucleotides)
                       for nuc in range(50)])
    print(' '.join([str(val) for key, val in count_nuc_frequency(dna_seq).items()]))
