import numpy as np

def main():
    a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
    unique_values = np.unique(a)
    print('unique_values = ', unique_values)

    unique_values, indices_list = np.unique(a, return_index=True)
    print('indices_list = ', indices_list)

    unique_values, occurrence_count = np.unique(a, return_counts=True)
    print('occurrence_count = ', occurrence_count)

if __name__ == '__main__':
    main()