N = int(input())
num = []
for i in range(1,N+1,1):
    num = num +[i]
s = str(input())
ls = len(s)
i=j=0
while(len(num)!=1):
    if(s[j]=='a'):
        i = (i+1)%N
        j = (j+1)%ls
    if(s[j]=='b'):
        num.remove(num[i])
        N=N-1
        i = i%N
        j = (j+1)%ls
print(num[0])
