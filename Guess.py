import random
random_number=str(random.randint(1,5))
print(random_number)
correct_answer=0


while correct_answer==0:
    guess=input("Pick a number between one and five.")
    if guess==random_number:
        print("good job!")
        print("your guess was "+guess+", and the random number was "+random_number)
        correct_answer+=1
    else:
        print("sorry, wrong guess. try again.")
        
