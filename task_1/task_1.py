import random
import math
import numpy as np
from operator import itemgetter


def create_matrix(lbr, rbr, lwh):
    return np.random.random_integers(lbr, rbr, (lwh, lwh, lwh))


def calculation(matrix, lwh):
    pc = []  # product columns
    for z in range(lwh):
        for y in range(lwh):
            for x in range(lwh):
                prox = 1  # product x
                proy = 1  # product y
                proz = 1  # product z
                for n in range(x, lwh):
                    prox *= matrix[n, y, z]  # product x
                for n in range(y, lwh):
                    proy *= matrix[x, n, z]  # product y
                for n in range(z, lwh):
                    proz *= matrix[x, y, n]  # product z
                pro = prox * proy * proz
                pc.append((pro, 'x:%s' % x, 'y:%s' % y, 'z:%s' % z))
    pc.sort(key=itemgetter(0))
    return pc[0]


def main():
    lbr = -9  # left border randomization
    rbr = 9  # right border randomization
    lwh = 10  # length, width, height
    matrix = create_matrix(lbr, rbr, lwh)
    end = calculation(matrix, lwh)
    print('Найменший добуток = %s' % itemgetter(0)(end))
    print('Кординати точки перетину стовпчиків = %s' % itemgetter(1)(end), itemgetter(2)(end), itemgetter(3)(end))

if __name__ == '__main__':
    main()
