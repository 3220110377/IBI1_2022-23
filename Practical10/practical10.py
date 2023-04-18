"""
just compare the value and five times of salary
"""


def buy_house(value, salary):
    return value >= 5*salary


buy_house(180000, 35000)  # It's a test, the output is True

"""
create a class called Triathlon
In the class, the first function is used to keep the information
the second function is used to output the information
"""


class Triathlon(object):
    def __init__(self, first_name, last_name, location, swim, cycle, run, total):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim = swim
        self.cycle = cycle
        self.run = run
        self.total = total

    def output(self):
        print('name:' + self.first_name + ' ' + self.last_name + '  ' + 'location:' + self.location + '  ' +
              'swim:' + self.swim + '  ' + 'cycle:' + self.cycle + '  ' + 'run:' + self.run + '  ' + 'total:'
              + self.total)


robert_young = Triathlon('robert', 'young', 'UK', '1h', '2h', '3h', '6h')
robert_young.output()  # It's a test, output is 'robert young  location:UK  swim:1h  cycle:2h  run:3h  total:6h'

"""
Write a function to determines whether the given DNA sequence is likely to be protein-coding or not.
So we should test whether the string between opening codon and stop codon is more than 50% of the total DNA
To make it easier, we just consider 'TGA' as stop codon and if there are many sequences, we just test the sequences 
which contain the first 'ATG' and the first 'TGA' 
"""


def test(sequence):
    import re
    k = ''
    n = False
    if re.findall(r'ATG', sequence):
        new = ''.join(map(str, re.findall(r'ATG(.+)', sequence)))
        new = re.findall(r'\w{3}', new)  # find the 'ATG' opening codon and split the sequences after that in 3
        for i in new:
            if i == 'TGA':
                n = not n
                break  # When the 'TGA' stop codon is found, jump out
            k = k + i
        if n:  # n means whether there is a 'TGA' stop codon
            if len(k)/len(sequence) >= 0.5:
                print("It's protein-coding")
            elif len(k)/len(sequence) <= 0.1:
                print("It's non-coding")
            else:
                print("It's unclear")
        else:
            print("It's non-coding")
    else:
        print("It's non-coding")  # If there is no 'ATG' opening codons, output 'It's non-coding'


test('ATGATGACTTAATGATGATGA')  # It's protein-coding
test('TATGTGAA')  # It's non-coding
test('CTATCTATGTCTATCATCTACTATCTACTAATGTGAGTAGATGATGATAGTAGTAGATGATAGATGATGATGATGATGATGATAGTATCTCT')  # It's unclear
test('TGATGATGATAGTGATGATGATGATAGTA')  # It's non-coding
test('AAAAAAAAAAAAA')  # It's non-coding
