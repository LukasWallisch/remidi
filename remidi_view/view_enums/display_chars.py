from enum import Enum


class MyEnum(Enum):
    def __str__(self):
        return self.name


class DisplayChars(MyEnum):
    A = [[False, True, True, False],
         [True, False, False, False],
         [True, False, False, True],
         [True, False, False, True],
         [True, True, True, True],
         [True, False, False, True],
         [True, False, False, True],
         [True, False, False, True]]

    B = [[True, True, False, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, True, False, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, True, False, False]]

    C = [[False, True, True, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [False, True, True, False]]

    E = [[True, True, True, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, True, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, True, True, False]]

    F = [[True, True, True, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, True, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False]]

    G = [[True, True, True, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, True, True, False]]

    H = [[True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, True, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False]]

    I = [[False, True, False, False],
         [False, True, False, False],
         [False, True, False, False],
         [False, True, False, False],
         [False, True, False, False],
         [False, True, False, False],
         [False, True, False, False],
         [False, True, False, False]]

    J = [[True, True, True, False],
         [False, False, True, False],
         [False, False, True, False],
         [False, False, True, False],
         [False, False, True, False],
         [False, False, True, False],
         [False, False, True, False],
         [True, True, False, False]]

    K = [[True, False, True, False],
         [True, False, True, False],
         [True, True, False, False],
         [True, False, False, False],
         [True, True, False, False],
         [True, True, False, False],
         [True, False, True, False],
         [True, False, True, False]]

    L = [[True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, True, True, False]]

    M = [[True, False, True, False],
         [True, True, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False]]

    N = [[True, False, False, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, True, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [False, False, True, False]]

    O = [[True, True, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, True, True, False]]

    P = [[True, True, False, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, True, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False],
         [True, False, False, False]]

    Q = [[False, True, False, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, True, True, False],
         [False, False, True, False]]

    R = [[True, True, False, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, True, False, False],
         [True, True, False, False],
         [True, False, True, False],
         [True, False, True, False],
         [True, False, True, False]]

    S = [[False, True, True, False],
         [True, False, False, False],
         [True, False, False, False],
         [False, True, False, False],
         [False, False, True, False],
         [False, False, True, False],
         [False, False, True, False],
         [True, True, False, False]]

    T = [[False, True, False, False],
         [False, True, False, False],
         [False, True, False, False],
         [False, True, False, False],
         [False, True, False, False],
         [False, True, False, False],
         [False, True, False, False],
         [False, True, False, False]]

    U = [[False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False]]

    V = [[False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False]]

    W = [[False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False]]

    X = [[False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False]]

    Y = [[False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False]]

    Z = [[False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False],
         [False, False, False, False]]
