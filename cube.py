import numpy as np


class Cube:
    def __init__(self):
        self.state = np.array([
            [['W', 'W', 'W'],
             ['W', 'W', 'W'],
             ['W', 'W', 'W']],

            [['R', 'R', 'R'],
             ['R', 'R', 'R'],
             ['R', 'R', 'R']],

            [['B', 'B', 'B'],
             ['B', 'B', 'B'],
             ['B', 'B', 'B']],

            [['Y', 'Y', 'Y'],
             ['Y', 'Y', 'Y'],
             ['Y', 'Y', 'Y']],

            [['O', 'O', 'O'],
             ['O', 'O', 'O'],
             ['O', 'O', 'O']],

            [['G', 'G', 'G'],
             ['G', 'G', 'G'],
             ['G', 'G', 'G']],
        ])

        self.FRONT = np.array(self.state[0])
        self.BACK = np.array(self.state[1])
        self.RIGHT = np.array(self.state[2])
        self.LEFT = np.array(self.state[3])
        self.DOWN = np.array(self.state[4])
        self.UP = np.array(self.state[5])

    def restart(self):
        pass

    def getCube(self):
        return self.state

    def R(self):
        pass

    def L(self):
        pass

    def U(self):
        pass

    def D(self):
        pass

    def F(self):
        pass

    def B(self):
        pass
