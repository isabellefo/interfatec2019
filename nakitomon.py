n = int(input())
dv = 0
sv = 0
e = n
c = {}
for i in range(2*n):
    c[n1] = input().split()
for i in range(n-1):
    for k in range(4):
        if int(c[i][k]) > int(c[i+n][k]):
            dv += 1
            e -= 1
        elif int(c[i][k]) < int(c[i+n][k]):
            sv += 1
            e -= 1
            

print ('danette venceu: {}'.format(dv))
print ('silvio venceu: {}'.format(sv))
print ('empate: {}'.format(e))
