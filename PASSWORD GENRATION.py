#  PROJECT PASSWORD GENERATOR
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

print(password)



#HARD PASSWORD
# password_list = []
#
# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))
#
# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#   password += char
#
# print(f"Your password is: {password}")
#
#
# #challenge
# import random
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /| \  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
#
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# work_length = len(chosen_word)
# lives = 6
# print(f'Pssst, the solution is {chosen_word}.')
#
# display = []
# for _ in range(work_length):
#     display += "_"
#
# end_of_game = False
# while not end_of_game:
#   guess = input("Guess a letter: ").lower()
#
#   for position in range(work_length):
#       letters = chosen_word[position]
#       #print(f"current position: {position} \n Current letter: {letters} \n guessed letter : {guess}")
#       if letters == guess:
#           display[position] = letters
#   if guess not in chosen_word:
#      lives -= 1
#      if lives == 0:
#        end_of_game = True
#        print("You lose")
#   print(f"{' '.join(display)} ")
#   if "_" not in display:
#      end_of_game = True
#      print("YOU WIN.")
#
#   print(stages[lives])