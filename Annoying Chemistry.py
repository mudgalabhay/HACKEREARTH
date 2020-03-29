def gcd(x,y):
    while(y):
        x,y= y,x%y
    return x
x,y,p,q= map(int,input().split())
b1 = p*y
b2 = x*q
b3 = x*y
g = gcd(b1,b2)
fg = gcd(g,b3)
b1 = b1//fg
b2 = b2//fg
b3 = b3//fg
print(b1,b2,b3)
