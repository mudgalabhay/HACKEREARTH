from collections import Counter
n = int(input())
l = []
for i in range(n):
    l.append(input())
    
for i in range(0,len(l)):
    l[i]=''.join(sorted(l[i]))
    
freqDict = Counter(l)
 
print(max(freqDict.values()))
