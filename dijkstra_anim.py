# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import time
from matplotlib import animation
 
#1が入るノード（黒色）にウェイトを掛けて壁化
rm_node = np.array(
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]
)

rm_node = np.rot90(rm_node, -1)

#ネットワークをまず作る
graph = nx.grid_graph(dim=[rm_node.shape[1], rm_node.shape[0]])

for (u, _) in graph.nodes(data=True):
    if rm_node[u]:
        graph.node[u]['color'] = 'black'
for (u, v, d) in graph.edges(data=True):
    if rm_node[u] or rm_node[v]:
        d['weight'] = np.inf
#後はダイクストラ法で解くだけ
#print(graph.edges(data=True))
t1 = time.time()
ans_route = nx.dijkstra_path(graph, (0, 0), (2, 0))
print(time.time() - t1)

#最短ルートを青色で図示
def update(i):
    print i, ans_route[i]
    if rm_node[ans_route[i]] != 1:
        graph.node[ans_route[i]]['color'] = 'blue'
    if i != 0:
        plt.cla()
    nx.draw(graph,
        pos=dict((n, n) for n in graph.nodes()),
        node_color=[graph.node[n].get('color', 'red') for n in graph.nodes()],
        node_size=200)
    plt.axis('equal')

fig = plt.figure(figsize=(10,10))
anim = animation.FuncAnimation(fig, update, frames=len(ans_route), interval=50)
anim.save('demoanimation.gif', writer='imagemagick', fps=4)    
#plt.show()
