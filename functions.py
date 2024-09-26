import random
class GeneticAlgorithm:
    def __init__(self, dataframe):
        print("Genetic Algorithm initialised!")
        self.dataframe = dataframe
        self.MUTATION_RATE = 0.02
        self.CROSSOVER_RATE = 0.2
        self.REPRODUCTION_RATE = 0.78

    def data_engine(self):
        self.dataframe["Wi"] = self.dataframe.apply(lambda row: [row['W1'], row['W2'], row['W3'], row['W4'], row['W5']], axis=1)
        self.dataframe["Pi"] = self.dataframe.apply(lambda row: [row['P1'], row['P2'], row['P3'], row['P4'], row['P5']], axis=1)

    def initial_selection(self):
        xi = []
        for wi in self.dataframe["Wi"][0]:
            curr_c = random.choice([0, 1])
            xi.append(curr_c)
        return xi

