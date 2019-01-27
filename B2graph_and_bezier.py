# -*- coding: utf-8 -*-

import networkx as nx
from networkx.readwrite import json_graph
import json
import matplotlib.pyplot as plt
import random

LOOP = 7
NODENUM = 4
colorlist = ["r", "g", "b", "c", "m", "y", "k", "pink"] #色

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

def bezier_point(t, v_list):
    ver = v_list
    
    tmp = []
    for i in range(len(ver)-1):
        qx, qy = (t * ver[i][0] + (1-t) * ver[i+1][0]), (t * ver[i][1] + (1-t) * ver[i+1][1])
        tmp.append((qx,qy))

    if len(tmp) == 1:
        return tmp[0][0], tmp[0][1]
    else:
        x, y = bezier_point(t, tmp)
        
    return x, y

def bezierme(V):
    x_bezier=[]
    y_bezier=[]

    for i in range(100):
        x, y = bezier_point(i/100, V)
        x_bezier.append(x)
        y_bezier.append(y)
    return x_bezier, y_bezier


def main():
    V = []
    V = [(0,0),(1,1),(4,-1),(5,0)]

    #for i in range(NODENUM):
    #    V.append((random.random()*20, random.random()*20))
    #bezier_x, bezier_y = bezierme(V)

    Vhalf = []
    for i in range(len(V)):
        if i == 0:
            Vhalf.append(((V[0][0]+V[1][0])*(1/2),(V[0][1]+V[1][1])*(1/2)))
        elif i == NODENUM - 1:
            Vhalf.append(((V[NODENUM - 2][0]+V[NODENUM - 1][0])*(1/2),(V[NODENUM - 2][1]+V[NODENUM - 1][1])*(1/2)))     
        else:
            Vhalf.append(V[i])

    bezier_x, bezier_y = bezierme(Vhalf)

    Gs = []
    g0, p0 = graphme(V)
    Gs.append((g0,p0))

    for t in range(LOOP):
        v = func(V)
        g, p  = graphme(v)
        Gs.append((g,p))
        V = p

    #for i in range(len(Gs)):
    for i in [0,len(Gs)-1]:
        nx.draw(Gs[i][0],Gs[i][1], node_color=colorlist[i], node_size=10)

    plt.plot(bezier_x, bezier_y)

    # 保存
    plt.savefig("test_fig.png")

    # 表示
    plt.show()

if __name__ == "__main__":
    main()