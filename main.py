import random

from DNAToolkit import *
from utilities import color_output

if __name__ == '__main__':
    dna_seq = ''.join([random.choice(DNA_nucleotides)
                       for nuc in range(50)])
    dna_seq = validate_seq(dna_seq)
    print(f'[1] Sequence length: {len(dna_seq)} \n'
          f'[2] Nucleotide frequency: {count_nuc_frequency(dna_seq)} \n'
          f'[3] DNA/RNA transcription: {color_output(transcription(dna_seq))} \n'
          '[4] Reverse complement \n'
          f'\t{color_output(dna_seq)} \n'
          f"\t{''.join(['|' for i in range(len(dna_seq))])} \n"
          f'\t{color_output(reverse_complement(dna_seq))}')
