import random


def initial_selection(my_list):
    xi = []
    for ml in my_list:
        curr_c = random.choice([0, 1])
        xi.append(curr_c)
    return xi


def first_generation(population, my_list):
    gen = []
    for i in range(0, population):
        curr_gen = initial_selection(my_list)
        if curr_gen in gen:
            #avoid to appending douplicated generaions
            i = i-1
        else:
            gen.append(curr_gen)

    return gen


def fitness(pi_list, gen):
    val = 0
    for g in gen:
        if (g == 1):
            val += pi_list[gen.index(g)]

    return val


if __name__ == '__main__':
    capacity = 100
    wi = [50, 30, 40, 60, 80, 90, 10, 20]
    pi = [10, 3, 12, 40, 5, 15, 4, 22]

    my_list = first_generation(5, wi)
    for ml in my_list:
        print(ml, fitness(pi, ml))