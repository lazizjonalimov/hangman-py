from words import words
from visual import visual_hangman_dic
import random, only_hints

is_correct = True
# randomly selected word
random_word = random.choice(words)
choices_list = []
characters = list(random_word)
word_length = len(characters)
first = only_hints.hint(word_length, choices_list, characters)
print(random_word)
false = 0
place = 0
print("Welcome to Hangman Game")
print()
while is_correct:
  print("Here is the secret word (1-4 hints):")
  print((" ").join(first))
  print()
  for i in range(len(characters)):
    place += 1
    if characters[i] == "_":
      pass
  user_choice = input("Give your letter choice: ")
  while not user_choice.isalpha():
     user_choice = input("Give your letter choice: ")

  user_num = input("Give Letter's Index: ")
  while (not user_num.isdigit()) or int(user_num) > len(random_word) or (first[int(user_num)-1] != "_"):
    print()
    print("Your Input should be an integer that is not greater than the length of the word, and it should be in the first index")
    print()
    user_num = input("Give Letter's Index: ")
  
  for i in characters: 
    if characters[int(user_num) - 1] == user_choice:
      first[int(user_num) - 1] = user_choice
      print("Congrats, you have guessed a right letter!")
      print("Keep it up!")
      break
    else: 
      print("Sorry, but you failed to guess a right letter")
      false += 1
      print(f"You have got {7-false} chances")
      print(visual_hangman_dic[false])
      break
  if false == 7:
    print("Sorry, YOU have FAILED - HANGED")
    print("Game is over!")
    is_correct = False

  if "_" not in first:
    print("You Great - WELL DONE")
    print(f"The word is - {random_word}")
    print("Game is over!")
    is_correct = False