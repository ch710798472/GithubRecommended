# -*- coding: utf-8 -*-
'''
Created by ch yy, 08/12/2015
Use svd to recommended edx course
'''
from numpy import *
from numpy import linalg as la

def create_matrix(filename,numbers):
    '''
    :param filename: 需要处理成矩阵的数据文件
    :return returnMat:数据矩阵
    '''
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines,numbers))        #返回向量
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[:numbers]
        index += 1
    print "record count = %d \n" % index
    return mat(returnMat)

def create_testData():
    dataMat = mat(
           [[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
           [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
           [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
           [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
           [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
           [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
           [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
           [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
           [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]])
    return dataMat

#三种距离计算方式，采用基于物品的相似度计算（还有基于内容和基于用户的推荐），
#之所以采用 列向量是因为通常用户的数目大于物品的数目，计算会少很多
def ecludSim(x,y):
    '''
    欧氏距离计算
    :param x:列向量
    :param y:列向量
    :return:欧氏距离
    '''
    return 1.0/(1.0 + la.norm(x - y))

def pearsSim(x,y):
    '''
    皮尔逊相关系数计算，并且把值从-1~1归一化到0~1
    :param x:列向量
    :param y:列向量
    :return:皮尔逊相关系数
    '''
    if len(x) < 3 : return 1.0
    return 0.5+0.5*corrcoef(x, y, rowvar = 0)[0][1]

def cosSim(x,y):
    '''
    余弦相似度计算,并且将值从-1~1归一化到0~1
    :param x:列向量
    :param y:列向量
    :return:余弦相似度
    '''
    num = float(x.T*y)
    d = la.norm(x)*la.norm(y)
    return 0.5+0.5*(num/d)

def est(dataMat, user, meas, course):
    '''
    推荐系统的课程相似性
    :param dataMat: 用户课程矩阵
    :param user: 用户行号
    :param meas: 相似性计算函数
    :param course: 课程
    :return:相似度
    '''
    n = shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    for j in range(n):
        userLine = dataMat[user,j]
        if userLine == 0: continue
        both = nonzero(logical_and(dataMat[:,course].A>0, \
                                      dataMat[:,j].A>0))[0]
        if len(both) == 0: similarity = 0
        else: similarity = meas(dataMat[both,course], \
                                   dataMat[both,j])
        simTotal += similarity
        ratSimTotal += similarity * userLine
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal

def svdsigma(dataMat):
    '''
    calculate S*90% to reduce dataMat 找到90%有效值是包含奇异值
    :param dataMat: 数据矩阵
    :return: 有效的奇异值个数
    '''
    U,S,VT = la.svd(dataMat)
    S1 = S**2
    Ssum = sum(S1)*0.9
    Slen = len(S)
    for i in range(Slen):
        print sum(S1[:i])
        if(sum(S1[:i]) > Ssum):
            sumTemp = i
            break
    if abs(sum(S1[:sumTemp])-Ssum) > abs(sum(S1[:sumTemp-1])-Ssum) :
        Sn = sumTemp-1
    else:
        Sn = sumTemp
    return Sn+1

def svd(dataMat, user, meas, course,Sn):
    '''
    采用了svd奇异矩阵来简化大量数据的相似度计算
    :param dataMat: 数据矩阵
    :param user: 用户行号
    :param meas: 相似性计算函数
    :param course: 课程
    :return:相似度
    '''
    n = shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    U,S,VT = la.svd(dataMat)
    Sig = mat(eye(Sn)*S[:Sn])
    xformedCourses = dataMat.T * U[:,:Sn] * Sig.I
    for j in range(n):
        userLine = dataMat[user,j]
        if userLine == 0 or j==course: continue
        similarity = meas(xformedCourses[course,:].T,\
                             xformedCourses[j,:].T)
        simTotal += similarity
        ratSimTotal += similarity * userLine
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal

def recommended(dataMat, user, N=3, meas=cosSim, estMethod=est):
    '''
    推荐算法
    :param dataMat: 数据矩阵
    :param user: 用户行号
    :param N: 推荐前N个
    :param meas: 相似度计算函数
    :param estMethod: svd函数
    :return:前N个推荐课程
    '''
    unratedCourses = nonzero(dataMat[user,:].A==0)[1]
    if len(unratedCourses) == 0: return 'you have complete all course'
    courseScores = []
    Sn = svdsigma(dataMat)
    for course in unratedCourses:
        svdScore = estMethod(dataMat, user, meas, course,Sn)
        courseScores.append((course, svdScore))
    return sorted(courseScores, key=lambda bb: bb[1], reverse=True)[:N]

def start_test():
    # dataMat = create_matrix("edx_course.csv")
    dataMat = create_testData()
    return recommended(dataMat, 1, meas=pearsSim , estMethod=svd)