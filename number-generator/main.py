import random
print(random.randrange(1,10))

#for i in range(10,20):
   # print(i)

top_of_range=input("type a number ")

if top_of_range.isdigit():#confirm they typed in a number before you convert it to a number
    top_of_range = int(top_of_range)

    if top_of_range < 0 :
        print("please type a number greater than zero")
        quit()
else:
    print("please type a number ")
    quit()

random_num = random.randint(0,top_of_range) 

guess=0 

while True:

    guess+=1

    user_guess= input("make a guess ")
    if user_guess.isdigit():#confirm they typed in a number before you convert it to a number
        user_guess = int(user_guess)    
    else:
        print("please type a number ")
        continue  #goes back to the top of the loop

    if user_guess == random_num:
        print("correct")
        break #to prevent it asking even after we got it right
    elif user_guess > random_num:
        print("a little lower")
    else:
        print("a little higher")

print(f"you got it in {guess} guesses")        
 
