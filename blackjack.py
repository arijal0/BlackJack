from blackjack_helper import *
user_hand_value = draw_starting_hand("YOUR")
while user_hand_value < 21:
  usersaid = input(f"You have {user_hand_value}. Hit (y/n)? ")
  if usersaid == 'n':
    break
  elif usersaid == 'y':
    user_hand_value_2nd = draw_card()
    user_hand_value = user_hand_value + user_hand_value_2nd
  else:
    print("Sorry I didn't get that.")
print_end_turn_status(user_hand_value)

dealer_hand_value = draw_starting_hand("DEALER")
while dealer_hand_value < 17:
  print("Dealer has {}.".format(dealer_hand_value))
  dealer_card_value_2nd = draw_card()
  dealer_hand_value = dealer_hand_value + dealer_card_value_2nd
print_end_turn_status(dealer_hand_value)


print_end_game_status(user_hand_value , dealer_hand_value)