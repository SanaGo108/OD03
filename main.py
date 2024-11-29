mas = [5, 10, 7, 4, 0, 17, 3, 8, -11, 34, 2, 45, -4, -8]
n = len(mas)  # Можно определить n на основе длины списка

for run in range(n - 1):
    for i in range(n - 1 - run):  # Уменьшаем количество проверяемых элементов с каждым проходом
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]

print(mas)