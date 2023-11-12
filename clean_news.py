import os
import json
import re

# 创建一个空的字典，用于存储所有的数据
data = {}
root = "securityNewsData"

#判断是否包含韩语
def contains_korean(s):
   pattern = re.compile(u"[\uac00-\ud7ff]")
   return pattern.search(s) is not None


if __name__ == "__main__":
    # 遍历文件夹中的所有文件
    file_list = os.listdir(root)
    for filename in file_list:
        if filename.endswith('.json'):
            path = './' + root + '/' + filename
            with open(path, 'r', encoding='UTF-8') as f:
                # 读取文件内容并转换为Python字典
                news_list = json.load(f)
                for news_json in news_list:
                    if contains_korean(str(news_json)) is False:
                        key = (news_json['time'], news_json['title'])
                        data[key] = news_json
    json_list = list(data.values())
    print(len(json_list))
    sorted_list = sorted(json_list, key=lambda x: x['time'], reverse=True)

    # 将字典转换为列表，然后写入新的JSON文件
    with open('output/output.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_list, f, indent=4, ensure_ascii=False)







