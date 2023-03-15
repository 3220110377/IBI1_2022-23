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
#d<e

X,Y=True, False #Set X,Y as Boolean
W=X and Y #Set W
Z= X or Y #Set Z
print(W,Z) #Output the values of W and Z
# W is False ,Z is True
