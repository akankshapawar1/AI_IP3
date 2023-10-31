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

playersName = ['1. Random Player', '2. MiniMax Player', '3. Alpha Beta Player', '4. Heuristic Alpha Beta Player',
               '5. MCTS Player', '6. Query Player']
players = [1, 2, 3, 4, 5, 6]


def main():
    def getPlayer(prompt):
        while True:
            player = int(input(prompt))
            if player in players:
                return player
            else:
                prompt = "Could not find your player, please try again: "

    print("Player Selection: ")
    for p in playersName:
        print(p)
    while True:
        player1 = getPlayer('Please enter your first player:')
        player2 = getPlayer('Please enter your second player:')
        print("TTTC will be called now")
        user_continue_choice = input('Would you like to play the game again? ')
        if user_continue_choice.lower() == 'no':
            print('Thank You for Playing Our Game!')
            break


if __name__ == "__main__":
    main()
