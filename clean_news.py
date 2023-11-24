import os
import json
import re

# 创建一个空的字典，用于存储所有的数据
root = "securityNewsData"
month_list1 = ['07', '08', '09', '10', '11', '12']
month_list2 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']


# 判断是否包含韩语
def contains_korean(s):
    pattern = re.compile(u"[\uac00-\ud7ff]")
    return pattern.search(s) is not None


def contains_russian(s):
    pattern = re.compile(u'[\u0400-\u04FF]')
    return pattern.search(s) is not None


def filter_method(s):
    if contains_korean(str(s)):
        return False
    # if contains_russian(str(s)):
    #     return False
    title = s['title']
    if "https" in str(title):
        return False
    return True


def clean_text(text):

    text = re.sub(r"[^a-zA-Z0-9 '-]", '', text)  # 去除所有的特殊字符
    text = re.sub(r'\s+', ' ', text)  # 替换连续的空白字符为单个空格

    return text.strip()


if __name__ == "__main__":
    # 遍历文件夹中的所有文件
    file_list = os.listdir(root)
    for month in month_list1:
        data_2022 = {}
        for filename in file_list:
            if filename.split('_')[1] == '2022' and filename.split('_')[2] == month:

                path = './' + root + '/' + filename
                with open(path, 'r', encoding='UTF-8') as f:
                    # 读取文件内容并转换为Python字典
                    news_list = json.load(f)
                    for news_json in news_list:
                        if filter_method(news_json) is True:
                            key = (news_json['time'], news_json['title'])
                            news_json['title'] = clean_text(news_json['title'])
                            news_json['text'] = clean_text(news_json['text'])
                            data_2022[key] = news_json
        json_list = list(data_2022.values())
        print(len(json_list))
        sorted_list = sorted(json_list, key=lambda x: x['time'], reverse=True)
        # 将字典转换为列表，然后写入新的JSON文件
        with open('output/cleaned_data/cleaned_data_2022_' + month + '.json', 'w', encoding='utf-8') as f:
            json.dump(sorted_list, f, indent=4, ensure_ascii=False)

    for month in month_list2:
        data_2023 = {}
        for filename in file_list:
            if filename.split('_')[1] == '2023' and filename.split('_')[2] == month:
                path = './' + root + '/' + filename
                with (open(path, 'r', encoding='UTF-8') as f):
                    # 读取文件内容并转换为Python字典
                    news_list = json.load(f)
                    for news_json in news_list:
                        if filter_method(news_json) is True:
                            if month == str(news_json['time']).split('-')[1]:
                                key = (news_json['time'], news_json['title'])
                                news_json['title'] = clean_text(news_json['title'])
                                news_json['text'] = clean_text(news_json['text'])
                                data_2023[key] = news_json
        json_list = list(data_2023.values())
        print(len(json_list))
        sorted_list = sorted(json_list, key=lambda x: x['time'], reverse=True)
        # 将字典转换为列表，然后写入新的JSON文件
        with open('output/cleaned_data/cleaned_data_2023_' + month + '.json', 'w', encoding='utf-8') as f:
            json.dump(sorted_list, f, indent=4, ensure_ascii=False)








