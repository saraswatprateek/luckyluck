from numpy import random
import numpy as np
import math
import matplotlib.pyplot as plt

def get_sample_dataset(sample_size):
    skill = random.randint(low=0, high=100, size=sample_size)
    luck = random.randint(low=0, high=100, size=sample_size)

    return skill, luck

def calculate_performance(skill, luck, dataset_size, luck_factor):
    skill_plus_luck = [ (skill[i]*(1-luck_factor) + luck[i]*luck_factor , i) for i in range(dataset_size)]

    skill_plus_luck.sort(key = lambda x: x[0])

    return skill_plus_luck

def select_top_candidates(skill_plus_luck, dataset_size, top_percent):
    top_candidates = skill_plus_luck[(-1)*math.ceil(dataset_size*(top_percent)/100) : ]
    return top_candidates

def calculate_average_luck_for_top_candidates(sample_size, luck_factor, top_percent):
    skill, luck = get_sample_dataset(sample_size)
    skill_plus_luck = calculate_performance(skill, luck, sample_size, luck_factor)
    top_candidates = select_top_candidates(skill_plus_luck, sample_size, top_percent)

    average_luck_for_top_candidates = sum([ luck[top_candidates[x][1]] for x in range(len(top_candidates))]) / len(top_candidates)

    print(average_luck_for_top_candidates)

    return average_luck_for_top_candidates

def func():
    sample_size = 1000000

    #Plot Graphs

    # 1. average_luck_for_top_candidates vs sample_size
    sample_sizes = [ x for x in range(1000, 100000, 500)]
    average_luck_for_top_candidates = [calculate_average_luck_for_top_candidates(i, 0.05, 0.1) for i in sample_sizes]

    plt.plot(sample_sizes, average_luck_for_top_candidates)
    plt.xlabel('Number of Candidates')
    plt.ylabel('Average Luck for top candidates')
    plt.show()


    # 2. Average luck for top x percent of candidates
    top_precents = list(np.arange(0.1, 100, 0.1))
    average_luck_for_top_candidates = [calculate_average_luck_for_top_candidates(100000, 0.05, i) for i in top_precents]

    plt.plot(top_precents, average_luck_for_top_candidates)
    plt.xlabel('Top percent luck')
    plt.ylabel('Average Luck for top candidates')
    plt.show()

    # 3. Average luck for top 0.1 percent of candidates vs luck_factor
    luck_factors = list(np.arange(0.01, 1, 0.003))
    average_luck_for_top_candidates = [calculate_average_luck_for_top_candidates(100000, i, 0.1) for i in luck_factors]

    plt.plot(luck_factors, average_luck_for_top_candidates)
    plt.xlabel('Percentage of luck in results')
    plt.ylabel('Average Luck for top candidates')
    plt.show()


if __name__ == '__main__':
    func()
