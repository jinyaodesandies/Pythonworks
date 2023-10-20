
import random
nume = 0
array = []
training= 15

for i in range(training):
    array.append(random.randint(1,400))
    nume += 1


lgth = len(array)
sorts = len(array)-1
miracle= 0

x=0

std= 0
print("original array is "+str(array))
while miracle == 0:
    std= x-1
    
    

    r= random.randint(std,sorts)

    
    r1 = random.randint(std,sorts)
    temp = array[r]
    sort = 1
    x=0
    x1=1
    array[r] = array[r1]

    array[r1]= temp
    
    while sort == 1:
       
        if array[x] < array[x1]:
            x += 1
            x1 += 1
            

                
            
        else:

            sort = 0
        
        if x == sorts:
            miracle = 1
            sort = 0
            

        
print(array)

