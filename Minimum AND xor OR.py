import sys
def minXor(l):
    n = len(l)
    l.sort()
    minxor = int(sys.float_info.max)
    val = 0
    for i in range(0,n-1):
        val = l[i]^l[i+1]
        minxor = min(minxor,val)
    return minxor
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))[:n]
    print(minXor(l))
