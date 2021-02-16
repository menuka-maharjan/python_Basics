lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: ")) 
for num in range(lower,upper + 1):
    t=num
    s=0
    while t>0:
        digits=t%10
        s+=digits**3
        t//=10
    if num==s:
        print(num)
