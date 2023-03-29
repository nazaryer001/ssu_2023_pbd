import numpy as np

def main():

   data = np.array([[1, 2], [5, 3], [4, 6]])
   print('data = ', data)

   max_0 = data.max(axis=0)
   print('max_0 = ', max_0)

   max_1 = data.max(axis=1)
   print('max_1 = ', max_1)

   data2 = np.array([[1, 2], [3, 4]])
   ones = np.array([[1, 1], [1, 1]])
   print('data2 = ', data2)
   print('ones = ', ones)
   print('data2 + ones = ', data2 + ones)

   data3 = np.array([[1, 2], [3, 4], [5, 6]])
   ones_row = np.array([[1, 1]])
   print('data3 = ', data3)
   print('ones_row = ', ones_row)
   print('data3 + ones_row = ', data3 + ones_row)

if __name__ == '__main__':
    main()