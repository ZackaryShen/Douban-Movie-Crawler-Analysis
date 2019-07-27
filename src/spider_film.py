# This py file was written by another group member

import requests
import time
import json
import re
import pandas as pd
from fake_useragent import UserAgent

ua = UserAgent()


def get_index_page(html):
    try:

        headers = {'User-Agent': ua.random}
        response = requests.get(url=html, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions:
        print('获取索引页错误')
        time.sleep(3)
        return get_index_page(html)


# 解析索引页
def parse_index_page(html):
    html = get_index_page(html)
    data = json.loads(html)
    data = data['data']
    for item in data:
        id_list.append(item['url'])


# 获取详情页
def get_detail_page(html):
    try:
        headers = {'User-Agent': ua.random}
        response = requests.get(url=html, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions:
        print('获取详情页错误')
        time.sleep(3)
        return get_detail_page(html)


# 解析详情页
def parse_detail_page(html):
    html = get_detail_page(html)
    info = []
    # 获取电影名称
    name_pattern = re.compile('<span property="v:itemreviewed">(.*?)</span>')
    name = re.findall(name_pattern, str(html))
    info.append(name)
    # 获取评分
    score_pattern = re.compile('rating_num" property="v:average">(.*?)</strong>')
    score = re.findall(score_pattern, str(html))
    info.append(score)
    # 获取导演
    director_pattern = re.compile('rel="v:directedBy">(.*?)</a>')
    director = re.findall(director_pattern, str(html))
    info.append(director)
    # 获取演员
    actor_pattern = re.compile('rel="v:starring">(.*?)</a>')
    actor = re.findall(actor_pattern, str(html))
    info.append(actor)
    # 获取月份
    month_pattern = re.compile('property="v:initialReleaseDate" content="2018-(.*?)-')
    month = re.findall(month_pattern, str(html))
    info.append(month)
    # 获取类型
    type_pattern = re.compile('property="v:genre">(.*?)</span>')
    type = re.findall(type_pattern, str(html))
    info.append(type)
    # 获取时长
    try:
        time_pattern = re.compile('property="v:runtime" content="(.*?)"')
        time = re.findall(time_pattern, str(html))
        info.append(time)
    except:
        info.append('1')
    # 获取语言
    language_pattern = re.compile('pl">语言:</span>(.*?)<br/>')
    language = re.findall(language_pattern, str(html))
    info.append(language)
    # 获取评价人数
    comment_pattern = re.compile('property="v:votes">(.*?)</span>')
    comment = re.findall(comment_pattern, str(html))
    info.append(comment)
    # 获取地区
    area_pattern = re.compile(' class="pl">制片国家/地区:</span>(.*?)<br/>')
    area = re.findall(area_pattern, str(html))
    info.append(area)
    return info


# 爬电影索引url
id_list = []
info_list = []
for i in range(0, 20, 20):    # 已改成0-20来方便测试，改回9970便可爬去2018年全部电影
    parse_index_page(
        "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=" + str(
            i) + "&year_range=2018,2018")
    print(i)

# 把索引写入文件
'''
file=open('list.txt','w')
for temp in id_list:
    file.write(temp+"\n")
file.close()
'''

# 爬电影主页详情data
info_list = []
j = 0
keys = ['电影名', '评分', '导演', '演员', '月份', '类型', '时长', '语言', '评论数', '地区']
for temp in id_list:
    info = parse_detail_page(temp)
    info = dict(zip(keys, info))
    info_list.append(info)
    j = j + 1
    print(j)
    time.sleep(1)

df = pd.DataFrame(info_list)
df.to_csv("data.csv", index=False, sep=',')