import importlib

from TK_1 import input_data_from_console
from TK_2 import get_cortege
from TK_3 import get_division
from TK_4 import get_multiplication


def main():
    TK_5 = importlib.import_module('TK-5')
    count = int(input('Get count data: '))
    list_data = input_data_from_console(count)
    print('List:', list_data)
    print('Min and max:', get_cortege(list_data))
    print('Division:', get_division(list_data))
    print('Multiplication:', get_multiplication(list_data))
    print('Square:', TK_5.get_square(list_data))
    return 0


if __name__ == '__main__':
    main()
