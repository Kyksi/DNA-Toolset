from collections import Counter

from structures import DNA_nucleotides, DNA_codons


def validate_seq(dna_seq: str) -> [bool, str]:
    """Check the sequence to make sure it is a valid DNA string"""

    dna_seq = dna_seq.upper()
    for nuc in dna_seq:
        if nuc not in DNA_nucleotides:
            return False
    return dna_seq


def count_nuc_frequency(dna_seq: str) -> [str, int]:
    """Count nucleotides in a given DNA string"""

    frq_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nuc in dna_seq:
        frq_dict[nuc] += 1
    return frq_dict


def transcription(dna_seq: str) -> str:
    """
    Conversion DNA to RNA
    Replacing Thymine with Uracil
    """

    return dna_seq.replace('T', 'U')


def reverse_complement(dna_seq: str) -> str:
    """
    Swapping Adenine with Thymine and Guanine with Cytosine.
    Reversing newly generated string.
    """

    mapping = str.maketrans('ATCG', 'TAGC')
    return dna_seq.translate(mapping)[::-1]


def gc_content(seq: str) -> float:
    """GC Content in a DNA/RNA sequence"""

    return round(((seq.count('G') + seq.count('C')) / len(seq) * 100), 3)


def gc_content_subsec(seq: str, k=10) -> list:
    """GC Content in a DNA/RNA sub-sequence length k"""

    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res


def translate_seq(dna_seq: str, init_pos=0) -> DNA_codons:
    """Translates a DNA sequence into an aminoacid sequence"""

    return [DNA_codons[dna_seq[pos:pos + 3]] for pos in range(init_pos, len(dna_seq) - 2, 3)]


def codon_usage(dna_seq: str, aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    
    tmp_list = []
    for i in range(0, len(dna_seq) - 2, 3):
        if DNA_codons[dna_seq[i:i + 3]] is aminoacid:
            tmp_list.append(dna_seq[i:i + 3])
    freq_dict = dict(Counter(tmp_list))
    total = sum(freq_dict.values())
    for seq in freq_dict:
        freq_dict[seq] = round(freq_dict[seq] / total, 2)
    return freq_dict
