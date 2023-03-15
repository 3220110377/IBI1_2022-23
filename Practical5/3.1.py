a=-3.19
b=-118.24
c=116.39 #enter the values of a,b, and c
d=min(abs(a-b),360-abs(a-b))
e=min(abs(a-c),360-abs(a-c)) #enter the values of d and e, get the smaller of the two accuracy differences
if d>e:
 print('d>e')
elif d==e:
 print('d=e')
else:
 print('d<e') #compare d and e and output the results


