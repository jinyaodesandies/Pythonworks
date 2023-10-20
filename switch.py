def rev(x):
    length = len(x)
    new = ""
    for i in range (length):
        new+= x[length-1]
        length-=1
    return new
string = input("revme!: ")

print(rev(string))
    
