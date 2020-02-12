n,k = map(int,input().split())
temp = 2*k
res = 10**100
for i in range(1,temp+1):
    res = min(res,abs(k-i)+min(n%i,i-n%i))
print(res)
