import numpy as np

def main():

   a1 = np.array([[1, 1],
                  [2, 2]])
   a2 = np.array([[3, 3],
                  [4, 4]])
   print('a1 = ', a1)
   print('a2 = ', a2)

   print('vertical stack = ', np.vstack((a1, a2)))

   print('horizontal stack = ', np.hstack((a1, a2)))

   x = np.arange(1, 25).reshape(2, 12)
   print('x = ', x)
   print('split = ', np.hsplit(x, 3))

if __name__ == '__main__':
    main()