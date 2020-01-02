t = int(input())
for i in range(t):
    n = int(input())
    if(n%21==0):
        print("The streak is broken!")
    else:
        s = str(n)
        if(s.find("21")==-1):
            print("The streak lives still in our heart!")
        else:
            print("The streak is broken!")
