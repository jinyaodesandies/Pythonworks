import random
grades = []
bonus= []
sort = 0
itera=0
total = []
rank = []
student = ["kyle_deng", "Jinyao DeSandies","Deepak Tyagi","Olivia Zoppa","Kanji Hamamoto","Eunsung Jang"]
for i in range(len(student)):
    grades.append(random.randint(40,99))
    bonus.append(round(grades[i]*0.01,2))

    total.append(grades[i]+bonus[i])

while sort ==0:
    
    
    if itera == len(student)-1:
        print("working")
        break
    elif total[itera] < total[itera+1]:
        itera += 1
        
    else:
        temp = total[itera]
        total[itera] = total[itera+1]
        total[itera+1] = temp
        temp = student[itera]
        student[itera] = student[itera+1]
        student[itera+1] = temp
        itera = 0

for i in range(len(student)):
    print(str(student[i])+"'s total grade is"+ str(total[i]))

    
    

