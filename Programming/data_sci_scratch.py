import numpy as np
from functools import reduce

def get_rows(a):
    split = []
    rows = a.shape[0]
    for i in range(rows):
        vec = a[i].reshape(1,rows)
        split.append(vec)
    return split

def get_cols(a):
    split = []
    # cols = a.T.shape[0]
    # for j in range(cols):
    #     split.append(a.T[j])
    cols = a.shape[1]
    for j in range(cols):
        vec = a[:,j].reshape(cols,1)
        split.append(vec)
    return split

def diamond(n):
    base = np.eye(n, dtype=int)
    side = np.eye(n, n-1, dtype=int)
    top = np.concatenate((np.flip(side, 0), base), axis=1)
    bottom = np.flip(top[:n-1], 0)
    diamond = np.concatenate((top, bottom))
    return diamond

def vector_lengths(a):
    aggr = a.sum(axis=1)
    return np.sqrt(aggr)

def vector_angles(x, y):
    prods = (x*y).sum(axis=1)
    denom = np.sqrt((x*x).sum(axis=1)) * np.sqrt((y*y).sum(axis=1))
    rads = np.arccos(np.clip(prods / denom, -1, 1))
    return np.degrees(rads)

def multiplication_table(n):
    left = np.arange(n)
    right = left.reshape((n,1))
    return left * right

def column_comparison(a):
    col_1 = a[:,1]
    col_2 = a[:,a.shape[0]-1]
    sub = col_1 > col_2
    return a[sub]

def first_half_second_half(a):
    splits = np.split(a, 2, axis=1)
    check = splits[0].sum(axis=1) > splits[1].sum(axis=1)
    return a[check]

def most_frequent_first(a, c):
    col = a[:, c]
    _, indices, counts = np.unique(col, return_inverse=True, return_counts=True)
    freq_sorted = np.argsort(counts[indices])
    return np.flip(a[freq_sorted], axis=0)

def matrix_power(a, n):
    mat_range = (a for _ in range(n))
    powered = reduce(lambda a, b: a@b, mat_range)
    return powered

def main():
    a = np.array([[5,0,3,3,7,9,3,5,2,4],
                  [7,6,8,8,1,6,7,7,8,1],
                  [5,9,8,9,4,3,0,3,5,0],
                  [2,3,8,1,3,3,3,7,0,1],
                  [9,9,0,4,7,3,2,7,2,0],
                  [0,4,5,5,6,8,4,1,4,9],
                  [8,1,1,7,9,9,3,6,7,2],
                  [0,3,5,9,4,4,6,4,4,3],
                  [4,4,8,4,3,7,5,5,0,1],
                  [5,9,3,0,5,0,1,2,4,2]])
    b = np.eye(2)
    print(matrix_power(b, 3))

if __name__ == '__main__':
    main()
