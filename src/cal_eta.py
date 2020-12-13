import numpy as np
# Calculating the time needed for task i when allocated in DC j


def dijstra(G, src, des):
    '''Find the shortest path lenght from src to des

    Args:
        G: A graph representing the network
        src: The source node 
        des: The destination node
    
    Returns:
        The length of one shortest path from src to des
    '''
    INT_MAX = 1 << 30
    vertex_number = len(G)
    dis = np.zeros(vertex_number, dtype=float)
    visited = np.zeros(vertex_number, dtype=bool)

    # initialize the dis[]
    for i in range(vertex_number):
        dis[i] = G[src][i]
    
    dis[src] = 0
    visited[src] = True
    while (visited[des]==False):
        index = 0
        min_d = INT_MAX
        for i in range(vertex_number):
            if not visited[i] and dis[i] < min_d:
                min_d = dis[i]
                index = i
        visited[index] = True
        
        # do relaxation
        for i in range(vertex_number):
            if not visited[i] and G[index][i] != INT_MAX and dis[index]+G[index][i] < dis[i]:
                dis[i] = dis[index]+G[index][i]
    return dis[des]


def cal_eta(loc, Gp, data_loc, data_amo):
    ''' Calculating the ETA when put this task in DC_loc
    
    Args:
        loc: which DC this task is aissgned
        Gp: the matrix representing the network of DCs
        data_loc: the location of DC's which stored data 
        data_amo: the amount of required data of DCs
    
    Returns：
        the ETA
    '''
    eta = 0.0
    for data in zip(data_loc, data_amo):
        G = Gp.copy()
        G = G.astype(float)
        for i in range(len(G)):
            for j in range(len(G[0])):
                G[i][j] = G[i][j] / data[1]
                print(str(G[i][j]) + " ", end='')
            print()
        eta += dijstra(G, data[0], loc)
    return eta

if __name__ == "__main__":
    Gp = np.array([
        [100, 100, 10000, 200],
        [100, 100, 200, 300],
        [10000, 200, 100, 10000],
        [200, 300, 10000, 100]
    ])
    data_loc = np.array([2, 3])
    data_amo = np.array([200, 300])
    # cal_eta(data_loc, data_amo, Gp, 0, 0)
    print(dijstra(Gp, 0, 2))
