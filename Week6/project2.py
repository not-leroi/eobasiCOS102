admitted = []
not_admitted = []

name = input("What is your name?")
jamb_score = int(input("What was your JAMB score?"))
credits = int(input("How many credits did you have in the key subjects?"))
interview = input("Did you pass your interview?").strip().lower()
department = input("What is your desired course of study?\nComputer Science or Mass Communication?").strip().lower()

if department == "computer science":
    if jamb_score >= 250 and credits >= 5 and interview == 'yes':
        print("Congratulations! You are admitted into the department of Computer Science.")
        admitted.append(name)
    else:
        print("Sorry. You aren't admitted into Computer Science")
        not_admitted.append(name)
elif department == 'mass communication':
    if jamb_score >= 230 and credits >= 5 and interview == "yes":
        print("Congrats! You are admitted into Mass Communication")
        admitted.append(name)
    else:
        print("Sorry. You are not admitted into Mass Communication")
        not_admitted.append(name)
else:
    print('Invalid department inputted')

print("\nThe admitted students are: ",admitted)
print("\nThe students that weren't admitted are: ",not_admitted)