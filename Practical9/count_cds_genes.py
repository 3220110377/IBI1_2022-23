"""
collect the input and read the file including sequences
find the sequences ends with input and write them in the file called input_stop_genes.fa
"""
import re
Input = input('Please input the stop codon like TAA, TAG and TGA')
Open1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
Open2 = open('%s_stop_genes.fa' % Input, 'w')  # make a file including input
f = Open1.read()
n = f.split('>')  # split the file with >
k = 0
for i in n:
    if re.findall(Input+r'\n$', i):  # find the sequence end with input
        t = re.sub(r'\n', '', n[k])  # delete the \n
        Open2.write('>' + ''.join(re.findall(r' gene:(.+?) ', t)) + ' ' + str(len(re.findall(Input, t))) + '\n' +
                    ''.join(re.findall(r'](.+)', t)) + '\n')  # output
    k += 1  # record the number of the sequence in the list
