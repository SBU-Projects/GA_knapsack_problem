import random
class GeneticAlgorithm:
    def __init__(self, dataframe):
        print("Genetic Algorithm initialised!")
        self.dataframe = dataframe
        self.MUTATION_RATE = 0.02
        self.CROSSOVER_RATE = 0.2
        self.REPRODUCTION_RATE = 0.78
        self.population = 500


    def data_engine(self):
        self.dataframe["Wi"] = self.dataframe.apply(lambda row: [row['W1'], row['W2'], row['W3'], row['W4'], row['W5']], axis=1)
        self.dataframe["Pi"] = self.dataframe.apply(lambda row: [row['P1'], row['P2'], row['P3'], row['P4'], row['P5']], axis=1)

    def initial_selection(self, my_list):
        xi = []
        for ml in my_list:
            curr_c = random.choice([0, 1])
            xi.append(curr_c)
        return xi

    def first_generation(self, my_list):
        gen = []
        for i in range(0, self.population):
            curr_gen = self.initial_selection(my_list)
            if curr_gen in gen:
                # avoid to appending douplicated generaions
                i = i - 1
            else:
                gen.append(curr_gen)

        return gen

    def fitness(self, pi_list, gen):
        val = 0
        loop_counter = 0
        for g in gen:
            if (g == 1):
                val += pi_list[loop_counter]
            loop_counter += 1

        return val

    def check_cap(self, wi_list, gen):
        val = 0
        loop_counter = 0
        for g in gen:
            if (g == 1):
                val += wi_list[loop_counter]
            loop_counter += 1

        return val

    def selection(self, population, pi):

        parents = []
        random.shuffle(population)

        # tournament between first and second
        if self.fitness(pi, population[0]) > self.fitness(pi, population[1]):
            parents.append(population[0])
        else:
            parents.append(population[1])

        # tournament between third and fourth
        if self.fitness(pi, population[2]) > self.fitness(pi, population[3]):
            parents.append(population[2])
        else:
            parents.append(population[3])

        return parents

    def crossver(self, parents):

        cros_site = len(parents[0]) // 2

        child1 = parents[0][0:cros_site]
        child2 = parents[0][0:cros_site]

        child1.extend(parents[1][cros_site:len(parents[0])])
        child2.extend(parents[0][cros_site:len(parents[0])])

        return [child1, child2]

    def mutate(self, population):
        for pop in population:
            pop_counter = 0
            for p in pop:
                if random.random() < self.MUTATION_RATE:
                    if p == 0:
                        pop[pop_counter] = 1
                    else:
                        pop[pop_counter] = 0

                    pop_counter += 1

        return population

    def next_generation(self, population, pi):
        nextgen = []

        while len(nextgen) < len(population):
            childs = []

            parents = self.selection(population, pi)

            if random.random() < self.REPRODUCTION_RATE:
                childs = parents
            else:
                if random.random() < self.MUTATION_RATE:
                    childs = self.mutate(childs)

                if random.random() < self.CROSSOVER_RATE:
                    childs = self.crossver(parents)

            nextgen.extend(childs)

        return nextgen[:len(population)]

    def genetic_algorithm(self, wi, pi, capacity):
        population = self.first_generation(500, wi)
        print(population)
        answer = 0
        answer_p = []

        for i in range(100):
            for p in population:
                if self.check_cap(wi, p) < capacity:
                    if self.fitness(pi, p) >= answer:
                        answer = self.fitness(pi, p)
                        answer_p = p

                    population = self.next_generation(population, pi)

        print(answer_p, answer)

    def run(self):

        for index, row in self.dataframe.iterrows():
            capacity = row['capacit']
            wi = row['Wi']
            pi = row['Pi']

            print("cap: {}, {}, {}".format(capacity, wi, pi))

