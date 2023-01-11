# guess number between 1 and 100
from random import randint
import is_even, is_prime, ranges
tot_attempst = 10
secret_number = randint(1,100)
counter = 0
print(secret_number)
print("Guess the secret number between 1 and 100")
print()
for i in range(tot_attempst):
  counter += 1
  print()
  user_guess = int(input("Guess Number: "))
  if 1 <= user_guess <= 100:
    if user_guess != secret_number:
      print("Wrong Guess")
    if user_guess == secret_number:
      print("Congrats! - You guessed the right number!")
      break
    if user_guess != secret_number and counter >=1:
      is_even.isEven(secret_number)
      is_prime.isPrime(secret_number)
      ranges.range(secret_number)
      if user_guess > secret_number:
        print("The guess is too high")
      elif user_guess < secret_number:
        print("The guess is too low")
    print(f"You have got {tot_attempst - counter} attempts left. ")
  else: 
    print("YOu are too far: between 1 and 100")
else: 
  print(f"Sorry, you lost the game - secret number is {secret_number}")