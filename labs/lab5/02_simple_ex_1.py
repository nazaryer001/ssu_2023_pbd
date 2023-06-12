import numpy as np

def main():
    a = np.arange(6)
    print(a.shape)
    a2 = a[np.newaxis, :]
    print(a2.shape)

if __name__ == '__main__':
    main()
