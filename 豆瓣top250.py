#
import  requests
from lxml import etree
def spider_douban():
    #爬取top250信息
    movie_list =[]
    for i in range(0,226,25):

        url = "https://movie.douban.com/top250?start={}&filter=".format(i)
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        response = requests.get(url,headers = headers)
        data = response.content
        html = etree.HTML(data)

        ol_list = html.xpath('//div[@id="content"]//ol/li')
        #print(len(ol_list))

        for li  in  ol_list:
            img_url = li.xpath('./div[@class="item"]/div[@class="pic"]/a/img/@src')[0]
            #print(img_url)
            serial_number = li.xpath('./div[@class="item"]/div[@class="pic"]/em/text()')[0]
            #print(serial_number)
            #电影名字
            movie_name = li.xpath('./div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/span/text()')[0]
            #print(movie_name)
            # 导演
            daoyan_name = li.xpath('./div[@class="item"]/div[@class="info"]/div[@class="bd"]/p/text()')
            daoyan_name = ''.join(daoyan_name)
            daoyan_name = daoyan_name.replace(' ','')
            daoyan_name = daoyan_name.replace('\n','')
            daoyan_name = daoyan_name.split('/')
            daoyan_name = ''.join(daoyan_name)
            daoyan_name = daoyan_name.split('\xa0')
            daoyan_name = ' '.join(daoyan_name)



            #print(daoyan_name)
            # 上映日期

            #  国家

            # 类型

            # 评价人数
            pnumber = li.xpath('./div[@class="item"]/div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()')[0]
            pnumber = pnumber.replace('人评价','')
            #print(pnumber)




            movie_list.append({
                "排名": serial_number,
                "img_url":img_url,

                "movie_name":movie_name,
                "daoyan_name": daoyan_name,
                "pnumber":pnumber,
            })

        for movie_info_dict in  movie_list:

            res = requests.get(movie_info_dict['img_url'])

            img_name = '000000{}.jpg'.format(movie_info_dict['排名'])

            if res.status_code==200:
                with open('./top250_img/{}'.format(img_name),'wb')as f:
                    f.write(res.content)
    for li in movie_list:
        print(li)








    pass




if __name__=="__main__":
    spider_douban()

