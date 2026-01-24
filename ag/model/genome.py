import numpy as np

class Genome():

    def __init__(self, params=None):
        if params == 'replica':
            self.L56, self.L68, self.L87, self.L67, self.L32, self.L27, self.L24, self.L47, self.L14, self.J1x, self.J1y, self.J3x, self.J3y, self.J5x, self.J5y = [0.371, 0.529, 0.580, 0.092, 0.087, 0.277, 0.150, 0.169, 0.077, 0, 0, -0.133, 0.0506, -0.171, 0.203]
        elif params is not None:
            self.L56, self.L68, self.L87, self.L67, self.L32, self.L27, self.L24, self.L47, self.L14, self.J1x, self.J1y, self.J3x, self.J3y, self.J5x, self.J5y = params
        else:
            self.L56 = np.random.uniform(0.01, 0.5)
            self.L68 = np.random.uniform(0.01, 1)
            self.L87 = np.random.uniform(0.01, 1)
            self.L67 = np.random.uniform(0.01, 0.2)
            self.L32 = np.random.uniform(0.01, 0.2)
            self.L27 = np.random.uniform(0.01, 0.5)
            self.L24 = np.random.uniform(0.01, 0.3)
            self.L47 = np.random.uniform(0.01, 0.3)
            self.L14 = np.random.uniform(0.01, 0.2)
            self.J3x, self.J3y = np.random.uniform(-0.3, 0.0), np.random.uniform(0, 0.1)