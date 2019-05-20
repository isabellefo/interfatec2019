n = int(input())
dv = 0
sv = 0
e = n
c = {}
n1 = 0
n2 = 1
for i in range(n):
    c[n1] = input().split()
    c[n2] = input().split()
    n1 += 2
    n2 += 2
for i in range(n-1):
    for k in range(4):
        if int(c[i][k]) > int(c[i+1][k]):
            dv += 1
            e -= 1
        elif int(c[i][k]) < int(c[i+1][k]):
            sv += 1
            e -= 1
            

print ('danette venceu: {}'.format(dv))
print ('silvio venceu: {}'.format(sv))
print ('empate: {}'.format(e))
