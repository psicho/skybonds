"""
Задача на конвертацию в процентное представление передаваемых значений
1. Сложность алгоритма: O(n*W), где n - количество облигаций; W - доступное количество средств у трейдера деленое на 1000
2. Ограничение на размер передаваемых параметров: не оценивалось
3. Сложность задачи: 8
4. Затраченное время: 8 часов.
"""

# Основная функция запуска расчета
def main():
    trader_data = [int(i) for i in input().split()]

    bonds_data = []

    while True:
        bond = input()
        if bond != "":
            bonds_data.append([i for i in bond.split()])
        else:
            break

    extend_bonds_data(trader_data, bonds_data)

    select_bonds(trader_data, bonds_data)


# Обработка входных данных с занесение в список
def extend_bonds_data(trader_data, bonds_data):
    for i in range(len(bonds_data)):
        data = calculate_data(trader_data, bonds_data[i])
        bonds_data[i].extend(data)


# Позиционная обработка входных данных
def calculate_data(trader_data, one_bond_data):
    day = int(one_bond_data[0])  # День выхода предложения облигации
    name = one_bond_data[1]  # Название облигации
    cost = float(one_bond_data[2])  # Процентная стоимость облигации
    amount = int(one_bond_data[3])  # Количество облигаций

    amount_days = trader_data[0]  # Количество дней за которые у трейдера есть информация о предложениях
    max_day_lots = trader_data[1]  # Максимальное количество представляемых лотов (позиций) облигаций в день
    money = trader_data[2]  # Доступное количество средств у трейдера

    bond_income = amount_days - day + 30  # расчет доходности в соответствии со временем обращения облигации
    bond_cost = round((1000 - cost / 100 * 1000),
                      1)  # Расчет прибыли от разницы курсово и номинальной стоимости облигации

    return [round((cost / 100 * 1000 * amount), 1), (bond_cost + bond_income) * amount,
            bond_cost + bond_income]  # полной стоимости лота, полной доходности и доходности на одну облигацию


# Функция выбора облигаций
def select_bonds(trader_data, bonds_data):
    # Массив цен, доходностей и выбранных облигаций при динамическом расчете
    data_gain_table = [[[0, 0, []] for _ in range(0, int(trader_data[2]), 1000)] for _ in range(len(bonds_data) + 1)]

    bonds_data.sort(key=lambda x: x[6], reverse=True)

    gain = 0
    for i in range(len(bonds_data)):
        for j in range(int(trader_data[2] // 1000)):
            if ((j + 1) - int(bonds_data[i][4]) // 1000) > 0:
                if (data_gain_table[i][((j + 1) - int(bonds_data[i][4]) // 1000)][0] + bonds_data[i][4] <= (j + 1) * 1000):
                    if (data_gain_table[i][((j + 1) - int(bonds_data[i][4]) // 1000)][1] + bonds_data[i][5]) > data_gain_table[i][j][1]:
                        data_gain_table[i+1][j][1] = data_gain_table[i][j-int(bonds_data[i][4]) // 1000][1] + bonds_data[i][5]
                        data_gain_table[i+1][j][0] = data_gain_table[i][j-int(bonds_data[i][4]) // 1000][0] + bonds_data[i][4]
                        data_gain_table[i + 1][j][2] = data_gain_table[i][j - int(bonds_data[i][4] // 1000)][2].copy()
                        data_gain_table[i + 1][j][2].append(bonds_data[i])
                    else:
                        data_gain_table[i + 1][j][2] = data_gain_table[i][j][2].copy()
                        data_gain_table[i + 1][j][1] = data_gain_table[i][j][1]
                        data_gain_table[i + 1][j][0] = data_gain_table[i][j][0]
                else:
                    data_gain_table[i + 1][j][2] = data_gain_table[i][j][2].copy()
                    data_gain_table[i + 1][j][1] = data_gain_table[i][j][1]
                    data_gain_table[i + 1][j][0] = data_gain_table[i][j][0]
            else:
                data_gain_table[i + 1][j][2] = data_gain_table[i][j][2].copy()
                data_gain_table[i + 1][j][1] = data_gain_table[i][j][1]
                data_gain_table[i + 1][j][0] = data_gain_table[i][j][0]

    # Вывод решения
    print(data_gain_table[-1][-1][1])
    for bond in data_gain_table[-1][-1][2]:
        print(" ".join(bond[:4]))

# Функция для тестирования
def testing():
    trader_data = [2, 2, 8000]
    bonds_data = [['1', 'alfa-05', '100.2', '2'], ['2', 'alfa-05', '101.5', '5'], ['2', 'gazprom-17', '100.0', '2']]

    extend_bonds_data(trader_data, bonds_data)
    # print("bonds data", bonds_data)

    select_bonds(trader_data, bonds_data)
    # print("bonds data", bonds_data)

if __name__ == "__main__":
    main()


# testing()
