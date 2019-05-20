s = input()
lists = set(s)
count = {}
for l in lists:
    count[l] = 0
    
for l in s:
    for k in count:
        if  k == l: 
            count[l] += 1
c = 0

if len(s)% 2 == 0:
    for i in count:
        if count[i]% 2 != 0:
            print('FALSO')
            break
        else:
            c += 1
    if c == len(count):
        print('VERDADEIRO')
else:
    for i in count:
        if count[i]%2 == 0:
            c += 1
    if c == len(count)- 1:
        print('VERDADEIRO')
    else:
        print('FALSO')
        
            
            
