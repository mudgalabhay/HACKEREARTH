def solver(s):
    count=0
    for i in range(len(s)):
        if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
            count+=1
    return count
t = int(input())
for i in range(t):
    s = input()
    s = s.lower()
    re = solver(s)
    print(re)
