f = open("poem.txt")
data = f.read()
if("Twinkle"in data):
    print("the word Twinkle is present in the poem")
else:
    print("the word Twinkle is not present in the poem")
f.close()