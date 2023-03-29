import numpy as np

def main():
    a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a[a < 5])

    divisible_by_2 = a[a%2==0]
    print(divisible_by_2)

    five_up = (a > 5) | (a == 5)
    print(five_up)

if __name__ == '__main__':
    main()