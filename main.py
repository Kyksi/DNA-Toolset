import random

from DNAToolkit import *
from utilities import color_output

if __name__ == '__main__':
    dna_seq = ''.join([random.choice(DNA_nucleotides)
                       for nuc in range(50)])
    dna_seq = validate_seq(dna_seq)
    print(f"[1] Sequence length: {len(dna_seq)} \n"
          f"[2] Nucleotide frequency: {color_output(str(count_nuc_frequency(dna_seq)))} \n"
          f"[3] DNA/RNA transcription: {color_output(transcription(dna_seq))} \n"
          "[4] DNA string + Complement + Reverse Complement \n"
          f"\t5' {color_output(dna_seq)} 3'\n"
          f"\t   {''.join(['|' for i in range(len(dna_seq))])} \n"
          f"\t3' {color_output(reverse_complement(dna_seq)[::-1])} 5' [Complement]\n"
          f"\t5' {color_output(reverse_complement(dna_seq))} 3' [Reverse Complement]\n"
          f"[5] GC content: {gc_content(dna_seq)}% \n"
          f"[6] GC content in subsection k=20: {gc_content_subsec(dna_seq, k=20)}")
