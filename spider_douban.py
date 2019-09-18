import requests
from lxml import html

def spider_douban(city):

    url = "https://movie.douban.com/cinema/later/{}/".format(city)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    requenese = requests.get(url,headers = headers)

    html_data = requenese.text
    selector = html.fromstring(html_data)

    ul_list = selector.xpath('//div[@id="showing-soon"]/div')
    moive_list = []
    for li  in ul_list:
        name = li.xpath('./div/h3/a/text()')[0]
        #print(name)
        li_list = li.xpath('./div/ul/li/text()')
        time = li_list[0]
        #print(time)
        cate = li_list[1]
        #print(cate)
        country = li_list[2]
        #print(country)
        #print(li_list)
        pnumber = li.xpath('./div/ul/li/span/text()')[0]
        pnumber=pnumber.replace('人想看','')
        #print(pnumber)
        moive_list.append({
            'name': name,
            'time': time,
            'cate': cate,
            'country':country,
            'pnumber':pnumber,
        }
        )
        # for n in li_list:
        #     time = n.xpath('./li/text()')
    moive_list = sorted(moive_list,key=lambda x:int(x['pnumber']),reverse=True)

    for li in moive_list:
        print(li)

if  __name__ == '__main__':
    spider_douban('wuhan')