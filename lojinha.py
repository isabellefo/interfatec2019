nv = int(input())
t = 0
for n in range(nv):
    q, v = input().split()
    t += int(q) * float(v)
print('{:.2f}'.format(t))
