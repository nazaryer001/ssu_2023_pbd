import numpy as np

def main():
   arr = np.arange(6).reshape((2, 3))
   print('arr = ', arr)

   tr1 = arr.transpose()
   print('transpose = ', tr1)

   tr2 = arr.T
   print('T = ', tr2)

if __name__ == '__main__':
    main()