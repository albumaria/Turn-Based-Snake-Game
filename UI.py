class UI:
    @staticmethod
    def startup_manual():
        n = input("Enter n: ")
        while not n.isnumeric():
            print("Incorrect input")
            n = input("Enter n: ")
        n = int(n)

        apples = input("Enter nr. apples: ")
        while not apples.isnumeric():
            print("Incorrect input")
            apples = input("Enter nr. apples: ")
        apples = int(apples)

        return n, apples

    @staticmethod
    def startup_file():
        with open("properties.txt", "r") as f:
            lines = f.readlines()

        for line in lines:
            data = line.strip().split(",")
            n = data[0]
            apples = data[1]

        n = int(n)
        apples = int(apples)

        return n, apples

    @staticmethod
    def input_command():
        command = input("> ")
        command = command.lower()
        parts = command.strip().split()

        return parts
