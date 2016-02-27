# -*- coding: utf-8 -*-
'''
Copyright@USTC SSE
Author by ch yy in suzhou ,10/12/2015
To recommended best match github user repository
'''
import requests
import json
from github import Github
import networkx as nx
from operator import itemgetter
from collections import Counter
from networkx.readwrite import json_graph
import webbrowser
import os

def start_test(filename):
    client,repo,stargazers,user = getRespond()
    g = addTOGraph(repo,stargazers,user)
    addEdge(stargazers,client,g)
    getPopular(g)
    savaGraph1(g,filename)
    top10(g)
    additional(stargazers,client,g) # 不必须，耗时可不必执行
    saveGraph2(g,filename)
    findOutgoingEdges(g) # 不必须，耗时可不必执行
    addProgramLanguage(g) # 不必须，耗时可不必执行
    stats(g) # 不必须，耗时可不必执行
    saveGraph3(g,filename)
    displayGraph(g,filename)
    webbrowser.open_new_tab("http://%s:%s/%s.html"%("localhost","9999", "display_githubRec"))

def simpleDisplay(ipaddress = "localhost",port = "9999"):
    '''
    利用每次处理后保存的图来进行恢复展示
    :return:
    '''
    # client,repo,stargazers,user = getRespond()
    # g = addTOGraph(repo,stargazers,user)
    # addEdge(stargazers,client,g)
    # getPopular(g)
    # savaGraph1(g)
    # top10(g)
    g = nx.read_gpickle("data/github.1")
    print nx.info(g)
    print

    mtsw_users = [n for n in g if g.node[n]['type'] == 'user']
    h = g.subgraph(mtsw_users)

    print nx.info(h)
    print
    d = json_graph.node_link_data(h)
    json.dump(d, open('data/githubRec.json', 'w'))
    cmdstr = "python3 -m http.server %s" % port
    webbrowser.open_new_tab("http://%s:%s/%s.html"%(ipaddress,port, "display_githubRec"))
    os.system(cmdstr)

def getAuth():
    '''
    获取github API的通关令牌
    :return:
    '''
    username = ''
    password = ''

    url = 'https://api.github.com/authorizations'
    note = 'Mining the Social Web, 2nd E'
    post_data = {'scopes':['repo'],'note': note }

    response = requests.post(url,auth = (username, password),data = json.dumps(post_data),)

    print "API response:", response.text
    print
    print "Your OAuth token is", response.json()['token']

def getRespond(user1 = 'edx',repo1 = 'edx-documentation'):
    '''
    获取原始仓库或者用户的一切API请求,参数是配置查找的用户以及公开仓库
    :return: client,repo,stargazers,user
    '''
    url = "https://api.github.com/repos/%s/%s/stargazers" % (user1, repo1)
    response = requests.get(url)

    print json.dumps(response.json()[0], indent=1)
    print

    for (k,v) in response.headers.items():
        print k, "=>", v

    # ACCESS_TOKEN = '9ebc1b3f8357b7b5a208daafd8a65a7ead7eba19'
    ACCESS_TOKEN = '1161b718b9555cd76bf7ff9070c8f1ba300ea885'

    # 这里配置查找的用户以及公开仓库
    USER = user1
    REPO = repo1

    client = Github(ACCESS_TOKEN, per_page=100)
    user = client.get_user(USER)
    repo = user.get_repo(REPO)

    stargazers = [ s for s in repo.get_stargazers() ] #可以先对这些人数进行分类限制
    print "关注人的数目: ", len(stargazers) #人数众多，速度太慢
    print
    return client,repo,stargazers,user #在这里可以控制人数

def addTOGraph(repo,stargazers,user):
    '''
    添加用户节点和仓库边，构成自我图
    :param repo: 仓库
    :param stargazers: 添加star的用户
    :param user: 原始user
    :return:
    '''
    g = nx.DiGraph()
    g.add_node(repo.name + '(r)', type='repo', lang=repo.language, owner=user.login)

    for sg in stargazers:
        g.add_node(sg.login + '(u)', type='user')
        g.add_edge(sg.login + '(u)', repo.name + '(r)', type='gazes')
        print sg.login + '(u)'

    # print nx.info(g)
    # print

    return g

def addEdge(stargazers,client,g):
    '''
    # 添加关注边，构建兴趣图谱，以获取最受欢迎的top10
    '''
    for i, sg in enumerate(stargazers):
        try:
            for follower in sg.get_followers():#成千上万的跟随者导致速度变慢
                if follower.login + '(u)' in g:
                    g.add_edge(follower.login + '(u)', sg.login + '(u)', type='follows')
        except Exception, e:
            print "获取追随者失败，跳过", sg.login, e

        print "正在处理第", i+1, " 个关注者。"

def getPopular(g):
    print nx.info(g)
    print

    print len([e for e in g.edges_iter(data=True) if e[2]['type'] == 'follows'])
    print

    print len([e for e in g.edges_iter(data=True) if e[2]['type'] == 'follows' and e[1] == 'edx(u)'])
    print

    print sorted([n for n in g.degree_iter()], key=itemgetter(1), reverse=True)[:10]
    print

    c = Counter([e[1] for e in g.edges_iter(data=True) if e[2]['type'] == 'follows'])
    popular_users = [(u, f) for (u, f) in c.most_common() if f > 1]
    print "受欢迎的用户数目：", len(popular_users)
    print "最受欢迎的十个用户：", popular_users[:10]

def savaGraph1(g,name):
    '''
    暂存图节点边的各种信息，因为对于有的star比较多的仓库计算一次不容易
    '''
    filename = "data/" + name + ".1"
    nx.write_gpickle(g, filename)
    # 如果恢复图的信息可以这么使用，g = nx.read_gpickle("github.1")

def top10(g, superNode = 'edx-documentation(repo)'):
    '''
    计算每种度量的top10
    '''
    h = g.copy()
    h.remove_node(superNode) #之所以要去掉原始中心仓库，是因为它是超节点，占用太多的节点关系和边的关系
    dc = sorted(nx.degree_centrality(h).items(), key=itemgetter(1), reverse=True)

    print "点度中心度"
    print dc[:10]
    print

    bc = sorted(nx.betweenness_centrality(h).items(), key=itemgetter(1), reverse=True)

    print "中介中心度"
    print bc[:10]
    print

    print "接近中心度"
    cc = sorted(nx.closeness_centrality(h).items(), key=itemgetter(1), reverse=True)
    print cc[:10]

def additional(stargazers,client,g):
    '''
    向图中加入带star的仓库
    '''
    MAX_REPOS = 500

    for i, sg in enumerate(stargazers):
        print sg.login
        try:
            for starred in sg.get_starred()[:MAX_REPOS]: # Slice to avoid supernodes
                g.add_node(starred.name + '(r)', type='repo', lang=starred.language, owner=starred.owner.login)
                g.add_edge(sg.login + '(u)', starred.name + '(r)', type='gazes')
        except Exception, e: #ssl.SSLError:
            print "获取加星仓库失败　", sg.login, "跳过."

        print "正在处理", i+1, "加星的仓库"

def saveGraph2(g, name):
    filename = "data/" + name + ".2"
    nx.write_gpickle(g, filename)

def findOutgoingEdges(g):
    '''
    承接additional,探索添加加型资源库之后的分析结果
    '''
    print nx.info(g)
    print

    repos = [n for n in g.nodes_iter() if g.node[n]['type'] == 'repo']

    print "Popular repositories"
    print sorted([(n,d)
              for (n,d) in g.in_degree_iter() if g.node[n]['type'] == 'repo'], key=itemgetter(1), reverse=True)[:10]
    print

    print "Respositories that edx has bookmarked"
    print [(n,g.node[n]['lang'])
           for n in g['edx(u)'] if g['edx(u)'][n]['type'] == 'gazes']
    print

    print "Programming languages edx is interested in"
    print list(set([g.node[n]['lang']
                for n in g['edx(u)'] if g['edx(u)'][n]['type'] == 'gazes']))
    print

    print "Supernode candidates"
    print sorted([(n, len(g.out_edges(n)))
                  for n in g.nodes_iter()
                  if g.node[n]['type'] == 'user' and len(g.out_edges(n)) > 500]
                 ,key=itemgetter(1), reverse=True)

def addProgramLanguage(g):
    '''
    给图增加编程语言节点
    '''
    repos = [n for n in g.nodes_iter() if g.node[n]['type'] == 'repo']

    for repo in repos:
        lang = (g.node[repo]['lang'] or "") + "(lang)"

        stargazers = [u for (u, r, d) in g.in_edges_iter(repo, data=True) if d['type'] == 'gazes']

        for sg in stargazers:
            g.add_node(lang, type='lang')
            g.add_edge(sg, lang, type='programs')
            g.add_edge(lang, repo, type='implements')

def stats(g):
    '''
    到目前位置一些调试输出信息
    '''
    print nx.info(g)
    print

    print [n for n in g.nodes_iter() if g.node[n]['type'] == 'lang']
    print

    print [n for n in g['edx(u)'] if g['edx(u)'][n]['type'] == 'programs']

    print "Most popular languages"
    print sorted([(n, g.in_degree(n)) for n in g.nodes_iter() if g.node[n]['type'] == 'lang'], key=itemgetter(1), reverse=True)[:10]
    print

    python_programmers = [u for (u, l) in g.in_edges_iter('Python(lang)') if g.node[u]['type'] == 'user']
    print "Number of Python programmers:", len(python_programmers)
    print

    javascript_programmers = [u for (u, l) in g.in_edges_iter('JavaScript(lang)') if g.node[u]['type'] == 'user']
    print "Number of JavaScript programmers:", len(javascript_programmers)
    print

    print "Number of programmers who use JavaScript and Python"
    print len(set(python_programmers).intersection(set(javascript_programmers)))

    print "Number of programmers who use JavaScript but not Python"
    print len(set(javascript_programmers).difference(set(python_programmers)))

def saveGraph3(g, name):
    filename = "data/" + name + ".3"
    nx.write_gpickle(g, filename)

def displayGraph(g, name):
    print nx.info(g)
    print

    mtsw_users = [n for n in g if g.node[n]['type'] == 'user']
    h = g.subgraph(mtsw_users)

    print nx.info(h)
    print
    d = json_graph.node_link_data(h)
    filename = "data/" + name + ".json"
    json.dump(d, open(filename, 'w'))

