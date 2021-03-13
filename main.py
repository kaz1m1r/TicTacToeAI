from Board import Board
from Player import Player
from AI import Ai
from Moderator import Mod


if __name__ == "__main__":
    # instantiating board
    board = Board()

    # instantiating player
    playerName = "Casper"
    playerSymbol = "X"
    player = Player(playerName, playerSymbol, board)

    # instantiating AI
    aiName = "Mike Hunt"
    aiSymbol = "O"
    ai = Ai(aiName, aiSymbol, board, player)

    # instantiating moderator
    banner = "new_tttBanner.txt"
    mod = Mod(board, player, ai, banner)
    mod.welcomeMessage()

    while not mod.determineWinner():
        mod.requestMove()
        if mod.checkDraw():
            break

