n = int(input())
ab = []
for j in range(n):
    aeb = input().split()
    aeb[0] = int(aeb[0])
    aeb[1] = int(aeb[1])
    ab.append(aeb)

for j in range(n):
    l = []
    print('INTERVALO {}'.format(j+1))
    for x in range(ab[j][0], ab[j][1]+1):
        c = 0
        for i in range(1, x//2 +1):
            if x%i == 0:
                c += 1
        if c  == 1:
            l.append(str(x))
    
    junto = ''.join(l)

    for x in range(10):
        print('{}: {}'. format(x, junto.count(str(x)) ))
