# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import time
from matplotlib import animation

start = [1,1]
#1が入るノード（黒色）にウェイトを掛けて壁化
"""
rm_node = np.array(
    [[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,0,0,0,0,0,0,0,0,0,0,0,0,0,8],
     [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]]
)

rm_node = np.rot90(rm_node, -1)
"""

rm_node = np.array(
    [[8,8,8,8,8,8,8],
     [8,0,0,0,0,0,8],
     [8,0,0,8,8,0,8],
     [8,0,0,8,0,0,8],
     [8,0,0,0,0,0,8],
     [8,0,0,0,0,0,8],
     [8,8,8,8,8,8,8]]
)

print rm_node


#ネットワークをまず作る
graph = nx.grid_graph(dim=[rm_node.shape[1], rm_node.shape[0]])

for (u, _) in graph.nodes(data=True):
    if rm_node[u]:
        graph.node[u]['color'] = 'black'
for (u, v, d) in graph.edges(data=True):
    if rm_node[u] or rm_node[v]:
        d['weight'] = np.inf

steps = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]
def step(x, y):
    obstacle_count = 0
    for i in range(len(steps)):
        min_cost = 8
        #print rm_node[x+steps[i][0]][y+steps[i][1]],x+steps[i][0],y+steps[i][1]
        if rm_node[x+steps[i][0]][y+steps[i][1]] != 8:
            rm_node[x+steps[i][0]][y+steps[i][1]] = rm_node[x+steps[i][0]][y+steps[i][1]] + 1

        if rm_node[x+steps[i][0]][y+steps[i][1]] < min_cost and abs(sum(steps[i])) == 1: # only straight
            min_cost = rm_node[x+steps[i][0]][y+steps[i][1]]
            next_x = x+steps[i][0]
            next_y = y+steps[i][1]
    print rm_node
    return next_x, next_y

def initial_cost():
    for i in range(rm_node.shape[0]):
        for j in range(rm_node.shape[1]):
            if i < rm_node.shape[0]-1 and j < rm_node.shape[0]-1 and i > 0 and j > 0 and rm_node[i,j] != 8:
                #print i,j, np.sum(rm_node[-1+i:2+i,-1+j:2+j]==8)
                #print rm_node[-1+i:2+i,-1+j:2+j]
                rm_node[i,j] = np.sum(rm_node[-1+i:2+i,-1+j:2+j]==8)
    print rm_node

initial_cost()
x = 5
y = 1
while True:
    x,y = step(x,y)
    print x,y

#print rm_node[0:3,0:3]
#print rm_node[1,1]
#最短ルートを青色で図示
def update(i): 
    if i != 0:
        plt.cla()
    nx.draw(graph,
        pos=dict((n, n) for n in graph.nodes()),
        node_color=[graph.node[n].get('color', 'red') for n in graph.nodes()],
        node_size=200)
    plt.axis('equal')

fig = plt.figure(figsize=(10,10))
#anim = animation.FuncAnimation(fig, update, frames=len(ans_route), interval=50)
#anim.save('demoanimation.gif', writer='imagemagick', fps=4)    
#anim.save('demoanimation.mp4', writer='ffmpeg') 
#plt.show()
