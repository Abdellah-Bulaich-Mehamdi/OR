def knapsack(k, v, w, W):
    if k < 1:
        if w[k] <= W: 
            return v[k]
        return 0
    else:
        a = 0
        if w[k] <= W:
            a = knapsack(k-1, v, w, W - w[k]) + v[k]
        b = knapsack(k-1, v, w, W)
    return max(a,b)

def Knapsack(v, w, W):
    return knapsack(len(v)-1, v, w, W)