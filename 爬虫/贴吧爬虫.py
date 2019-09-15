# -*- coding:utf-8 -*-
import requests

class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.heeaders = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        self.url_temp = "http://www.baidu.com/f?kw="+ tieba_name + "&ie=utf-8&pn={}"

    def get_url_list(self):
        # url_list = []
        # for i in range(5):
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i*50) for i in range(5)]

    def parse_url(self, url):  # 发送请求，获取相应
        response = requests.get(url, headers=self.heeaders)
        return response.content.decode()

    def save_html(self, html_str, page_num):
        file_path = "{}吧第{}页.html".format(self.tieba_name,page_num)
        with open(file_path,'w',encoding='utf-8') as f:
            f.write(html_str)
        print('-----is saving {}吧第{}页.html'.format(self.tieba_name, page_num))

    def run(self):  # 实现主要逻辑
        # 1. 构造url列表
        url_list = self.get_url_list()

        # 2. 遍历，发送请求，获取相应
        for url in url_list:
            html_str = self.parse_url(url)

            # 3. 保存
            page_num = url_list.index(url)+1
            self.save_html(html_str,page_num)
        print('---------done----------')

if __name__ == '__main__':
    tieba_spider = TiebaSpider('李毅')
    tieba_spider.run()
    # print(tieba_spider.get_url_list(),sep='\n')



