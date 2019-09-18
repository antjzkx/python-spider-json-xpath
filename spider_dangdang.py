# -*- coding:utf-8 -*-
import  requests
from lxml import html

def spider_dangdang(isbn):

    url = "http://search.dangdang.com/?key={}&act=input".format(isbn)
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    responses = requests.get(url,headers = headers)

    html_data = responses.text
    # print(html_data)
    selector = html.fromstring(html_data)

    ul_list = selector.xpath('//div[@id="search_nature_rg"]/ul/li')
    book_list=[]
    i=0
    for li in ul_list:

        book1 =  li.xpath('./a/@title')[0]
        print(book1)
        src1 =  li.xpath('./a/@href')[0]
        print(src1)
        price1 = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()')[0]
        price1=price1.replace('¥','')
        print(price1)
        store1=li.xpath('./p[@class="search_shangjia"]/a/text()')
        if len(store1) == 0:
            store1 ="当当自营"
        else :
            store1 = store1[0]

        print(store1)
        book_list.append({
            'title':book1,
            'link':src1,
            'price':price1,
            'store':store1,
        })
        # book_list[i] =  {
        #     'id':i,
        #     'book':book1,
        #     'src':src1,
        #     'price':price1,
        #     'store':store1,
        #
        # }

        i = i + 1
        #print(book_list)

    book_list = sorted(book_list,key=lambda x:float(x['price']),reverse=True)

    for book in book_list:
        print(book)
    pass



if __name__=='__main__':
    spider_dangdang('9787115428028')