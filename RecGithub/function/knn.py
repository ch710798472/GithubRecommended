# -*- coding: utf-8 -*-
'''
Copyright@USTC SSE
Author by ch yy in suzhou ,28/11/2015
Find out nevents, ndays_act, nplay_video, nchapters, nforum_posts weather or not determined on
         viewed,explored,certified,grade
'''
from numpy import *
import load_csv as lc
import operator

def knn(base, dataSet, labels, k):
    '''
    :param base: 基础数据矩阵用来对其他数据进行分类距离的计算
    :param dataSet: 需要分类的数据集合
    :param labels: 每一条记录真实属于哪一类的标签
    :param k: knn算法中所取的top数量
    :return sortedClassCount:返回排序好的分类数据，是labels值
    '''
    dataSetSize = dataSet.shape[0]
    diffMat = tile(base, (dataSetSize,1)) - dataSet # 重复 max(datasetsize,1) 次
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()     
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1 # 有标签属性了加一，没有则加入
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createMatrix(filename):
    '''
    :param filename: 需要处理成矩阵的数据文件
    :return returnMat,classLabelVector:数据矩阵，数据标签矩阵
    '''
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines,5))        #返回向量
    classLabelVector = []                       #labels
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:5]
        classLabelVector.append(int(round(float(listFromLine[-1])))) #仅仅是为了处理int('1.0')这个错误加了这么多函数
        index += 1
    print "record count = %d \n" % index
    return returnMat,classLabelVector
    
def Normalized(dataSet):
    '''
    :param dataSet: 数据矩阵
    :return normDataSet, ranges, minVals：归一化后的矩阵，取值范围，最小值
    '''
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals                      #处理不同的特征值之间数值的不统一，进行归一化
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #归一化后数值 =（真实数据-最小值）/（最大值-最小值）
    return normDataSet, ranges, minVals
   
def data_test(filename):
    '''
    :param filename: 需要进行分类的文件
    :return: 输出分类结果，以及错误率等
    '''
    how = 0.10      # 测数数据占数据的百分比
    dataMat,dataLabels = createMatrix(filename)
    normMat, ranges, minData = Normalized(dataMat)
    m = normMat.shape[0]
    testNum = int(m*how)
    errorCount = 0.0
    for i in range(testNum):
        classifierResult = knn(normMat[i,:],normMat[testNum:m,:],dataLabels[testNum:m],3)
        print "classifier into : %d, real answer is: %d" % (classifierResult, dataLabels[i])
        if (classifierResult != dataLabels[i]): errorCount += 1.0
    print "error rate : %f \n" % (errorCount/float(testNum))
    print "error count：%d \n" %errorCount

def start_test():
    '''
    导入数据文件，测试knn算法开始函数
    '''
    # lc.load_csv_data()
    data_test('edx_knn.csv')

def displayData(filename):
    how = 0.10      # 测数数据占数据的百分比
    dataMat,dataLabels = createMatrix(filename)
    normMat, ranges, minData = Normalized(dataMat)
    m = normMat.shape[0]
    testNum = int(m*how)
    errorCount = 0.0
    classifierData = []
    realData = []
    for i in range(testNum):
        classifierResult = knn(normMat[i,:],normMat[testNum:m,:],dataLabels[testNum:m],3)
        classifierData.append(classifierResult)
        realData.append(dataLabels[i])
        if (classifierResult != dataLabels[i]): errorCount += 1.0
    return testNum,(errorCount/float(testNum)), errorCount, classifierData, realData