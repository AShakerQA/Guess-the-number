from art import logo
print(logo)
import random
# generated_num = random.randint(1, 100)
# print(generated_num)

# end_game = False
# complexity = input("Select your difficulty: Easy or Hard?\n").lower()
# if complexity == "easy":
#     lives = 10
# elif complexity == "hard":
#     lives = 5


# while not end_game:
#     player_guess = int(input("Guess A Number Between 1 and 100: "))
#     if player_guess > generated_num:
#         print("Too High.")
#         lives -= 1
#         if lives > 1:
#             print(f"You have {lives} lives remaining")
#         elif lives == 1: 
#             print(f"You have {lives} life remaining")
#     elif player_guess < generated_num:
#         print("Too Low.")
#         lives -= 1
#         if lives > 1:
#             print(f"You have {lives} lives remaining")
#         elif lives == 1: 
#             print(f"You have {lives} life remaining")
#     if lives > 0 and player_guess == generated_num:
#         print(f"You Win, the number was: {generated_num}")
#         end_game = True
#     if lives == 0:
#         print("You've run out of lives, You Lose!")
#         end_game = True




EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Cycle through guess
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Reduce turns by 1 if wrong
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()
