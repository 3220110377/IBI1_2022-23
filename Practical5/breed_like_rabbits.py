"""
when the number of rabbits less than 100, double the number of rabbits and add one to the generation
loop over and over and output the result
"""


g = 1  # generation
n = 2  # the number of rabbits or the number of water bottle rabbits need
while n < 100:
    g = g + 1
    n = 2 * n  # When the number of rabbits is less than 100, the number of generations is increased by one and the
    # number of rabbits is doubled
else:
    print('When the age is %d, one hundred water bottles can be used up' % g)
# Output results, %d means a decimal integer output and use % () at the end to indicate the amount that should be
# output at %d
