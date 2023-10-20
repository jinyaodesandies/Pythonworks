import random
door= [1,2,3]
true= []
x=0
false=[]

num= random.randint(1,3)

for i in range(3):
    if door[x] == num:
        true+=door[x]
    else:
        false += door[x]
    x+=1
 print(true)
 print(false)
