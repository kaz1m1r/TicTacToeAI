import termcolor
from Board import Board


class Player:

    def __init__(self, name: str, symbol: str, board: Board):
        """
        Make an instance of a player object
        :param name: str (name of the player instance)
        :param symbol: str (symbol of the player instance)
        :param board: Board (instance of the board that the player is currently playing on)
        """

        # setting instance variables of the Player class
        self.name = name
        self.symbol = termcolor.colored(symbol, "red")
        self.board = board

    def insertSymbol(self, position):
        """
        Player's method to insert his/her symbol on the board
        :param position:
        :return: None
        """
        if self.board.positions[position] == " ":
            self.board.insertSymbol(self.symbol, position)
        else:
            try:
                position = int(input(f"{self.getName()}, that place is occupied. Pick another number (1 - 9) : "))
                self.insertSymbol(position)
            except ValueError:
                position = int(input(f"Insert an integer! (1 - 9) : "))
                self.insertSymbol(position)

    def getName(self):
        """
        Return the name of the player instance
        :return: str
        """
        return self.name

    def getSymbol(self):
        """
        Return the symbol of the player instance
        :return: str
        """
        return self.symbol
