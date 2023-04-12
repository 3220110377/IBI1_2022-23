import re
Open1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
Open2 = open('TGA_genes.fa', 'w')
f = Open1.read()
n = f.split('>')
k = 0
for i in n:
    if re.findall(r'TGA\n$', i):
        t = re.sub(r'\n', '', n[k])
        Open2.write('>' + ''.join(re.findall(r' gene:(.+?) ', t)) + '\n' + ''.join(re.findall(r'](.+)', t)) + '\n')
    k += 1







