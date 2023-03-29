import numpy as np

def main():
    a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
                  [0.54627315, 0.05093587, 0.40067661, 0.55645993],
                  [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

    print('a_sum = ', a.sum())

    print('a_min = ', a.min())

    print('a_min_0 = ', a.min(axis=0))

if __name__ == '__main__':
    main()