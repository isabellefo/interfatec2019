n = input().split()

for k in range(3):
    n[k] = int(n[k])
    
m = 30001
for num in n:
    if num < m:
        m = num

print(m)
