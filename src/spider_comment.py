# This py file was written by another group member

import requests
import time
import re
from fake_useragent import UserAgent

ua = UserAgent()


# 获取评论用户索引页
def get_name_list(html):
    try:
        headers = {'User-Agent': ua.random}
        response = requests.get(url=html, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions:
        print('获取用户索引页错误')
        time.sleep(3)
        return get_name_list(html)


# 解析评论用户索引页
def parse_name_list(html):
    html = get_name_list(html)
    # 获取评论用户名
    name_pattern = re.compile('https://www.douban.com/people/(.*?)/')
    name = re.findall(name_pattern, str(html))
    # 去重
    name_list.append(list(set(name)))


# 获取评论用户主页
def get_name_page(html):
    try:
        headers = {'User-Agent': ua.random}
        response = requests.get(url=html, headers=headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except requests.exceptions:
        print('获取用户主页错误')
        time.sleep(3)
        return get_name_page(html)


# 解析评论用户主引页
def parse_name_page(html):
    html = get_name_page(html)
    # 获取评论用户名
    sex_pattern = re.compile('<span class="gender (.*?)" />')
    sex = re.findall(sex_pattern, str(html))
    sex_list.append(sex)


name_list = []
sex_list = []

for i in range(0, 200, 20):
    parse_name_list("https://movie.douban.com/subject/26425063/comments?start=" + str(i) + "&limit=20&sort=new_score&status=P&percent_type=h")
    print(i)

j=0
for temp in name_list:
    for temp2 in temp:
        parse_name_page("https://m.douban.com/people/" + str(temp2) + "/")
        j = j + 1
        print(j)
        time.sleep(1)

male = 0
female = 0

for i in sex_list:
    for j in i:
        for k in j:
            if (k == 'm'):
                male += 1
            elif (k == 'f'):
                female += 1

print("男生人数 : ", male)
print("女生人数 : ", female)

