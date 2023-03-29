import numpy as np

def main():

   arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
   print('arr = ', arr)

   reversed_arr = np.flip(arr)
   print('Reversed Array: ', reversed_arr)

   arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
   print('arr_2d = ', arr_2d)

   reversed_arr_2d = np.flip(arr_2d)
   print('reversed_arr_2d = ', reversed_arr_2d)

   reversed_arr_rows = np.flip(arr_2d, axis=0)
   print('reversed_arr_rows = ', reversed_arr_rows)

if __name__ == '__main__':
    main()