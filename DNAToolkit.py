from structures import DNA_nucleotides


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
