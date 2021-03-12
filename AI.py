from Player import Player
from Board import Board
import termcolor
import math


class Ai(Player):

    def __init__(self, name: str, symbol: str, board: Board, opponent: Player):
        """
        Make an instance of the Ai class
        :param name: str (name of the Ai)
        :param symbol: str (symbol that corresponds with the Ai)
        :param board: Board (instance of the board that the Ai is playing on)
        :param opponent: Player (instance of the opponent of the Ai
        """

        # setting instance variables of the super class
        super().__init__(name, symbol, board)

        # setting instance variables of the Ai class
        self.opponent = opponent
        self.symbol = termcolor.colored(symbol, 'yellow')

    def makeBestMove(self):
        """
        Use the minimax method to find the Ai's optimal move given the current board
        :return: None
        """

        # best return value (1, -1 or 0)
        bestVal = - math.inf
        bestPosition = -math.inf

        # traverse all positions
        for position in range(len(self.board.positions)):

            # check if position is empty
            if self.board.positions[position] == " ":

                # make move
                self.board.positions[position] = self.getSymbol()

                moveValue = self.minimax(0, False)

                # undo move
                self.board.positions[position] = " "

                if moveValue > bestVal:
                    bestPosition = position
                    bestVal = moveValue

        self.insertSymbol(bestPosition)

    def minimax(self, depth: int, is_maximizer: bool):
        """
        Minimax search algorithm that's used to determine whether its beneficial or not for the Ai
         to place it's symbol at the current position of the board
        :param depth: specifies the depth of the tree, in this case the open positions
        :param is_maximizer: specifies whether its the maximizer's turn (Ai) or the minimizer's turn (opponent)
        :return: int
        """

        # determine whether the current board has a winner, loser or if it's not decided and save
        # the outcome to a variable 'score'
        score = self.checkForWinner()

        # return score if the Ai wins the game
        if score == 1:
            return score

        # return the score if the opponent wins the game
        if score == -1:
            return score

        # return 0 if there's no winner
        if not self.areMovesLeft():
            return 0

        # if it's the maximizer's move (AI's move)
        if is_maximizer:
            best = - math.inf

            # traverse all cells
            for position in range(len(self.board.positions)):

                # place symbol if an available position is found on the board
                if self.board.positions[position] == " ":
                    # make move
                    self.board.positions[position] = self.getSymbol()

                    best = max(best, self.minimax(depth + 1, not is_maximizer))

                    # undo the move
                    self.board.positions[position] = " "
            return best

        # if it's the minimizer's turn (opponent's move)
        else:
            best = math.inf

            # traverse all cells
            for position in range(len(self.board.positions)):

                # place symbol if an available position is found on the board
                if self.board.positions[position] == " ":
                    # make move
                    self.board.positions[position] = self.opponent.getSymbol()

                    best = min(best, self.minimax(depth + 1, not is_maximizer))

                    # undo the move
                    self.board.positions[position] = " "
            return best

    def checkForWinner(self):
        """
        Check rows, columns and diagonals for winner
        :return: int
        """

        '''checking rows for a winner'''

        # saving the rows of the board in a variable
        rows = self.board.getRows()

        # iterating through the rows
        for row in rows:

            # return 1 if the Ai has its symbol trice in a row
            if row.count(self.getSymbol()) == 3:
                return 1

            # return -1 if the opponent has its symbol trice in a row
            elif row.count(self.opponent.getSymbol()) == 3:
                return -1

        '''checking columns for a winner'''

        # saving the columns of the board in a variable
        columns = self.board.getColumns()

        # iterating through the columns
        for column in columns:

            # return 1 if the Ai has its symbol trice in a column
            if column.count(self.getSymbol()) == 3:
                return 1

            # return -1 if the opponent has its symbol trice in a column
            elif column.count(self.opponent.getSymbol()) == 3:
                return -1

        '''checking diagonals for a winner'''

        # save the diagonals of the board in a variable
        diagonals = self.board.getDiagonals()

        # iterating through the diagonals
        for diagonal in diagonals:

            # return 1 if the Ai has its symbol trice in a diagonal
            if diagonal.count(self.getSymbol()) == 3:
                return 1

            # return -1 if the opponent has its symbol trice in a diagonal
            elif diagonal.count(self.opponent.getSymbol()) == 3:
                return -1

        # return 0 if neither the Ai nor the opponent has won
        return 0

    def areMovesLeft(self):
        """
        Check if there are empty cells left in the board
        :return: boolean
        """
        for position in self.board.positions:
            if position == " ":
                return True
        return False
