#coding:utf-8
import ConfigParser
import requests
from github import Github
import json

def readcfg():
    '''
    read config.cfg file
    :return:github username,password
    '''
    config=ConfigParser.ConfigParser()
    with open('./RecGithub/config.cfg','r') as cfgfile:
        config.readfp(cfgfile)
    user=config.get('info','user')
    passwd=config.get('info','passwd')
    return user,passwd

def GetSearchInfo(location,language):
    '''
    search infomation
    :param location:
    :param language:
    :return:
    '''
    #search 100 users from location,language
    d = {"items":[]}
    url = 'https://api.github.com/search/users?sort=followers&q=location:%s+language:%s&per_page=30&page=' % (location,language)
    rank_count=1

    #获取排名
    print 'chgithub.GetSearchInfo->get start user'
    for i in range(rank_count):
        # print url + str(i+1)
        newUrl = url + str(i+1)
        r = requests.get(newUrl)
        temp = r.json()
        d['items'].extend(temp['items'])

    print 'chgithub.GetSearchInfo->finish rank user'

    #获取用户详细信息
    username,password=readcfg()

    client = Github(login_or_token=username,password=password, per_page=100)
    t = {}
    notdone=[]
    j=0
    for i in d['items']:
        try:
            user = client.get_user(i['login'])
            t[user._rawData['login']] = user._rawData
        except Exception,e:
            print "chgithub.GetSearchInfo->time out"
            print Exception,e
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

def SearchRepo(stars,language):
    d = {"items":[]}
    url = 'https://api.github.com/search/repositories?q=language:%s&stars:>%s&sort=stars&order=desc&per_page=100&page=' % (language,stars)
    rank_count=2

    #获取
    print 'chgithub.SearchRepo->get start repo'
    for i in range(rank_count):
        # print url + str(i+1)
        newUrl = url + str(i+1)
        r = requests.get(newUrl)
        temp = r.json()
        d['items'].extend(temp['items'])

    print 'chgithub.SearchRepo->finish rank repo'

    if len(d):
        filename='./static/bootstrap/data/searchrepo.json'
        json.dump(d, open(filename, 'w'))
        print 'chgithub.GetSearchInfo->DONE'
        return 1
    else:
        print 'chgithub.GetSearchInfo->DONE'
        return 0

def SocialConnect(searchKey):

    username,password=readcfg()

    client = Github(login_or_token=username,password=password, per_page=100)

    user = client.get_user(USER)
    repo = user.get_repo(REPO)

    stargazers = [ s for s in repo.get_stargazers() ] #可以先对这些人数进行分类限制