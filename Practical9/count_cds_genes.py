import re
Input = input('Please input the stop codon like TAA, TAG and TGA')
Open1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
Open2 = open('%s_stop_genes.fa' % Input, 'w')
f = Open1.read()
n = f.split('>')
k = 0
for i in n:
    if re.findall(Input+r'\n$', i):
        t = re.sub(r'\n', '', n[k])
        Open2.write('>' + ''.join(re.findall(r' gene:(.+?) ', t)) + ' ' + str(len(re.findall(Input, t))) + '\n' + ''.join(re.findall(r'](.+)', t)) + '\n')
    k += 1
