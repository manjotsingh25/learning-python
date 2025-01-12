n = int(input("Enter a number: "))
for i in range(2,n):
    if(n%i)==0:
        print("this number is not a prime")
        break
else:
    print("this number is prime")