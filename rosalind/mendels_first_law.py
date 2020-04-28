"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
        k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing
        a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Sample Dataset
    2 2 2
Sample Output
    0.78333
"""

dominant, hetero, recessive = 16, 27, 30
total = dominant + hetero + recessive

r_r = (recessive/total) * ((recessive-1)/(total-1))
h_h = (hetero/total) * ((hetero-1)/(total-1)) * 1/4
h_r = ((hetero/total) * (recessive/(total-1)) + (recessive/total) * (hetero/(total-1))) * 1/2

recessive_total = r_r + h_h + h_r
print('{:.5f}'.format(1-recessive_total))
