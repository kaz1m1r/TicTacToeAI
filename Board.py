from typing import List, Union
from typing import Optional  # var: Optional[int] so var is either an integer or None
T = Union[str, int]  # type T is either a string or an integer


class Board:

    def __init__(self):
        """
        Making instance of a Board
        """

        # setting initial board of the Board class
        self.positions = [""] + 9 * [" "]

    def getDiagonals(self) -> list:
        """
        Save the diagonals of the board in a list and return the list
        :return: list
        """

        # saving the values per diagonal in a list
        topLeftDiagonal: List[str] = [self.positions[i] for i in range(1, 10, 4)]
        bottomLeftDiagonal: List[str] = [self.positions[i] for i in range(7, 2, -2)]

        # saving the diagonals in a list
        diagonals: List[List[str]] = [
            topLeftDiagonal,
            bottomLeftDiagonal
        ]

        # returning a list that contains the diagonals of the current board
        return diagonals

    def getColumns(self) -> List[List[str]]:
        """
        Save columns of the board in a list and return the list
        :return: list
        """

        # saving values per column in lists
        leftColumn: List[str] = [self.positions[i] for i in range(1, 8, 3)]
        middleColumn: List[str] = [self.positions[i] for i in range(2, 9, 3)]
        rightColumn: List[str] = [self.positions[i] for i in range(3, 10, 3)]

        # saving columns in a list
        columns: List[List[str]] = [
            leftColumn,
            middleColumn,
            rightColumn
        ]

        # returning list that contains the columns of the current board
        return columns

    def getRows(self) -> List[List[str]]:
        """
        Save rows on the board in a list and return the list
        :return: list
        """

        # saving the values of every row in a list
        topRow: List[str] = [self.positions[i] for i in range(1, 4)]
        middleRow: List[str] = [self.positions[i] for i in range(4, 7)]
        bottomRow: List[str] = [self.positions[i] for i in range(7, 10)]

        # saving the rows in a list
        rows: List[List[str]] = [
            topRow,
            middleRow,
            bottomRow
        ]

        # returning list that contains all the columns of the current board
        return rows

    def insertSymbol(self, symbol: str, position: int) -> None:
        """
        Insert specified symbol on specified position
        :param symbol:
        :param position:
        :return: None
        """
        self.positions[position] = symbol
        self.printBoard()

    def printBoard(self) -> None:
        """
        Print the current board
        :return: None
        """
        print(f""
              f"{self.positions[1]} | {self.positions[2]} | {self.positions[3]}\n"
              f"--+---+--\n"
              f"{self.positions[4]} | {self.positions[5]} | {self.positions[6]}\n"
              f"--+---+--\n"
              f"{self.positions[7]} | {self.positions[8]} | {self.positions[9]}\n"
              )
