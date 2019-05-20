n = int(input())
he = []
hs = []
for i in range(n):
    k = input().split()
    he.append(int(k[0])*60 + int(k[1]))
    hs.append(int(k[2])*60 + int(k[3]))
    
print(max(hs) - min(he))
