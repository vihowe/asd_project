import numpy as np
# Calculating the time needed for task i when allocated in DC j


# Parameters:
#   data_loc: the location of DC's which stored data 
#   data_amo: the amount of data for DCs
#   Gp: the matrix representing the network of DCs
#   loc: which DC this task is aissgned
#   pre_tasks_loc: the DCs his pres which offers immediate results located
def cal_eta(data_loc, data_amo, Gp, loc, pre_tasks_loc):
    eta = 0.0
    for data in zip(data_loc, data_amo):
        G = Gp.copy()
        G = G.astype(float)
        for i in range(len(G)):
            for j in range(len(G[0])):
                G[i][j] = G[i][j] / data[1]
                print(str(G[i][j]) + " ", end='')
            print()
        # eta += dijstra(G, data[0], loc)
    return eta

if __name__ == "__main__":
    Gp = np.array([
        [100, 100, 10000, 10000],
        [100, 100, 200, 300],
        [10000, 200, 100, 10000],
        [10000, 300, 10000, 100]
    ])
    data_loc = np.array([2, 3])
    data_amo = np.array([200, 300])
    cal_eta(data_loc, data_amo, Gp, 0, 0)
