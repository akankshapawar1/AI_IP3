"""
Player Selection:
1. Random Player
2. MiniMax Player
3. Alpha Beta Player
4. Heuristic Alpha Beta Player
5. MCTS Player
6. Query Player
Please enter your first player: 0
Could not find your player, please try again: 1
Please enter your second player: 7
Could not find your player, please try again: 6
"""
from TicTacToeClass import random_player, minmax_decision, alpha_beta_search, alpha_beta_cutoff_search, \
    monte_carlo_tree_search, \
    query_player, Game, TicTacToe

playersName = ['1. Random Player', '2. MiniMax Player', '3. Alpha Beta Player', '4. Heuristic Alpha Beta Player',
               '5. MCTS Player', '6. Query Player']

validPlayerList = [1, 2, 3, 4, 5, 6]

player_functions = {
    1: random_player,
    2: minmax_decision,
    3: alpha_beta_search,
    4: alpha_beta_cutoff_search,
    5: monte_carlo_tree_search,
    6: query_player
}


def main():
    def getPlayer(prompt):
        while True:
            player = int(input(prompt))
            if player in validPlayerList:
                return player
            else:
                prompt = "Could not find your player, please try again: "

    print("Player Selection: ")
    for p in playersName:
        print(p)

    while True:
        player1_choice = getPlayer('Please enter your first player:')
        player2_choice = getPlayer('Please enter your second player:')

        TTT = TicTacToe()
        TTT.current_state = TTT.initial

        # create player instance
        player1 = player_functions[player1_choice]
        player2 = player_functions[player2_choice]

        scores = {'Player1': 0, 'Player2': 0}
        # Keep track of whether the last round was a draw
        last_round_was_draw = False
        for round in range(1, 4):  # This loop will go through rounds 1 to 3
            print(f"\nRound {round}:")

            # initializing the game with two players
            winner = TTT.play_game(player1, player2)

            # Update the scores based on who won this round
            if winner == 1:
                # Player1 is 'X' and has won
                scores['Player1'] += 1
                print(f'Player X won the game in Round {round}')
                # Reset draw tracker on a win
                last_round_was_draw = False
            elif winner == -1:
                # Player2 is 'O' and has won
                scores['Player2'] += 1
                print(f'Player O won the game in Round {round}')
                # Reset draw tracker on a win
                last_round_was_draw = False
            else:
                print(f'Player X and Player O drew the game in Round {round}')
                if last_round_was_draw:
                    print("No Player could win two out of three rounds in the game. The game was a draw.")
                    break
                last_round_was_draw = True

            # Check if a player has won two rounds, then break the loop
            if scores['Player1'] == 2 or scores['Player2'] == 2:
                break

        # Print the final scores and winner
        print(f"\nFinal Scores: Player1 - {scores['Player1']}, Player2 - {scores['Player2']}")
        if scores['Player1'] > scores['Player2']:
            print(f"Player X won two out of three rounds in the game."
                  f" Player X is the winner!")
        elif scores['Player1'] < scores['Player2']:
            print(f"Player O won two out of three rounds in the game."
                  f" Player O is the winner!")
        else:
            print(f"Player X and Player O drew the game in Round {round}")

        user_continue_choice = input('Would you like to play the game again? (yes/no): ')
        if user_continue_choice.lower() == 'no':
            print('Thank You for Playing Our Game!')
            break


if __name__ == "__main__":
    main()
