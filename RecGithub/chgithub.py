#coding:utf-8
import ConfigParser
import requests
from github import Github
import json

def readcfg():
    config=ConfigParser.ConfigParser()
    with open('config.cfg','r') as cfgfile:
        config.readfp(cfgfile)
    user=config.get('info','user')
    passwd=config.get('info','passwd')
    return user,passwd

def GetSearchInfo(location,language):
    #search 100 users from location,language
    d = {"items":[]}
    url = 'https://api.github.com/search/users?sort=followers&q=location:%s+language:%s&per_page=100&page=' % (location,language)
    rank_count=1

    #获取排名
    for i in range(rank_count):
        print url + str(i+1)
        newUrl = url + str(i+1)
        r = requests.get(newUrl)
        temp = r.json()
        d['items'].extend(temp['items'])

    print 'chgithub.GetSearchInfo->finish rank user'

    #获取用户详细信息
    username,password=readcfg()
    ACCESS_TOKEN = '0d1c6d6da836bc28b691f87dd34a1fbdc604c895'
    client = Github(username,password=password, per_page=100)
    t = {}
    notdone=[]
    j=0
    for i in d['items']:
        try:
            user = client.get_user(i['login'])
            t[user._rawData['login']] = user._rawData
        except Exception,e:
            print "GetSearchInfo->time out"
            notdone.append(i['login'])
        if (j%10)==0:
            print j
        j = j + 1

    print 'chgithub.GetSearchInfo->finish user info'

    #重新排序

    d1 = []#最后的结果存储
    for i in d['items']:
        for k in t:
            try:
                if i['login'] == k:
#                   print k
                    d1.append(t[k])
#                   apendx.append(k)
            except Exception,e:
                pass

    print 'chgithub.GetSearchInfo->DONE'

    if len(d1):
        # filename=+ location+ '_'+language+ '.json'
        filename='./static/bootstrap/data/search.json'
        json.dump(d1, open(filename, 'w'))
        return 1
    else:
        return 0