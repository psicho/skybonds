def main():
    trader_data = [int(i) for i in input().split()]

    bonds_data = []

    while True:
        bond = input()
        if bond != "":
            bonds_data.append([i for i in bond.split()])
        else:
            break
    print("trader data", trader_data)
    print("bonds data", bonds_data)

    extend_bonds_data(trader_data, bonds_data)
    print("bonds data", bonds_data)


def extend_bonds_data(trader_data, bonds_data):
    for i in range(len(bonds_data)):
        data = calculate_data(trader_data, bonds_data[i])
        bonds_data[i].extend(data)
        print(data)


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
    # print('bond_cost >>> ', bond_cost)

    return [round((cost / 100 * 1000 * amount), 1), (bond_cost + bond_income) * amount,
            bond_cost + bond_income]  # полной стоимости лота, полной доходности и доходности на одну облигацию


def select_bonds(trader_data, bonds_data):
    money = trader_data[2]
    bonds_select = []
    data_table = [[0 for _ in range(0, int(trader_data[2]), 1000)] for _ in range(len(bonds_data) + 1)]
    print("data_table", data_table)
    # [[i * j for j in range(m)] for i in range(n)]

    bonds_data.sort(key=lambda x: x[6], reverse=True)

    gain = 0
    for i in range(len(bonds_data)):
        for j in range((trader_data[2] // 1000)):
            # print(j, i)
            # print('data_table[i-1][j]', data_table[i-1][j])
            # print(bonds_data[i][4])
            if bonds_data[i][4] <= (j + 1) * 1000:
                # print((j + 1) * 1000, bonds_data[i][4])
                # print("###>>>>", data_table[i][j-int(bonds_data[i][4] // 1000)] + bonds_data[i][4], (j + 1) * 1000)
                if data_table[i][j - int(bonds_data[i][4] // 1000)] + bonds_data[i][4] <= (j + 1) * 1000:
                    data_table[i+1][j] = max(float(data_table[i][j]), data_table[i][j-int(bonds_data[i][4] // 1000)] + bonds_data[i][4])
                elif data_table[i][j] + bonds_data[i][4] <= (j + 1) * 1000:
                    # data_table[i][j]
                    data_table[i+1][j] = max(float(data_table[i][j] + bonds_data[i][4]), float(bonds_data[i][4]))
                elif bonds_data[i][4] > data_table[i][j]:
                    data_table[i + 1][j] = bonds_data[i][4]
                else:
                    data_table[i + 1][j] = data_table[i][j]
            else:
                data_table[i + 1][j] = data_table[i][j]

            # if bonds_data[i][4] <= money:
            #     bonds_select.append(bonds_data[i])
            #     if money - bonds_data[i][4] >= bonds_data[i+1][4]:
            #         money -= bonds_data[i][4]
            #         gain += bonds_data[i][5]
            #     # else:

    print(">>> ", data_table)

    # pass


# if __name__ == "__main__":
#     main()



# main()

trader_data = [2, 2, 8000]
bonds_data = [['1', 'alfa-05', '100.2', '2'], ['2', 'alfa-05', '101.5', '5'], ['2', 'gazprom-17', '100.0', '2']]

extend_bonds_data(trader_data, bonds_data)
print("bonds data", bonds_data)

select_bonds(trader_data, bonds_data)
print("bonds data", bonds_data)
