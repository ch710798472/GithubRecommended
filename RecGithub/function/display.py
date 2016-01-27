# -*- coding: utf-8 -*-
'''
Copyright@USTC SSE
Author by ch yy in suzhou ,08/12/2015
Use d3.js to display
'''
import numpy as np
import d3py
import pandas
import knn as knn1
import fptree as fptree1
import svd as svd1
import networkx as nx
import json
import webbrowser
import os
from networkx.readwrite import json_graph
def knn(ipaddress = "localhost",port = "9999"):
    '''
    用D3.JS展示Knn算法的运行结果
    :return:
    '''
    testNum,errorRate, errorCount, classifierData, realData = knn1.displayData(
        'data/edx_knn.csv');
    x = np.linspace(0,testNum,testNum)
    df = pandas.DataFrame({
    'x' : x,
    'y' : classifierData[:testNum],
    'z' : realData[:testNum],
    })

    print "testNummber = %d \n" % testNum, "error rate : %f \n" % (errorCount/float(testNum)), "error count：%d \n" % errorCount

    webbrowser.open_new_tab("http://%s:%s/%s.html" % (ipaddress, port, "disply_knn"))
    with d3py.PandasFigure(df, 'disply_knn', width=20000, height=200, port = int(port)) as fig:
        fig += d3py.geoms.Line('x', 'y', stroke='BlueViolet')
        fig += d3py.geoms.Line('x', 'z', stroke='DeepPink')
        fig += d3py.xAxis('x', label="test number")
        fig += d3py.yAxis('y', label="test label")
        fig.show()


def githubRec(ipaddress = "localhost",port = "8989"):
    '''
    利用每次处理后保存的图来进行恢复展示
    :return:
    '''
    g = nx.read_gpickle("data/github.1")
    print nx.info(g)
    print

    mtsw_users = [n for n in g if g.node[n]['type'] == 'user']
    h = g.subgraph(mtsw_users)

    print nx.info(h)
    print
    d = json_graph.node_link_data(h)
    json.dump(d, open('data/githubRec.json', 'w'))
    # cmdstr = "python3 -m http.server %s" % port
    webbrowser.open_new_tab("http://%s:%s/%s.html"%(ipaddress,port, "display_githubRec"))
    # os.system(cmdstr)

def fptree():
    fptree1.start_test()

def svd():
    svd1.start_test()

if __name__ == '__main__':
    githubRec()
