def input_data():
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


def calculate_data():
    pass
