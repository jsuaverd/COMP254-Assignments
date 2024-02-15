def gcd(a,b):
    c = max(a,b)
    d = min(a,b)

    if c%d ==0:
       return d
    else:
        e = c%d
        return gcd(d,e)


a = int(input("Please enter a number: "))
b =  int(input("Please enter a second number: "))

r = gcd(a,b)

print(f"the GCD of {a} and {b} is  {r}")