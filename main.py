import random


def initial_selection(my_list):
    xi = []
    for ml in my_list:
        curr_c = random.choice([0, 1])
        xi.append(curr_c)
    return xi

if __name__ == '__main__':
    capacity = 100
    wi = [50, 30, 40, 60, 80, 90, 10, 20]
    pi = [10, 3, 12, 40, 5, 15, 4, 22]

    my_list = initial_selection(wi)
    print(my_list)