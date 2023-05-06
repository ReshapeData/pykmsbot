from mwclient import Site
from wbs import wbs



def wikiWbs_create(ns='JH',project='XSDD2303-001-02',task='1.08收款条件'):
    '''
    增加项目节点
    :param ns:公司代号
    :param project: 项目号
    :param task: 任务节点
    :return:
    '''

    username = 'Hoolilay@rdBot';
    password = '8jthor7j5ejt90sb96qov35hs9ah9h44'
    site = Site(host='106.54.172.90:8401', scheme='http',path='/')
    site.login(username, password)
    page_title = ns +':'+project+' '+task
    #page_title = 'JH:XSDD2303-001-02 1.08收款条件 '
    page_content = '{{cat|catName='+ns+'|orderName=Task}}{{cat|catName='+project+'}}{{cat|catName='+task+'}}  \n This is a new page created by rdBot'
    page = site.pages[page_title]
    page.save(page_content, summary='Creating a new page using mwclient')
    res = page.text()
    #print(res)
    return(res)
def wikiDate_create(ns='分类',date='2023-05-05',week='2023W19'):
    '''
    增加日期
    :param ns:
    :param date:
    :param week:
    :return:
    '''
    username = 'Hoolilay@rdBot';
    password = '8jthor7j5ejt90sb96qov35hs9ah9h44'
    site = Site(host='106.54.172.90:8401', scheme='http',path='/')
    site.login(username, password)
    page_title = ns +':'+date
    page_content = '{{cat|catName='+week+'|orderName=Res}}  \n This is a new page created by rdBot'
    page = site.pages[page_title]
    page.save(page_content, summary='Creating a new page using mwclient')
    res = page.text()
    #print(res)
    return(res)
def wikiWeek_create(ns='分类',week='2023W19',year='2023'):

    '''
    增加周
    :param ns:
    :param week:
    :param year:
    :return:
    '''
    username = 'Hoolilay@rdBot';
    password = '8jthor7j5ejt90sb96qov35hs9ah9h44'
    site = Site(host='106.54.172.90:8401', scheme='http',path='/')
    site.login(username, password)
    page_title = ns +':'+week
    page_content = '{{cat|catName='+year+'|orderName=Res}}  \n This is a new page created by rdBot'
    page = site.pages[page_title]
    page.save(page_content, summary='Creating a new page using mwclient')
    res = page.text()
    #print(res)
    return(res)
def wikiHr_create(ns='分类',name='胡歌'):

    '''
    添加顾问
    :param ns:
    :param name:
    :return:
    '''

    username = 'Hoolilay@rdBot';
    password = '8jthor7j5ejt90sb96qov35hs9ah9h44'
    site = Site(host='106.54.172.90:8401', scheme='http',path='/')
    site.login(username, password)
    page_title = ns +':'+name
    page_content = '{{cat|catName=棱星顾问|orderName=HR}}  \n This is a new page created by rdBot'
    page = site.pages[page_title]
    page.save(page_content, summary='Creating a new page using mwclient')
    res = page.text()
    #print(res)
    return(res)

def wikiProject_create(ns='JH',project='XSDD2303-001-02'):
    '''
    增加项目所有的项目节点

    :param ns: 公司代号
    :param project: 项目编码
    :return:
    '''

    for task in wbs:

        paper = wikiWbs_create(ns=ns, project=project, task=task)

        print(task)
# def wikiContract_create(ns='JH'):
#     '''
#
#
#
#     :param ns: 公司代号
#     :return:
#     '''
#     for project in projects:
#         wikiProject_create(ns=ns,project=project)

# if __name__=='__main__':
#     #wikiContract_create(ns='JH')
#     #wikiDate_create(date='2023-04-28',week='2023W18')
#     wikiWeek_create(week='2023W18',year='2023')
#    #wikiHr_create(name='肖桃')




