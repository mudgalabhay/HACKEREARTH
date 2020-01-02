def substring(name):
    n = len(name)
    count = 0
    for i in range(n):
        for j in range(i+1,n+1):
            substr = name[i:j]
            rev = substr[::-1]
            if(substr == rev):
                count+=1
    print(count)
name  = input()
substring(name)