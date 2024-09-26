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

    def fitness(pi_list, gen):
        val = 0
        loop_counter = 0
        for g in gen:
            if (g == 1):
                val += pi_list[loop_counter]
            loop_counter += 1

        return val

