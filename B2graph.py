# -*- coding: utf-8 -*-

import networkx as nx
from networkx.readwrite import json_graph
import json
import pylab
import matplotlib.pyplot as plt
import random
import scipy.misc as scm
import numpy as np

LOOP = 7
NODENUM = 5
colorlist = ["r", "g", "b", "c", "m", "y", "k", "pink"]

def func(vertex):
    v_list = []

    for i in range(len(vertex) - 1):
        qx, qy = (3 * vertex[i][0] + 1 * vertex[i+1][0])  / (1 + 3), (3 * vertex[i][1] + 1 * vertex[i+1][1])  / (1 + 3)
        rx, ry = (1 * vertex[i][0] + 3 * vertex[i+1][0])  / (1 + 3), (1 * vertex[i][1] + 3 * vertex[i+1][1])  / (1 + 3)

        v_list.append((qx, qy))
        v_list.append((rx, ry))

    return v_list

def graphme(v_list):
    G = nx.Graph()
    pos={}

    for v in range(len(v_list)):
        G.add_node(v)
        pos[v]=(v_list[v][0], v_list[v][1])

    for i in range(len(v_list) - 1):
        G.add_edge(i, i+1)

    return G, pos


def main():
    V = [(0,0),(1,1),(4,-1),(5,0)]

    #for i in range(NODENUM):
    #    V.append((random.random()*20, random.random()*20))



    Gs = []
    g0, p0 = graphme(V)
    Gs.append((g0,p0))

    for t in range(LOOP):
        v = func(V)
        g, p  = graphme(v)
        Gs.append((g,p))
        V = p

    for i in [0,7]:
        nx.draw(Gs[i][0],Gs[i][1], node_color=colorlist[i], node_size=10)

    # 保存
    plt.savefig("test_fig.png")

    # 表示
    plt.show()

if __name__ == "__main__":
    main()