import numpy as np

def main():

    a = np.zeros(2)
    print('a = ', a)

    b = np.arange(2, 9, 2)
    print('b = ', b)

    c = np.linspace(0, 10, num=5)
    print('c = ', c)

if __name__ == '__main__':
    main()