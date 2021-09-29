print("Welcome to my computer quiz!")
n = input("Do you want to play? ").lower()
score = 0
if n == "yes":
    print("Okay! Lets play :)")
    answer = input("What does CPU stands for? ").lower()
    if answer == "central processing unit":
        print("Correct!")
        score +=1
    else:
        print("Incorrect")
        print("correct answer - central processing unit")
    
    answer = input("What does RAM stands for? ").lower()
    if answer == "random access memory":
        print("Correct!")
        score +=1
    else:
        print("Incorrect")
        print("correct answer - random access memory")

    answer = input("What does GPU stands for? ").lower()
    if answer == "graphics processing unit":
        print("Correct!")
        score +=1
    else:
        print("Incorrect")
        print("correct answer - graphics processing unit")

    answer = input("What does PSU stands for? ").lower()
    if answer == "power supply unit":
        print("Correct!")
        score +=1
    else:
        print("Incorrect")
        print("correct answer - power supply unit")
        
else:
    quit()
print("You got ",score ,"questions correct!")
print("You got ",((score/4) *100) ,"%.")