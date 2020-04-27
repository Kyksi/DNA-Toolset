import random

from DNAToolkit import *

if __name__ == '__main__':
    dna_seq = ''.join([random.choice(DNA_nucleotides)
                       for nuc in range(50)])
