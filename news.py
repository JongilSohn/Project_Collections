
from bs4 import BeautifulSoup
import requests
import json
from flask import Flask, render_template, jsonify, request


def news_card():
    news_result = requests.get(
    'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B7%A8%EC%97%85')
    # 뷰티풀숩을 사용해 Html을 전체 가져온다.
    news_soup = BeautifulSoup(news_result.text, 'html.parser')
    # page 수를 찾기 위해 해당 div를 가져와서 확인한다.
    news_result = requests.get(
    'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B7%A8%EC%97%85')
    # 뷰티풀숩을 사용해 Html을 전체 가져온다.
    news_soup = BeautifulSoup(news_result.text, 'html.parser')
    news_div = news_soup.find("div", {"class": "news mynews section _prs_nws"})
    news_ul = news_div.find("ul", {"class": "type01"})
    news_li = news_ul.find_all("div", {"class": "thumb"})
    news_dl = news_ul.find_all("dl")

    news_link = []
    news_img = []
    news_title = []
    news_content = []

    news_card = []

    for news_links in news_li:
        news_links = news_links.find("a")["href"]
        # print(news_links)
        news_link.append(news_links)

    for news_imgs in news_li:
        news_imgs = news_imgs.find("img")["src"]
        news_imgs = news_imgs.strip("&type=ofullfill80_80_q75_re2%27,")
        # print(news_imgs)
        news_img.append(news_imgs)

    for news_titles in news_dl:
        news_titles = news_titles.find("dt").find("a")["title"]
        news_title.append(news_titles)

    for news_contents in news_dl:
        total_news_contents = news_contents.find_all(
            "dd")[1].get_text(strip=True)
        news_content.append(total_news_contents)

        # print(dd_content)
        # sub_news_contents = news_contents.find_all("dd", {"class":"text_inline"})
        #news_contents = total_news_contents.replace(sub_news_contents,'')
        # print(total_news_contents)

    for n in range(8):
        news_cards = {"news_img": news_img[n], "news_title": news_title[n],
                      "news_link": news_link[n], "news_content": news_content[n]}
    #news_card ={"news_img":news_img, "news_title":news_title, "news_link":news_link}
        news_card.append(news_cards)
    return jsonify ({'result':'success','news_card':news_card})