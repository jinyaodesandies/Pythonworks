'''
Created on Sep 15, 2023

@author: ISASC_ST
'''



    
def revme(num):
    
    n=1
    tru = 2
    digit=0
    revd=0
    r=0

    while tru == 2:
        denom =10 ** digit
        if num % denom == num:
            
            
            tru+=1
        else:
            
            digit += 1
            n+=1

        
    remainder_denominator = 1
    operated_num=num
    new_num=0
    current_num=0
 
    increasing = 1

    power = digit - 1
    
    for i in range(digit):
        current_num = operated_num% 10**increasing
        new_num += current_num * 10**power
        operated_num-=current_num
        power-=2
        increasing+=1
        print("power is "+str(power))
        print("new number is"+str(new_num))
        
        
        
        

    
        
reverse = int(input("reverse me!"))
revme(reverse)
