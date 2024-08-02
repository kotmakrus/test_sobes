f = open('27_B.txt')
n = int(f.readline())   # количество чисел
k, total = 89, 0    # изначальные данные
max_sum, min_len = 0, 10 ** 10    #макс. сумма и ее мин. длина


elements = {0: (0, 0)}  # словарь, ключ - текущая сумма, значение - ее длина

for j in range(1, n + 1):   # идем по всем числам
    total += int(f.readline())  # вводим и сразу суммируем в текущую сумму
    if total % k in elements:   # если сумма делится на K=89
        if total - elements[total % k][0] > max_sum: # проверяем максимальна ли она, если да
            max_sum = total - elements[total % k][0]    # сохраняем ее
            min_len = 10 ** 10  # мин. длина более не актуальна, поскольку был найден новый максимум
        if total - elements[total % k][0] == max_sum:   # если текущая сумма равна максимальной
            min_len = min(min_len, j - elements[total % k][1])  # переписываем мин. длину
    else:    # если сумма не делится на K=89
        elements[total % k] = (total, j)    # добавляем ее значение и позицию элемента в словарь для дальнейших возможных
                                            # сумм с такими же остатками

print(min_len)
