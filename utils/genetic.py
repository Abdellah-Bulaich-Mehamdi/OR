import random 
import numpy as np
import matplotlib.pyplot as plt

def fitness(string, v, w, W):
    n = len(string)
    answer, weight = 0, 0
    for i in range(n):
        answer += int(string[i])*v[i]
        weight += int(string[i])*w[i]
    return (weight <= W)*answer

def crossover(a, b, P = .3):
    n = len(a)
    if random.random() < P:
        k = random.randint(1, n-1)
    else:
        k = n-1
    return a[:k] + b[k:], b[:k] + a[k:]

def mutation(d, Q = .3):
    n = len(d)
    if random.random() < Q:
        k = random.randint(0, n - 1)
        l = str(d[:k]) + str(1-int(d[k])) + str(d[k+1:])
        return l
    return d

def selection(D, v, w, W, G, P = .3, Q = .3):
        keep = int(.3*G)
        vals = [fitness(key, v, w, W) for key in D]
        ind = np.argpartition(vals, -keep)[-keep:]
        R = []
        for i in ind:
            R += [D[i]]

        while len(R) < G:
            i, j = random.choices(range(G), weights = vals, k = 2)
            k, l = crossover(D[i], D[j], P)
            k, l = mutation(k, Q), mutation(l, Q)

            if k not in R:
                R.append(k)

            if l not in R:
                R.append(l)

        return R