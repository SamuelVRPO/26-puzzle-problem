# The State class contains the two representation of state:
# - Board contains the matrix representation of the board as a three dimensional list [][][]
# - Coordinates is a hashmap with tile numbers as keys and coordinates as values

class State:
    def __init__(self, board, coordinates):
        self.board = board
        self.coordinates = coordinates