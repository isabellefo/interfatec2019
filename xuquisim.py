a, l = input().split()
a, l = int(a), int(l)
arv = {}
for lines in range(l):
    n, d = input().split()
    n = int(n)
    arv[n] = d

e = int(input())
inicio = 1
for i in range(e):
    boo = input()
    boo  = (boo == 'true')
    if boo:
        inicio = inicio*2 + 1
    else:
        inicio *= 2
print(arv[inicio])
