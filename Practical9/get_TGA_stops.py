"""
read the content of the file
find the sequences end with TGA
write these sequences in the new file called TGA_genes.fa
"""
import re
Open1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
Open2 = open('TGA_genes.fa', 'w')
f = Open1.read()
n = f.split('>')  # split the content with >
k = 0
for i in n:
    if re.findall(r'TGA\n$', i):  # find the sequences end with TGA
        t = re.sub(r'\n', '', n[k])  # delete the \n in the sequence
        Open2.write('>' + ''.join(re.findall(r' gene:(.+?) ', t)) + '\n' + ''.join(re.findall(r'](.+)', t)) + '\n')
        # output
    k += 1  # record the number of the sequence in the list







