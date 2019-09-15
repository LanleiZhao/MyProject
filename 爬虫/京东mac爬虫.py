# -*- coding:utf-8 -*-
import requests
import json
import os
import time
import random
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
# import Pillow
import jieba
from PIL import Image

COMMENT_FILE_PATH = 'jd_wawa_comment.txt'
WC_FONT_PATH = 'C:/Windows/Fonts/simsun.ttc'

def spider_comment(page):
    """爬取京东macbook air的评论"""
    # url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv51&produ" \
    #       "ctId=100006728984&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1".format(page)  # macbook


    url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv2628&productId=39992135855&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"  # 娃娃

    headers = {"referer": "https://item.jd.com/39992135855.html",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
               }

    try:
        response = requests.get(url, headers=headers)
        # print(response.status_code)
        response.raise_for_status()
        # print('京东评论数据:'+ response.text[:500])
        # print(response.text[:500])
        # print(response.text[26:])
    except:
        print('获取失败')
    # 获取json数据字符串
    r_json_str = response.text[26:-2]

    # # 字符串转换为json对象
    r_json_object = json.loads(r_json_str)
    r_json_comments = r_json_object['comments']
    print('京东评论数据:')
    # # 遍历评论对象列表
    for r_json_comment in r_json_comments:
    #     # 以追加模式换行写入每条评论
        with open(COMMENT_FILE_PATH, 'a+',encoding='utf-8') as file:
            file.write(r_json_comment['content'] + '\n')
        # 打印评论对象中的评论内容
        print(r_json_comment['content'])


def batch_spider_comment():
    """批量爬取京东评论"""
    # 写入数据之前清空之前的数据
    if os.path.exists(COMMENT_FILE_PATH):
        os.remove(COMMENT_FILE_PATH)
    for i in range(5):
        spider_comment(i)
        # 模拟用户浏览,设置一个爬虫间隔,防止ip被封
        time.sleep(random.random() * 5)

def cut_word():
    """对数据分词"""
    with open(COMMENT_FILE_PATH,encoding='utf-8') as file:
        comment_txt = file.read()
        wordlist = jieba.cut(comment_txt, cut_all=True)
        wl = " ".join(wordlist)
        # print(wl)
        return wl

def create_word_cloud():
    """生成词云"""
    # 设置词云形状图片
    coloring = np.array(Image.open('wawa2.jpg'))
    # 设置词云的一些配置
    wc = WordCloud(background_color='white',max_words=2000,mask=coloring,scale=4,max_font_size=50,random_state=42,
                   font_path=WC_FONT_PATH)
    wc.generate(cut_word())

    plt.imshow(wc,interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()


if __name__ == "__main__":
    # spider_comment(1)
    # batch_spider_comment()
    # cut_word()
    create_word_cloud()