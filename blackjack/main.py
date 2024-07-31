import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "    It's a draw."
  elif computer_score == 0:
    return "    Computer has a Blackjack, you lose!"
  elif user_score == 0:
    return "    You win with a Blackjack!"
  elif user_score > 21:
    return "    You bust."
  elif computer_score > 21:
    return "    Computer busts and you win!"
  elif user_score > computer_score:
    return "    You win!"
  else:
    return "    You lose."
    
def play_game():
  
  print(logo)
  
  user_cards = []
  computer_cards = []
  game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards [0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      user_should_deal = input("  Please type y to hit, or n to pass.\n")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"  Your final hand was {user_cards} for a total of {user_score}.")
  print(f"  The Computer's final hand was {computer_cards} for a total of {computer_score}.")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Would you like to play a game of Blackjack? Please type y or n.\n"):
  clear()
  play_game()