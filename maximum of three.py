def maximum (num1,num2,num3):
    
    top = num1
    if num2>=top:
        top= num2
        mx=2
    else:
        mx= 1
    
    if num3>=top:
        top = num3
        mx=3
    else:
        mx= 1
    print("the maximum number is number "+str(mx))
    return top

x = int(input("enter num 1: "))
y = int(input("enter num 2: "))
z = int(input("enter num 3: "))

print("valued at "+str(maximum(x,y,z)))

        
