import random


word_list = ["ardvark", "baboon", "camel"]

choose_word = random.choice(word_list)

print(choose_word)



display =[]

for _ in range(len(choose_word)): 

 display += "_"

print(display)


end_of_game = False

while not end_of_game :

 

  user_guess = input("Guess a letter : ").lower()


  for position in range(len(choose_word)):
     letter = choose_word[position]
    #  print(f"current position : {position}\n current letter : {letter}\n guessed letter : {user_guess}\n")
     if letter == user_guess:
        display[position] = letter

  lives = 6
  if user_guess not in  choose_word :
    lives -= 1
    if lives == 0:
     end_of_game = True
     print("You lose")

  print(display)

  if "_" not in display :
    end_of_game = True
    print("You won")

from hangmanstage import stages

print(stages[lives])

