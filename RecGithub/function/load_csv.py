# -*- coding: utf-8
'''
Copyright@USTC SSE
Author by ch yy in suzhou ,28/11/2015
'''
import pandas as pd
def load_csv_to_knn():
    '''
    导入edx课程学习记录的数据
    course_id,userid_DI,registered,viewed,explored,certified,final_cc_cname_DI,LoE_DI,YoB,
    gender,grade,start_time_DI,last_event_DI,nevents,ndays_act,nplay_video,nchapters,
    nforum_posts,roles,incomplete_flag
    课程ID,用户ID,注册，浏览者，探索者，认证者，国家,学历,出生日期,
    性别，学习成绩,,注册课程时间,最后交互时间, 课程交互次数,课程访问天数,播放视频次数,学习章节数,
    论坛发帖数，角色，未完成标志
    并且构造出数据集合['nevents', 'ndays_act', 'nplay_video', 'nchapters', 'nforum_posts', 'incomplete_flag']的文件
    '''
    filename = "/home/ch/edx_note/edx_data.csv" #全部数据
    # dic = dict()
    # with open(filename, 'r') as f:
    #     for i in range(1): # 虚读1行
    #         label = f.readline()
    #     fcsv = csv.DictReader(f)
    #     for x in fcsv:
    #         for y in label.split(','):
    #             dic[y]=x
    edx_data = pd.read_csv(filename,nrows = 10000) # 读取nrows条
    # print edx_data['course_id'].describe()#一些简单的统计信息
    #print edx_data['incomplete_flag'].sum()
    # 构造数据集合,'nevents', 'ndays_act', 'nplay_video', 'nchapters', 'nforum_posts', 'incomplete_flag'为每一列的特征含义
    edx_data.to_csv('data/edx_knn.csv', index=False, header=False, sep='\t',
                    cols=['nevents', 'ndays_act', 'nplay_video', 'nchapters', 'nforum_posts', 'incomplete_flag']
                    ,na_rep='0')

def load_csv_to_fptree():
    '''
    导出edx课程学习记录的数据
    viewed,explored,certified,gender,grade,nevents,ndays_act,nplay_video,nchapters,nforum_posts,incomplete_flag
    输出[viewed,explored,certified,gender,grade,nevents,ndays_act,nplay_video,nchapters,nforum_posts,incomplete_flag]
    '''
    filename = "/home/ch/edx_note/edx_data.csv"
    edx_data = pd.read_csv(filename) # 读取nrows条,nrows = 100000

    edx_data.to_csv('data/edx_fp.csv', index=False, header=False, sep='\t',
                    cols=['viewed','explored','certified','gender','grade','nevents', 'ndays_act',
                          'nplay_video', 'nchapters', 'nforum_posts', 'incomplete_flag'],na_rep='0')