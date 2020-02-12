def solver(S,qo,n,m):
    parti = 1
    cs = 0
    for i in range(n):
        if(qo[i]>S):
            return False
        if(cs+qo[i]>S):
            cs = qo[i]
            parti+=1
        else:
            cs+=qo[i]
    return parti<=m
    
    
n,m = map(int,input().split())
q = list(map(int,input().split()))
maxm = 0
for i in range(n):
    if(maxm<q[i]):
        maxm = q[i]
 
S = maxm
maxsum = 0
for i in range(n):
    maxsum+=q[i]
    
l = 0
r = maxsum
while(l<=r):
    qo = q
    mid = (l+r)//2
    if(solver(mid,qo,n,m)==True):
        r = mid-1
    else:
        l = mid+1
    
print(l)
    
 
