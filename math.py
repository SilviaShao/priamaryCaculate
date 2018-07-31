#coding=utf-8
import random


def get_combination(min=1, max=200):
    history = []
    max_count = ((max - min + 1) ** 2) * 3 / 2
    while True:
        if len(history) >= max_count:
            raise StopIteration()

        number1 = random.randint(min, max)
        operator_flag = random.randint(0, 1)
        _max = max if operator_flag else number1
        number2 = random.randint(min, _max)

        combination = (number1, operator_flag, number2)
        if combination not in history:
            history.append(combination)
            yield combination


if __name__ == '__main__':
    combination = get_combination()
    i=0
    for number1, operator_flag, number2 in combination:
        operator = '+' if operator_flag else '-'
        i = i+1
        if i<4:
            with open('c:\\2.csv','a') as f:
                f.write(str(number1 )+ operator+ str( number2 )+' = '+',')
        else:
            with open('c:\\2.csv','a') as f:
                f.write(str(number1 )+ operator+ str( number2 )+' = '+'\n')
                i=0

