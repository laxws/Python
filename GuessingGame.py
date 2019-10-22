import random


print("Hello, What is your name ?")
name = input("Name : ")

number = random.randint(1, 20)
number_of_guess = 0
print(f'{name} , Number that I was thinking of is between 1 and 20')

while number_of_guess < 10:
    print("Take a guess")
 
    guess = int(input("Guess: "))
    number_of_guess += 1

    if guess > number:
        print(f'{name} , number is lower than the answer')

    if guess < number:
        print(f'{name} , number is higher than the answer')

    if guess == number:
        print(f'Well done {name} !, you have guess correctly in {number_of_guess} tries !')
        break

if guess != number:
    print(f'I am sorry {name} , the correct answer is {number}')

input("\n\nPress the enter key to exit")







