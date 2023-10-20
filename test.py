score_num=0
reps=0
num=1
print('welcome to the calculator. type done if you want to end the calculation')
while num>0:
    A=(input("what score?"))
    if A == 'done':
        break
    else:
        score_num+=int(A)
        reps+=1
        num+=1
        
score= score_num/reps
print('you got '+str(score)+' points in average.')

