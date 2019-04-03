"""
Задача на конвертацию в процентное представление передаваемых долей
1. Сложность алгоритма: O(n)
2. Ограничение на размер передаваемых параметров:
3. Сложность задачи: 1
4. Затраченное время: менее 10 минут.
"""

count_share = int(input())
share_digit = []

for _ in range(count_share):
    share_digit.append(float(input()))

sum_share_digit = sum(share_digit)

for i in share_digit:
    print(round(i / sum_share_digit, 3))
