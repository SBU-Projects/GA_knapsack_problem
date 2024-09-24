import random

Mutate_Rate = 0.01
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
    loop_counter = 0
    for g in gen:
        if (g == 1):
            val += pi_list[loop_counter]
        loop_counter += 1

    return val

def selection(population, pi):

    parents = []
    random.shuffle(population)


    # tournament between first and second
    if fitness(pi, population[0]) > fitness(pi, population[1]):
        parents.append(population[0])
    else:
        parents.append(population[1])

    # tournament between third and fourth
    if fitness(pi, population[2]) > fitness(pi, population[3]):
        parents.append(population[2])
    else:
        parents.append(population[3])

    return parents


def crossver(parents):

    cros_site = len(parents[0])//2

    child1 = parents[0][0:cros_site]
    child2 = parents[0][0:cros_site]

    child1.extend(parents[1][cros_site:len(parents[0])])
    child2.extend(parents[0][cros_site:len(parents[0])])

    return [child1, child2]

def mutate(population):
    for pop in population:
        pop_counter = 0
        for p in pop:
            if random.random()<Mutate_Rate:
                print("Mutation is called")
                if p == 0:
                    pop[pop_counter] = 1
                else:
                    pop[pop_counter] = 0

                pop_counter += 1

    return population





if __name__ == '__main__':
    capacity = 100
    wi = [50, 30, 40, 60, 80, 90, 10, 20]
    pi = [10, 3, 12, 40, 5, 15, 4, 22]

    my_list = first_generation(8, wi)
    print(my_list)
    print(mutate(my_list))



