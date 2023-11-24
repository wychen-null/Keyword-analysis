import requests
from bs4 import BeautifulSoup
import json
import time
import re
from fake_useragent import UserAgent


def security_scraper(html, count):
    news_list = []

    for date in range(150):
        print("Round is " + str(date))
        #获取时间值 获取不到就下一个
        news_time = html.find('div', class_="date")
        time_str = news_time.text
        if len(time_str) > 0:
            print(time_str)
            news_date, news_weekday = news_time.text.split(' ')
        else:
            html = get_previous_page(html)

        links = html.find_all('div', class_='report-link')
        #如果links数组不为0
        if len(links) != 0:
            for link in links:
                try:
                    article_url = link.find('a').text
                    title, content = find_security_news(article_url)
                    if contains_chinese(content) is True or title is None:
                        print("Contains Chinese")
                        continue
                    news_info = {
                        "time": news_date,
                        "title": title,
                        "text": content
                    }
                    print(news_info)
                    print("======================================================================")
                    news_list.append(news_info)

                except Exception as err:
                    print(err)
                    continue
            if len(news_list) > 0:
                write_in_json(news_list, news_date)
                news_list = []
                count = count + len(news_list)
                print("======================================================================")
        html = get_previous_page(html)

    return count


def get_previous_page(html):
    previous = html.find('a', class_="prev").get("href")
    pre_url = 'https://cert.360.cn/' + previous
    print(pre_url)
    ua = UserAgent()
    send_headers = {'User-Agent': ua.random}
    time.sleep(3)
    pre_response = requests.get(pre_url, headers=send_headers)
    html = BeautifulSoup(pre_response.text, 'html.parser')
    return html


def write_in_json(news_list, date_str):
    file_name = "securityNewsData/SecurityNews_" + date_str.replace("-", "_") + ".json"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(news_list, f, indent=3, ensure_ascii=False)


def contains_chinese(text):
   chinese_pattern = re.compile(u'[\u4e00-\u9fa5]')
   match = chinese_pattern.search(text)
   return match is not None


def find_security_news(url):
    print(url)
    ua = UserAgent()
    send_headers = {'User-Agent': ua.random}
    art_response = requests.get(url, headers=send_headers)
    # art_response = requests.get(url)
    time.sleep(5)
    if art_response.status_code == 200:
        art_html = BeautifulSoup(art_response.text, 'html.parser')
        # title
        try:
            title_head = art_html.find('head').find('title')
            title = title_head.text
        except:
            title = None

        # text
        if art_html.find('div', class_='articleBody'):
            paragraphs = art_html.find('div', class_='articleBody').find_all('p')
        else:
            paragraphs = art_html.find_all('p')
        content = " "
        for para in paragraphs:
            if para.find('a') is None:
                text = para.text
                if text:
                    content = content + text
        return title, content
    return None, None


if __name__ == "__main__":
    root = 'https://cert.360.cn/'
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    root_url = root + "/daily?date=2023-11-24"
    response = requests.get(root_url, headers=send_headers)
    html = BeautifulSoup(response.text, 'html.parser')
    count = security_scraper(html, 0)

    print("Total news:", count)

