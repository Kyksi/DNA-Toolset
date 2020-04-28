"""
Problem
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT

Sample Output
    7
"""

with open('data', 'r') as f:
    dna_strings = [line.strip() for line in f.readlines()]

ham_distance = sum([a != b for a, b in zip(dna_strings[0], dna_strings[1])])
print(ham_distance)
