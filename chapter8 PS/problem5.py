p = int(input("Enter a Number: "))
def pattern(n):
    if (n==0):
        return
    print("*" * n)
    pattern(n-1)
pattern(p)