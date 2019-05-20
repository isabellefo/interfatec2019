from math import factorial as fac
x = int(input())
r = x*(3.1415/180)
t = 0

for n in range(6):
    t += ( (-1)**n ) * ((r)**(2*n)/ (fac(2*n)))

if t < 1 and int(str(t)[5]) > 6:
    print('{:.3f}'.format(t))
else: 
    print('{:.3f}'.format(int(t*1000)/1000))
