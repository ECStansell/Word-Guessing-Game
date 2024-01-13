#Emily Stansell
#November 30, 2023
#DEV 108
#Word Guessing Game Assignment


#import the wordlist to the main file
import wordlists

#functions to call a random word from each category
def get_bird():
  bird = wordlists.get_random_bird()
  return bird.upper()

def get_fish():
  fish = wordlists.get_random_fish()
  return fish.upper()
 
def get_animal():
  animal = wordlists.get_random_animal()
  return animal.upper()

#add spaces to the words in each category
def add_spaces_bird(bird):
  bird_with_spaces = " ".join(bird)
  return bird_with_spaces

def add_spaces_fish(fish):
  fish_with_spaces = " ".join(fish)
  return fish_with_spaces

def add_spaces_animal(animal):
  animal_with_spaces = " ".join(animal)
  return animal_with_spaces

#the user will choose if they want to play the game, display the menu, or exit the program
def game_choice():
  choice1 = input("\nWhich category would you like?\n------------------------------\n1. Birds\n2. Fish\n3. Animals\n\nOther Options: \n--------------\nM. Display This Menu\nE. Exit\n\nEnter Choice: \n-------------\n")
  #exits program
  if choice1.lower() == "e":
    print("Thank you for playing!")
    exit()
  #displays menu
  elif choice1.lower() == "m":
    game_choice()
  #plays the Birds category
  elif choice1 =="1":
    print("Your Choice: Birds")
    print()
    play_bird_game()
  #plays the Fish category
  elif choice1 =="2":
    print("Your Choice: Fish")
    play_fish_game()
  #plays the Animals category
  elif choice1 =="3":
    print("Your Choice: Animals")
    play_animal_game()
  else: 
    print()
    print("Invalid Entry. Try again.")
    game_choice()

#get letter guess from the user
def get_letter(guessed_letters):
  while True:
    guess = input("Enter a letter: ").strip().upper()
    #guess cannot be blank or longer than one letter
    if guess == "" or len(guess) > 1:
      print()
      print("Please enter a single letter. Try Again.")
      print()
      continue
    #guess must be a letter
    elif not guess.isalpha():
      print()
      print("Please enter a letter. Try Again.")
      print()
      continue
    #guess must be unique
    elif guess in guessed_letters:
      print()
      print ("You already guessed that letter. Try again.")
      print()
      continue
    else:
      return guess

#function that draws the screen for the bird category
def draw_screen_bird(num_wrong, num_guesses, guessed_letters, displayed_word):
  print("Word:", add_spaces_bird(displayed_word), " |"
       " Category:", "Birds |",
       "Guess:", num_guesses, "|"
       " Wrong:", num_wrong, "|"
       " Tried:", add_spaces_bird(guessed_letters), " |")

#function that draws the screen for the fish category
def draw_screen_fish(num_wrong, num_guesses, guessed_letters, displayed_word):
  print("Word:", add_spaces_fish(displayed_word), " |"
       " Category:", "Fish |",
       "Guess:", num_guesses, "|"
       " Wrong:", num_wrong, "|"
       " Tried:", add_spaces_fish(guessed_letters), " |")

#function that draws the screen for the animal category
def draw_screen_animal(num_wrong, num_guesses, guessed_letters, displayed_word):

  print("Word: ", add_spaces_animal(displayed_word), " |"
       " Category:", "Animals |",
       "Guess:", num_guesses, "|"
       " Wrong: ", num_wrong, "|"
       " Tried: ", add_spaces_animal(guessed_letters), " |")

#function that allows the user to play the animal category
def play_animal_game():
  animal = get_animal()

  #display the length of the word to help the user guess it
  word_length = len(animal)
  remaining_letters = word_length
  displayed_word = "#" * word_length

  #set the counters for the game
  num_wrong = 0
  num_guesses = 0
  guessed_letters = ""

  draw_screen_animal(num_wrong, num_guesses, guessed_letters, displayed_word)

  #start a while loop for the game. The user must have less than 10 losses and more than 0 remaining letters
  while num_wrong < 10 and remaining_letters > 0:
    print()
    guess = get_letter(guessed_letters)
    guessed_letters += guess

    #check if the letter is in the word
    pos = animal.find(guess, 0)
    if pos != -1:
      displayed_word = ""
      remaining_letters = word_length
      for char in animal:
        if char in guessed_letters:
          displayed_word += char
          remaining_letters -= 1
        else:
          displayed_word += "#"
    #if the user guesses an incorrect letter, their number of wrong guesses increases
    else:
      num_wrong += 1

    #number of guesses increases whether or not the user is correct
    num_guesses +=1

    draw_screen_animal(num_wrong, num_guesses, guessed_letters, displayed_word)

  print("_" * 60)
  #if the user correctly guesses all letters
  if remaining_letters == 0:
    print("Yay! You got it in " + str(num_guesses) + " guesses!")
    print()
    #user may play again, return to menu, or exit
    choice2 = input("Would you like to play the Animals guessing game again?\n\nYes (Y)\nMenu (M)\nExit (E)\n\n").strip().lower()
    if choice2.lower() == "y":
      play_animal_game()
    elif choice2.lower() == "m":
      game_choice()
    elif choice2.lower() == "e":
      print()
      print("Thanks for playing!")
      exit()
    else:
      print("Invalid Entry. Returning to menu")
  #if the user exceeds 10 wrong guesses
  else:
    print("Sorry, you lost.")
    print("The word was: ", animal)
    print()
    #the user may play again, go to the menu, or exit
    choice3 = input("Would you like to play the Animals guessing game again?\n\nYes (Y)\nMenu (M)\nExit (E)\n\n").strip().lower()
    if choice3.lower() == "y":
      play_animal_game()
    elif choice3.lower() == "m":
      game_choice()
    elif choice3.lower() == "e":
      print()
      print("Thanks for playing!")
      exit()
    else:
      print("Invalid Entry. Returning to menu")

#function that allows the user to play the fish category
def play_fish_game():
  fish = get_fish()

  #display the length of the word to help the user guess it
  word_length = len(fish)
  remaining_letters = word_length
  displayed_word = "#" * word_length

  #set the counters for the game
  num_wrong = 0
  num_guesses = 0
  guessed_letters = ""

  draw_screen_fish(num_wrong, num_guesses, guessed_letters, displayed_word)

  #start a while loop for the game. The user must have less than 10 losses and more than 0 remaining letters
  while num_wrong < 10 and remaining_letters > 0:
    print()
    guess = get_letter(guessed_letters)
    guessed_letters += guess

    #check if the letter is in the word
    pos = fish.find(guess, 0)
    if pos != -1:
      displayed_word = ""
      remaining_letters = word_length
      for char in fish:
        if char in guessed_letters:
          displayed_word += char
          remaining_letters -= 1
        else:
          displayed_word += "#"
    #if the user guesses an incorrect letter, their number of wrong guesses increases
    else:
      num_wrong += 1

    #number of guesses increases whether or not the user is correct
    num_guesses +=1

    draw_screen_fish(num_wrong, num_guesses, guessed_letters, displayed_word)

  print("_" * 60)
  #if the user correctly guesses all letters
  if remaining_letters == 0:
    print("Yay! You got it in " + str(num_guesses) + " guesses!")
    print()
    #Allows the user to play again, return to the menu, or exit
    choice4 = input("Would you like to play the Fish guessing game again?\n\nYes (Y)\nMenu (M)\nExit (E)\n\n").strip().lower()
    if choice4.lower() == "y":
      play_fish_game()
    elif choice4.lower() == "m":
      game_choice()
    elif choice4.lower() == "e":
      print()
      print("Thanks for playing!")
      exit()
    else:
      print("Invalid Entry. Returning to menu.")
  #if the user exceeds 10 wrong guesses
  else:
    print("Sorry, you lost.")
    print("The word was: ", fish)
    print()
    #Allows the user to play again, return to the menu, or exit
    choice5 = input("Would you like to play the Fish guessing game again?\n\nYes (Y)\nMenu (M)\nExit (E)\n\n").strip().lower()
    if choice5.lower() == "y":
      play_fish_game()
    elif choice5.lower() == "m":
      game_choice()
    elif choice5.lower() == "e":
      print()
      print("Thanks for playing!")
      exit()
    else:
      print("Invalid Entry. Returning to menu.")
    

#function that allows the user to play the bird category
def play_bird_game():
  bird = get_bird()

  #display the length of the word to help the user guess it
  word_length = len(bird)
  remaining_letters = word_length
  displayed_word = "#" * word_length

  #set the counters for the game
  num_wrong = 0
  num_guesses = 0
  guessed_letters = ""

  draw_screen_bird(num_wrong, num_guesses, guessed_letters, displayed_word)

  #start a while loop for the game. The user must have less than 10 losses and more than 0 remaining letters
  while num_wrong < 10 and remaining_letters > 0:
    print()
    guess = get_letter(guessed_letters)
    guessed_letters += guess

    #check if the letter is in the word
    pos = bird.find(guess, 0)
    if pos != -1:
      displayed_word = ""
      remaining_letters = word_length
      for char in bird:
        if char in guessed_letters:
          displayed_word += char
          remaining_letters -= 1
        else:
          displayed_word += "#"
    #if the user guesses an incorrect letter, their number of wrong guesses increases
    else:
      num_wrong += 1

    #number of guesses increases whether or not the user is correct
    num_guesses +=1

    draw_screen_bird(num_wrong, num_guesses, guessed_letters, displayed_word)

  print("_" * 60)
  #if the user correctly guesses all letters
  if remaining_letters == 0:
    print("Yay! You got it in " + str(num_guesses) + " guesses!")
    print()
    #Allows the user to play again, return to the menu, or exit
    choice6 = input("Would you like to play the Birds guessing game again?\n\nYes (Y)\nMenu (M)\nExit (E)\n\n").strip().lower()
    if choice6.lower() == "y":
      play_bird_game()
    elif choice6.lower() == "m":
      game_choice()
    elif choice6.lower() == "e":
      print()
      print("Thanks for playing!")
      exit()
    else:
      print("Invalid Entry. Returning to menu.")
  #if the user exceeds 10 wrong guesses
  else:
    print("Sorry, you lost.")
    print("The word was: ", bird)
    print()
    #Allows the user to play again, return to the menu, or exit
    choice7 = input("Would you like to play the Birds guessing game again?\n\nYes (Y)\nMenu (M)\nExit (E)\n\n").strip().lower()
    if choice7.lower() == "y":
      play_bird_game()
    elif choice7.lower() == "m":
      game_choice()
    elif choice7.lower() == "e":
      print()
      print("Thanks for playing!")
      exit()
    else:
      print("Invalid Entry. Returning to menu.")
      
      

    
#main function
def main():
  #displays title
  print("Welcome to Emily's Animal-Themed Word Guessing Game!")
  print("=" * 52)
  #calls game console
  game_choice()
  #plays game
  while True:
    game_choice()
    

if __name__ == "__main__":
  main()