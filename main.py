import random
import pandas as pd
from functions import GeneticAlgorithm


dataframe = pd.read_csv("datasets/knapsack_5_items_new.csv")
GA = GeneticAlgorithm(dataframe)
GA.data_engine()
print(GA.run())


