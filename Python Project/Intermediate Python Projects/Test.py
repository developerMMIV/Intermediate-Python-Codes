name = input("What is your name?:")

print("Welcome to the wife material test, created by @developergustavoMMIV. This is a test to determine if you are worthy to be a wife material.")
print("{} in order to pass this test, you must get at least 70% (C) to be considered a wife material.".format(name))
input("Press any key to start")

# Initialize point variable
point = 0

question1 = int(input("Question 1: How old are you? "))
if 18 <= question1 <= 29:
    point += 1

question2 = input("Question 2: Are you a virgin? ").lower()
if question2 == "yes":
    point += 1

print("Total points: {}".format(point))
