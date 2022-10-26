#!/usr/bin/python3
import numpy as np

points = np.random.rand(10, 2)

points = [[0,0],[1,0],[1,1],[1,1]]
def evaluate(path):
    print(path)
    print(np.linalg.norm(path))
# np.random.shuffle(points)
evaluate(points)
