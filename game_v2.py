"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def my_predict2(number: int = 1) -> int:
    """Угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    ct = 0
    l = 1
    r = 101
    m = (l + r) // 2
    while m != number:
        ct += 1
        if number < m:
            r = m
        else:
            l = m
        m = (l + r) // 2
    return ct

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    return 1
    # count = 0

    # while True:
    #     count += 1
    #     predict_number = np.random.randint(1, 101)  # предполагаемое число
    #     if number == predict_number:
    #         break  # выход из цикла если угадали
    # return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
