import os

from termcolor import cprint

from AI import Ai
from Board import Board
from Player import Player


class Mod:

    def __init__(self, board: Board, player: Player, ai: Ai, banner="tttBanner.txt"):
        """
        Instance of a moderator. Moderator keeps track of whose turn it is a
        to make a move. It also keeps track of who wins the game
        :param board:
        :param player:
        :param ai:
        :param banner:
        """

        # setting instance variables
        self.board = board
        self.player = player
        self.ai = ai
        self.banner = banner

        # which player has the current turn
        self.whoseTurn = self.player

    def checkDraw(self):
        """
        Check if the game ends in a draw
        :return: bool
        """
        if self.board.positions.count(" ") == 0:
            print("DRAW!")
            return True

    def determineWinner(self):
        """
        Determining if the current board has a winner
        :return: bool
        """

        # Saving the board's rows, columns and diagonals in variables
        rows = self.board.getRows()
        columns = self.board.getColumns()
        diagonals = self.board.getDiagonals()

        # saving the board's rows, columns and diagonals in one list
        lines = [row for row in rows]
        for column in columns:
            lines.append(column)
        for diagonal in diagonals:
            lines.append(diagonal)

        # checking if either the AI or the human has three in a row, column or diagonal
        for symbol in [self.getPlayerSymbol(), self.getAiSymbol()]:
            for line in lines:
                if line.count(symbol) == 3:
                    # human player wins
                    if symbol == self.getPlayerSymbol():
                        winner = self.player

                    # AI wins
                    else:
                        winner = self.ai
                    print(f"THE WINNER IS {winner.getName()}")
                    return True
        return False

    def requestMove(self):
        """
        This method asks the player for a move when it's the players turn.
        When its the AI's turn this method makes the AI perform a move
        :return: None
        """

        # player's turn to make a move
        if self.whoseTurn == self.player:
            position = int(input(f"{self.player.getName()}'s turn : "))
            self.player.insertSymbol(position)
            self.whoseTurn = self.ai

        # AI's turn to make a move
        else:
            print(f"{self.ai.getName()}'s turn")
            self.ai.makeBestMove()
            self.whoseTurn = self.player

    def getPlayerSymbol(self):
        """
        Return the symbol that corresponds with the human player
        :return: str
        """
        return self.player.getSymbol()

    def getAiSymbol(self):
        """
        Return the symbol that corresponds with the AI
        :return: str
        """
        return self.ai.getSymbol()

    def welcomeMessage(self):
        """
        Print a nice welcome message and the initial empty board
        :return: None
        """

        # creating absolute path to the the banner that was passed in the constructor
        runtime_file_path = os.path.abspath(__file__)
        runtime_file_folder = os.path.dirname(runtime_file_path)
        banner_file_path = os.path.join(runtime_file_folder, self.banner)

        cprint("WELCOME TO:", 'red', attrs=['bold'])
        banner = open(banner_file_path, "r")
        for line in banner:
            cprint(line.strip("\n"), 'yellow', attrs=['bold'])
        cprint(72 * "~", 'magenta', attrs=['bold'])
        print()
        self.board.printBoard()
