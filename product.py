def sumls (ls):
    n= len(ls)
    print(ls[1])
    total = 1
    for i in range(n):

        total= total * ls[i]
        print(total)
    return total

lis = [2,2,2,3]
print("the product of this list is "+str(sumls(lis)))


