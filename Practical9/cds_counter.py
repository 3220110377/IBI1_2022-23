"""
mRNA sequence begins from 'ATG'
ends at 'TAA' 'TAG' 'TGA'
only one 'ATG' in the sequence
To check the possible coding sequences, I think
find the 'ATG'
check the number of stop codons to get the number of possible coding sequences
"""
import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'  # create a string variable seq
if re.search('ATG', seq):
    new = ''.join(map(str, re.findall(r'ATG.+', seq)))
    print(len(re.findall(r'TAA|TAG|TGA', new)))
else:
    print('no start codon')

