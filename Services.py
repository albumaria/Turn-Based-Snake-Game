from texttable import Texttable
from random import randint


class BoardService:
    def __init__(self, n, apples):
        self.__board = [[" " for _ in range(n)] for _ in range(n)]
        self.__n = n-1
        self.__snake = [[n//2 - 1, n//2], [n//2, n//2], [n//2 + 1, n//2]]
        self.__direction = "up"
        self.set_snake()
        self.__nr_apples = apples
        self.add_apples(self.__nr_apples)

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, new):
        self.__direction = new

    def set_snake(self):
        """
        Sets the snake on the board using the list of positions
        :return:
        """
        self.__board[self.__snake[0][0]][self.__snake[0][1]] = "*"
        for i in range(1, len(self.__snake)):
            self.__board[self.__snake[i][0]][self.__snake[i][1]] = "+"

    def clear_snake(self):
        """
        Completely clears the snake off the board
        :return:
        """
        self.__board[self.__snake[0][0]][self.__snake[0][1]] = " "
        for i in range(1, len(self.__snake)):
            self.__board[self.__snake[i][0]][self.__snake[i][1]] = " "

    def add_apples(self, nr_apples):
        """
        Adds apples to the board
        :param nr_apples: The number of apples
        :return:
        """
        a = 0  # remembers how many apples it has placed
        while a < nr_apples:
            placed = False
            while not placed:
                # randomises coordinates
                i = randint(0, self.__n)
                j = randint(0, self.__n)
                if i == 0:  # if it is on the first row
                    if j == 0:  # and the first column
                        if self.__board[i][j] == " " and self.__board[0][1] != "a" and self.__board[1][0] != "a":
                            placed = True
                            self.__board[i][j] = "a"
                            a += 1
                    elif j == self.__n:  # and the last column
                        if self.__board[i][j] == " " and self.__board[0][self.__n-1] != "a" and self.__board[1][self.__n] != "a":
                            placed = True
                            self.__board[i][j] = "a"
                            a += 1
                    else:  # if it is between first and last columns
                        if self.__board[i][j] == " " and self.__board[0][j-1] != "a" and self.__board[1][j] != "a" and self.__board[0][j+1] != "a":
                            placed = True
                            self.__board[i][j] = "a"
                            a += 1
                elif i == self.__n:  # if it is on the last row
                    if j == 0:  # if it is in the left down corner
                        if self.__board[i][j] == " " and self.__board[i-1][j] != "a" and self.__board[i][j+1] != "a":
                            placed = True
                            self.__board[i][j] = "a"
                            a += 1
                    elif j == self.__n:  # if it is in lower down corner
                        if self.__board[i][j] == " " and self.__board[i-1][j] != "a" and self.__board[i][j-1] != "a":
                            placed = True
                            self.__board[i][j] = "a"
                            a += 1
                    else:  # if it is on the last row between first and last column
                        if self.__board[i][j] == " " and self.__board[i][j-1] != "a" and self.__board[i-1][j] != "a" and self.__board[i][j+1] != "a":
                            placed = True
                            self.__board[i][j] = "a"
                            a += 1
                elif j == 0:  # if it is on the first column
                    if self.__board[i][j] == " " and self.__board[i-1][j] != "a" and self.__board[i][j+1] != "a" and self.__board[i+1][j] != "a":
                        placed = True
                        self.__board[i][j] = "a"
                        a += 1
                elif j == self.__n:  # if it is on the last column
                    if self.__board[i][j] == " " and self.__board[i-1][j] != "a" and self.__board[i][j-1] != "a" and self.__board[i+1][j] != "a":
                        placed = True
                        self.__board[i][j] = "a"
                        a += 1
                else:  # it is somewhere in the interior of the board, we can safely check all positions
                    if self.__board[i][j] == " " and self.__board[i-1][j] != "a" and self.__board[i+1][j] != "a" and self.__board[i][j-1] != "a" and self.__board[i][j+1] != "a":
                        placed = True
                        self.__board[i][j] = "a"
                        a += 1

    def move_snake(self, steps):
        """
        Moves the snake once, in a given direction
        :param steps: Oops, you can replace steps with 1
        :return:
        """
        if self.__direction == "up":
            if self.__snake[0][0] - steps < 0:  # if it hits the border
                return "game over!"
            elif self.__board[self.__snake[0][0] - steps][self.__snake[0][1]] == "+":  # if it hits itself
                return "game over!"
            else:
                self.clear_snake()
                last = self.__snake[len(self.__snake)-1]
                for i in range(len(self.__snake) - 1, 0, -1):
                    self.__snake[i] = self.__snake[i - 1].copy()

                if self.__board[self.__snake[0][0]-steps][self.__snake[0][1]] == "a":
                    self.__snake.append(last)
                    self.add_apples(1)

                self.__snake[0][0] = self.__snake[0][0] - steps
                self.set_snake()

        elif self.__direction == "down":
            if self.__snake[0][0] + steps > self.__n:
                return "game over!"
            elif self.__board[self.__snake[0][0] + steps][self.__snake[0][1]] == "+":
                return "game over!"
            else:
                self.clear_snake()
                last = self.__snake[len(self.__snake)-1]
                for i in range(len(self.__snake) - 1, 0, -1):
                    self.__snake[i] = self.__snake[i - 1].copy()

                if self.__board[self.__snake[0][0]+steps][self.__snake[0][1]] == "a":
                    self.__snake.append(last)
                    self.add_apples(1)

                self.__snake[0][0] = self.__snake[0][0] + steps
                self.set_snake()

        elif self.__direction == "left":
            if self.__snake[0][1] - steps < 0:
                return "game over!"
            elif self.__board[self.__snake[0][0]][self.__snake[0][1]-steps] == "+":
                return "game over!"
            else:
                self.clear_snake()
                last = self.__snake[len(self.__snake)-1]
                for i in range(len(self.__snake) - 1, 0, -1):
                    self.__snake[i] = self.__snake[i - 1].copy()

                if self.__board[self.__snake[0][0]][self.__snake[0][1] - steps] == "a":
                    self.__snake.append(last)
                    self.add_apples(1)

                self.__snake[0][1] = self.__snake[0][1] - steps
                self.set_snake()

        elif self.__direction == "right":
            if self.__snake[0][1] + steps > self.__n:
                return "game over!"
            elif self.__board[self.__snake[0][0]][self.__snake[0][1]+steps] == "+":
                return "game over!"
            else:
                self.clear_snake()
                last = self.__snake[len(self.__snake)-1]
                for i in range(len(self.__snake) - 1, 0, -1):
                    self.__snake[i] = self.__snake[i - 1].copy()

                if self.__board[self.__snake[0][0]][self.__snake[0][1] + steps] == "a":
                    self.__snake.append(last)
                    self.add_apples(1)

                self.__snake[0][1] = self.__snake[0][1] + steps

                self.set_snake()

    def __str__(self):
        """
        Way in which the table is represented
        :return:
        """
        t = Texttable()

        for i in range(self.__n + 1):
            t.add_row(self.__board[i])

        return t.draw()
