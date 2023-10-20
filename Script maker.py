script=""
subject=input("input subject")
grade=6
selector=1
num=1
for i in range(14):  
    winner=input("type winner")
    merit={1,3,5,7,9,11,13}
    excellence={2,4,6,8,10,12,14}
    if selector in merit:
        types="merit"
    else:
        types="Excellence"
        
    
    tag="The "+str(grade)+" "+subject+" "+types+" award goes to "+winner+".\n" 
    script+=tag
    if selector in excellence:
        grade+=1
    selector+=1
print(script)
