score_num=0
rep=int(input("how many scores do you want to calculate?"))
reps=0
for i in range(rep):
    score_num+=int(input("what score?"))
    reps+=1

score= score_num/rep

print('you got '+str(score)+' points in average.')
