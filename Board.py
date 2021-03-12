class Board:

    def __init__(self):
        """
        Making instance of a Board
        """

        # setting initial board of the Board class
        self.positions = [""] + 9 * [" "]

    def getDiagonals(self):
        """
        Save the diagonals of the board in a list and return the list
        :return: list
        """

        # saving the values per diagonal in a list
        topLeftDiagonal = [self.positions[i] for i in range(1, 10, 4)]
        bottomLeftDiagonal = [self.positions[i] for i in range(7, 2, -2)]

        # saving the diagonals in a list
        diagonals = [
            topLeftDiagonal,
            bottomLeftDiagonal
        ]

        # returning a list that contains the diagonals of the current board
        return diagonals

    def getColumns(self):
        """
        Save columns of the board in a list and return the list
        :return: list
        """

        # saving values per column in lists
        leftColumn = [self.positions[i] for i in range(1, 8, 3)]
        middleColumn = [self.positions[i] for i in range(2, 9, 3)]
        rightColumn = [self.positions[i] for i in range(3, 10, 3)]

        # saving columns in a list
        columns = [
            leftColumn,
            middleColumn,
            rightColumn
        ]

        # returning list that contains the columns of the current board
        return columns

    def getRows(self):
        """
        Save rows on the board in a list and return the list
        :return: list
        """

        # saving the values of every row in a list
        topRow = [self.positions[i] for i in range(1, 4)]
        middleRow = [self.positions[i] for i in range(4, 7)]
        bottomRow = [self.positions[i] for i in range(7, 10)]

        # saving the rows in a list
        rows = [
            topRow,
            middleRow,
            bottomRow
        ]

        # returning list that contains all the columns of the current board
        return rows

    def insertSymbol(self, symbol, position):
        """
        Insert specified symbol on specified position
        :param symbol:
        :param position:
        :return: None
        """
        self.positions[position] = symbol
        self.printBoard()

    def printBoard(self):
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
