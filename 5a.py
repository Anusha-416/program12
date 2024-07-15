a1=int(input("Enter first number:")) 
a2=int(input("Enter Second number:")) 
#recursive function 
def gcd_r(m1,m2): 
    if m2 == 0: 
        return m1 
    return gcd_r(m2, m1 % m2) 
#non recursive function 
def gcd_nonr(n1,n2): 
    while(n1!=n2): 
        if n1>n2: 
            n1-=n2 
        else: 
            n2-=n1 
    return n1 
if a1>=0 and a2>=0: 
    recursive=gcd_r(a1,a2) 
    nonrecursive=gcd_nonr(a1,a2) 
    print(f"\nGCD of {a1} and {a2} using recursive function is {recursive}") 
    print(f"GCD of {a1} and {a2} using non-recursive function is {nonrecursive} ") 
else: 
    print("Please enter a positive Integer")
