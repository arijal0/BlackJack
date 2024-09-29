Here is the README file for your Blackjack project repository:

---

# Blackjack Game in Python

This project is a simple Blackjack game implemented in Python. The game allows a user to play against the dealer (computer). The player can choose to 'hit' or 'stand' during their turn, while the dealer follows fixed rules for drawing cards. The game checks for "Blackjack" and "Bust" conditions and determines the winner based on the hand totals.

## Project Structure

The project consists of two Python files:

1. `blackjack_helper.py`: Contains helper functions for drawing cards, printing headers, determining hand values, and handling game results.
2. `main.py`: Runs the game logic, where the user plays a hand against the dealer.

## How to Play

1. The game starts by dealing two cards to both the player and the dealer.
2. The player will be prompted to "Hit" (draw another card) or "Stand" (keep their current hand). The goal is to get as close to 21 without exceeding it.
3. After the player's turn, the dealer will automatically draw cards until their hand total is 17 or more.
4. The game checks for winning conditions, including "Blackjack" (21 points exactly) and "Bust" (exceeding 21 points).
5. The game prints the results, declaring the winner or whether the game is a "Push" (a tie).

## Running the Game

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Run the game by executing the `main.py` file:

```bash
python main.py
```

## File Descriptions

### `blackjack_helper.py`
This file includes the following functions:
- **`print_card_name(card_rank)`**: Prints the name of the drawn card.
- **`draw_card()`**: Draws a card with a value between 1-13 and returns its Blackjack value.
- **`print_header(message)`**: Prints a message formatted as a header.
- **`draw_starting_hand(name)`**: Draws two cards for the player or dealer and returns the total hand value.
- **`print_end_turn_status(hand_value)`**: Prints the final hand status at the end of a player's turn (e.g., if the player has "Blackjack" or "Bust").
- **`print_end_game_status(user_hand, dealer_hand)`**: Prints the end game result, determining the winner based on the final hand values.

### `main.py`
This file implements the game logic:
- The player is prompted to choose whether to "Hit" or "Stand."
- The dealer automatically draws cards according to the game's rules.
- The results are printed at the end of the game, showing whether the player or the dealer wins.

## Example Output

```
-----------
YOUR TURN
-----------
Drew a 7
Drew a 5
You have 12. Hit (y/n)? y
Drew a Jack
You have 22. BUST.
-----------
DEALER TURN
-----------
Drew a King
Drew a 6
Dealer has 16.
Drew a 2
Dealer has 18.
Final hand: 18.
-----------
GAME RESULT
-----------
Dealer wins!
```


