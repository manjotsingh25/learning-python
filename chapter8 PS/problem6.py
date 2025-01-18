def inches_to_cms(inche):
    return inche * 2.54
n = float(input("Enter your value: "))
print(f"The value of corresponding in cms is: {inches_to_cms(n)}")