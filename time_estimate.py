import time


# start_time = time.time()



# def time_work(func):
#     start_time = time.time()
#     func()
#     print(" Время работы алготитма: " + str(time.time() - start_time) + " сек.")


# Task 1
# @time_work
def percent(args, kwargs):
    count_share = (input(args))
    share_digit = []
    print(kwargs)

    for share in list(kwargs):
        share_digit.append(float(input(share)))

    sum_share_digit = sum(share_digit)

    for share in share_digit:
        print(round(share / sum_share_digit, 3))


for complex_calsulate in range(10, 10**9):
    shares = [share for share in range(complex_calsulate)]
    # print(shares)
    start_time = time.time()
    percent(complex_calsulate, list(shares))
    print(" Время работы алготитма: " + str(time.time() - start_time) + " сек.")
