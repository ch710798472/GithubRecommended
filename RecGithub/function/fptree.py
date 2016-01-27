# -*- coding: utf-8 -*-
'''
copyright@USTC SSE
author by ch yy in suzhou ,07/12/2015
FP-Growth algorithm find frequent pattern
'''
class treeNode:
    def __init__(self, value, num, parentNode):
        self.name = value
        self.count = num
        self.nodeLink = None
        self.parent = parentNode
        self.children = {} 
    
    def inc(self, num):
        self.count += num
        
    def disp(self, ind=1):
        print '  '*ind, self.name, ' ', self.count
        for child in self.children.values():
            child.disp(ind+1)

def load_data(filename):
    '''
    输出[viewed,explored,certified,gender,grade,nevents,ndays_act,nplay_video,nchapters,nforum_posts,incomplete_flag]
    对应[1     ,2       ,3        ,4     ,5    ,6      ,7        ,8          ,9        ,10          ,11    ]序列数据集
    :param filename:
    :return:
    '''
    f = open(filename)
    result = []
    j = 0
    for line in f.readlines():
        line = line.strip().split('\t')
        i = 0
        temp = []
        for l in line:
            i = i + 1
            if l != '0':
                temp.append(i)
        result.append(temp)
    return result

def start_test():
    '''
    测试开始函数
    :return: 频繁项集
    '''
    dataSet = load_data('data/edx_fp.csv')
    initSet = createInitSet(dataSet)
    fptree,headertab = createTree(initSet,50)
    frequentSet = []
    frequentTree(fptree,headertab,50,set([]),frequentSet)
    print frequentSet

def createInitSet(dataSet):
    '''
    :param dataSet: 要挖掘频繁项集的数据集
    :return: 字典数据集
    '''
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict

def createTree(dataSet, support=1):
    '''
    create FP-tree from dataset
    :param dataSet: 输入数据字典
    :param support: 出现最小次数
    :return:
    '''
    headertab = {}
    for trans in dataSet:
        for item in trans:
            headertab[item] = headertab.get(item, 0) + dataSet[trans]
    for k in headertab.keys():  # 去掉不符合个数要求的频繁项集
        if headertab[k] < support:
            del(headertab[k])
    freqItemSet = set(headertab.keys())
    if len(freqItemSet) == 0: return None, None
    for k in headertab:
        headertab[k] = [headertab[k], None]
    retTree = treeNode('root', 1, None) # 建立一个根节点
    for tranSet, count in dataSet.items():  # 第二次遍历数据集
        localD = {}
        for item in tranSet:
            if item in freqItemSet:
                localD[item] = headertab[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateFpTree(orderedItems, retTree, headertab, count)
    return retTree, headertab

def updateFpTree(items, fptree, headertab, count):
    '''
    :param items: 更新项集
    :param fptree: fp树
    :param headertab: 头指针表
    :param count: treeNode里面的num
    :return:
    '''
    if items[0] in fptree.children: # 看看是否有子节点
        fptree.children[items[0]].inc(count)
    else:
        fptree.children[items[0]] = treeNode(items[0], count, fptree)
        if headertab[items[0]][1] == None:
            headertab[items[0]][1] = fptree.children[items[0]]
        else:
            updateFpHeader(headertab[items[0]][1], fptree.children[items[0]])
    if len(items) > 1:
        updateFpTree(items[1::], fptree.children[items[0]], headertab, count)
        
def updateFpHeader(node, targetNode):
    '''
    更新头指针表
    :param node:
    :param targetNode: 插入节点
    :return:
    '''
    while (node.nodeLink != None):
        node = node.nodeLink
    node.nodeLink = targetNode
        
def ascendTree(leafNode, prefixPath):
    '''
    迭代上溯整个fp树
    :param leafNode:
    :param prefixPath:
    :return:
    '''
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)
    
def findPrefixPath(basePat, treeNode):
    '''
    生成条件模式基，遍历整个头指针链表
    :param basePat:
    :param treeNode:
    :return:
    '''
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats

def frequentTree(fptree, headertab, support, preFix, frequentSet):
    '''
    递归查找频繁项集
    :param fptree:
    :param headertab:
    :param support:
    :param preFix:
    :param frequentSet:
    :return:
    '''
    bigL = [v[0] for v in sorted(headertab.items(), key=lambda p: p[1])]
    for basePat in bigL:
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        # print 'finalFrequent Item: ',newFreqSet
        frequentSet.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headertab[basePat][1])
        # print 'condPattBases :',basePat, condPattBases

        myCondTree, myHead = createTree(condPattBases, support)
        # print 'head from conditional tree: ', myHead
        if myHead != None:
            # print 'conditional tree for: ',newFreqSet
            frequentTree(myCondTree, myHead, support, newFreqSet, frequentSet)

