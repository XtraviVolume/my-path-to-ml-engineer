from math import gcd
n,k = map(int(input().split()))
a=list(map(int(input().split())))
for i in range (n-k+1):
    s = sum(a[i:i+k])
    if s%k==0:
        print(s//k, end=" ")
    else:
        g =gcd(s,k)
        p= s//g
        q=k//g
        print(f"{p}/{q}", end=" ")