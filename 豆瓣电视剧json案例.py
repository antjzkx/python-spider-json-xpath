# JSON(JavaScript Object Notation, JS 对象简谱)
# 是一种轻量级的数据交换格式

##  {} json 对象  []json数组
#{"name": "John Doe", "age": 18, "address": {"country" : "china", "zip-code": "10000"}}
"""
json 数组表示
{
"people":[
{
"firstName": "Brett",
"lastName":"McLaughlin"
},
{
"firstName":"Jason",
"lastName":"Hunter"
}
]
}
"""
import requests
import json
# 这是当前页面的信息，并不一定是数据信息
# url = 'https://movie.douban.com/tv/#!type=tv&tag=热门&sort=recommend&page_limit=20&page_start=0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=热门&sort=recommend&page_limit=20&page_start=0'
# XHR  XMLHTTPRequest
response = requests.get(url, headers = headers)
# 把响应数据转化成str类型
data = response.content.decode()
# print(data)
# 把json字符串转化成字典
#  json ======> python
dict_data = json.loads(data)
# print(dict_data)
result_list = dict_data["subjects"]
# print(len(result_list))
# 提取
# 创建空列表 然后存储提取的数据
# 存储形式[{},{},{}] 每一部电视剧是一个字典
data_list = []
for result in result_list:
    temp = {}
    # 所有的电视剧名字
    temp['title'] = result['title']

    # 评分
    temp['rate'] = result['rate']
    # url

    temp['url'] = result['url']

    data_list.append(temp)

for tv in data_list:
    print(tv)

# 存储成json格式

f = open('douban_tv.json', 'w',encoding='utf-8')

json.dump(data_list, f, ensure_ascii=False)