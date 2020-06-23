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

        self.FRONT = self.state[0]
        self.BACK = self.state[1]
        self.RIGHT = self.state[2]
        self.LEFT = self.state[3]
        self.DOWN = self.state[4]
        self.UP = self.state[5]

    def reset(self):
        pass

    def getCube(self):
        return self.state

    def R(self):
        buffer = np.copy(self.FRONT[:, 2])

        self.FRONT[:, 2] = self.UP[:, 2]
        self.UP[:, 2] = self.BACK[:, 2]
        self.BACK[:, 0] = self.DOWN[:, 2]
        self.DOWN[:, 2] = buffer

        self.RIGHT = np.rot90(self.RIGHT)

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
