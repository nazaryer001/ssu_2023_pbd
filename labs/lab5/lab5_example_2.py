import numpy as np

def main():
    arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
    print(np.sort(arr))

    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    print(np.concatenate((a, b)))

    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6]])
    print(np.concatenate((x, y), axis=0))


if __name__ == '__main__':
    main()