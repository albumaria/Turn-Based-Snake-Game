from src.Services import BoardService
from src.UI import UI


class Game:
    def __init__(self):
        self.__ui = UI()
        self.__n, self.__apples = self.__ui.startup_file()

        self.__board = BoardService(self.__n, self.__apples)
        print(self.__board)

    def start(self):
        try:
            while True:
                try:
                    parts = self.__ui.input_command()

                    if len(parts) == 0:
                        raise ValueError("Input a valid command")

                    elif parts[0] == "move":
                        if len(parts) == 2:
                            moves = int(parts[1])
                            end = True
                            while moves != 0:
                                message = self.__board.move_snake(1)
                                if message == "game over!":
                                    end = False
                                    break
                                else:
                                    moves -= 1
                            if end:
                                print(self.__board)
                            elif not end:
                                print("game over!")
                                break

                        elif len(parts) == 1:
                            message = self.__board.move_snake(1)
                            if message == "game over!":
                                print("game over!")
                                break
                            else:
                                print(self.__board)

                    elif (parts[0] == "up" or parts[0] == "right" or parts[0] == "left" or parts[0] == "down") and len(parts) == 1:
                        current_direction = self.__board.direction
                        direction = parts[0]

                        if current_direction == "up" and direction == "down":
                            print("Invalid move")
                        elif current_direction == "left" and direction == "right":
                            print("Invalid move")
                        elif current_direction == "down" and direction == "up":
                            print("Invalid move")
                        elif current_direction == "right" and direction == "left":
                            print("Invalid move")
                        elif current_direction == direction:
                            pass
                        else:
                            self.__board.direction = direction
                            self.__board.move_snake(1)
                            print(self.__board)

                    else:
                        raise ValueError("Invalid input")

                except ValueError as ve:
                    print(ve)

        except ValueError as ve:
            print(ve)


game = Game()
game.start()
