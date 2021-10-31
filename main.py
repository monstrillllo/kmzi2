import math

import numpy as np


def permutation_encryption(text: str, key: int, type_: str = 'encrypt') -> str:
    matrix = np.array([l for l in text])
    row_size = math.ceil(matrix.size / key)
    if type_ != 'encrypt':
        pose = -1
        for i in range(key - matrix.size % key, 0, -1):
            if i == 1:
                matrix = np.append(matrix, '')
            else:
                matrix = np.insert(matrix, pose - (row_size * (i - 1) - i), '')
    # print(matrix)
    while matrix.size % key != 0:
        matrix = np.append(matrix, '')
    # print(f'Исходный список: \n{matrix}')
    matrix = np.reshape(matrix, (row_size, key) if type_ == 'encrypt' else (key, row_size))
    # print(f'Исходная матрица: \n{matrix}\n')
    matrix = matrix.T
    # print(f'Т матрица: \n{matrix}')
    matrix = np.reshape(matrix, -1)
    result_string = ''
    for l in matrix:
        result_string += l
    # print(f'Зашифрованная строка: \n{result_string}')
    return result_string


def main():
    text = input('Text to text for encryption: ')
    key = int(input('Encryption key (table size): '))
    result = permutation_encryption(text, key)
    print(f'Encrypted string: {result}')
    print(f"Decrypted string: {permutation_encryption(result, key, type_='decrypt')}")
    # print(np.array([[1, 2, 3], [1, 2]]))


if __name__ == '__main__':
    main()
