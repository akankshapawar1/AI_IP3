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
from TicTacToeClass import random_player, minmax_decision, alpha_beta_search, alpha_beta_cutoff_search, monte_carlo_tree_search, \
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


'''def main():
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

        # start
        scores = {'Player1': 0, 'Player2': 0}
        for round in range(1, 4):  # This loop will go through rounds 1 to 3
            print(f"\nRound {round}:")

            # initializing the game with two players
            # print("TicTacToe will be called now")
            winner = TTT.play_game(player1, player2)

            # Update the scores based on who won this round

            if winner == 1:
                scores['Player1'] += 1  # Player1 is 'X' and has won
            elif winner == -1:
                scores['Player2'] += 1  # Player2 is 'O' and has won

            # Check if a player has won two rounds, then break the loop
            if scores['Player1'] == 2 or scores['Player2'] == 2:
                break

        # Print the final scores and winner
        print(f"\nFinal Scores: Player1 - {scores['Player1']}, Player2 - {scores['Player2']}")
        if scores['Player1'] > scores['Player2']:
            print("Player1 wins the game!")
        elif scores['Player1'] < scores['Player2']:
            print("Player2 wins the game!")
        else:
            print("The game is a draw!")
        # end

        user_continue_choice = input('Would you like to play the game again? ')
        if user_continue_choice.lower() == 'no':
            print('Thank You for Playing Our Game!')
            break'''

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

        # start
        scores = {'Player1': 0, 'Player2': 0}
        last_round_was_draw = False  # Keep track of whether the last round was a draw
        for round in range(1, 4):  # This loop will go through rounds 1 to 3
            print(f"\nRound {round}:")

            # initializing the game with two players
            winner = TTT.play_game(player1, player2)

            # Update the scores based on who won this round
            if winner == 1:
                scores['Player1'] += 1  # Player1 is 'X' and has won
                last_round_was_draw = False  # Reset draw tracker on a win
            elif winner == -1:
                scores['Player2'] += 1  # Player2 is 'O' and has won
                last_round_was_draw = False  # Reset draw tracker on a win
            else:
                if last_round_was_draw:  # Check if the last round was also a draw
                    print("Two consecutive draws. Game will stop now.")
                    break  # End the game if two consecutive draws occurred
                last_round_was_draw = True  # Set draw tracker for this round

            # Check if a player has won two rounds, then break the loop
            if scores['Player1'] == 2 or scores['Player2'] == 2:
                break

        # Print the final scores and winner
        print(f"\nFinal Scores: Player1 - {scores['Player1']}, Player2 - {scores['Player2']}")
        if scores['Player1'] > scores['Player2']:
            print("Player1 wins the game!")
        elif scores['Player1'] < scores['Player2']:
            print("Player2 wins the game!")
        else:
            print("The game is a draw!")
        # end

        user_continue_choice = input('Would you like to play the game again? (yes/no): ')
        if user_continue_choice.lower() == 'no':
            print('Thank You for Playing Our Game!')
            break


if __name__ == "__main__":
    main()
