"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
        Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated;

Sample Dataset
    >Rosalind_6404
    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    TCCCACTAATAATTCTGAGG
    >Rosalind_5959
    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ATATCCATTTGTCAGCAGACACGC
    >Rosalind_0808
    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output
    Rosalind_0808
    60.919540
"""

from DNAToolkit import gc_content

with open('data', 'r') as file:
    data = file.read()

data = data.split('>')[1:]
ros_dict = {d[0:13]: d[13:].replace('\n', '') for d in data}
result = {key: gc_content(val) for (key, val) in ros_dict.items()}

max_key = max(result, key=result.get)
print(f'{max_key}\n{result[max_key]}')
