import blosum as bl
from itertools import combinations
matrix = bl.BLOSUM(62)  # Import matrix


def seq(name):
    k = ""
    f = open(name, 'r')
    for i in f:
        k = i[:-1]
    return k  # Define the function to take out the sequence


cat = seq('ACE2_cat.fa')
human = seq('ACE2_human.fa')
mouse = seq('ACE2_mouse.fa')
d = {'cat': cat, 'human': human, 'mouse': mouse}  # Make a dictionary for easy recall later


def test(name1, name2):
    x, y = d[name1], d[name2]
    val, n = 0, 0
    for i in range(len(x)):
        val += matrix[x[i]][y[i]]
        if x[i] == y[i]:
            n += 1  # Define functions that look up scores in turn and add them up
    print(open('ACE2_%s.fa' % name1, 'r').read() + '\n' + open('ACE2_%s.fa' % name2, 'r').read() + '\n' +
          'Scores =' + str(val) + '\n' + 'Percentage =' + str(n/len(x)))


L = ["cat", "human", "mouse"]
c = combinations(L, 2)
for a, b in c:
    test(a, b)  # All cases of ranking combinations
"""
Cats and humans were the most similar, followed by rats and humans, and the least similar was cats and rats.
"""