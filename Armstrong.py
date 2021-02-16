n=int(input())
s=0
t=n
while t>0:
    digits=t%10
    s+=digits**3
    t//=10
if n==s:
    print("Armstrong")
else:
    print("not")