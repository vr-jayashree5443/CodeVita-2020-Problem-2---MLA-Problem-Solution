#!/usr/bin/env python
# coding: utf-8

# In[2]:



m1 = int(input())
m2 = int(input())
N = int(input())
population = list(map(int, input().split()))


def min_vaccination_time(m1, m2, N, population):
    population.sort(reverse=True)
    total_time_1 = 0
    total_time_2 = 0
    for i in range(N):
        if i % 2 == 0:
            total_time_1 += population[i] * m1
        else:
            total_time_2 += population[i] * m2
    return max(total_time_1, total_time_2)

result = min_vaccination_time(m1, m2, N, population)
print(result)


# In[ ]:




