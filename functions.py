
class GeneticAlgorithm:
    def __init__(self, dataframe):
        print("Genetic Algorithm initialised!")
        self.dataframe = dataframe
        self.MUTATION_RATE = 0.02
        self.CROSSOVER_RATE = 0.2
        self.REPRODUCTION_RATE = 0.78

    def data_engine(self):
        self.dataframe["Wi"] = self.dataframe.apply(lambda row: [row['W1'], row['W2'], row['W3']], axis=1)

        return self.dataframe
