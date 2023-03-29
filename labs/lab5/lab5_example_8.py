import numpy as np

def main():

   x = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
   a1 = x.flatten()
   a1[0] = 99
   print('x = ', x)  # Original array
   print('flatten: ', a1)  # New array

   a2 = x.ravel()
   a2[0] = 98
   print('x = ', x)  # Original array
   print('ravel: ', a2)  # New array

if __name__ == '__main__':
    main()