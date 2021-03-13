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
        self.name: str = name
        self.symbol: str = termcolor.colored(symbol, "red")
        self.board: Board = board

    def insertSymbol(self, position: int) -> None:
        """
        Player's method to insert his/her symbol on the board on the specified position
        :param position: integer
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

    def getName(self) -> str:
        """
        Return the name of the player instance
        :return: str
        """
        return self.name

    def getSymbol(self) -> str:
        """
        Return the symbol of the player instance
        :return: str
        """
        return self.symbol
