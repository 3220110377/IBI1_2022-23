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
if re.search('ATG', seq):  # make sure there is ATG sequence
    new = ''.join(map(str, re.findall(r'ATG.+', seq)))  # view the sequence begins with ATG as new sequence
    print(len(re.findall(r'TAA|TAG|TGA', new)))  # count the number of stop codons in the new sequence
else:
    print('no start codon')  # If there is no start codon, print no start codon

