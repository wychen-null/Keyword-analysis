import matplotlib.pyplot as plt
from wordcloud import WordCloud
import stylecloud
import json
import csv

# 读取JSON文件
# with open('output/output_nltk1.json', 'r') as json_file:
#     data = json.load(json_file)
#
# # 创建CSV文件并写入数据
# with open('output/output_nltk1.csv', 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#
#     # 写入CSV文件的表头
#     writer.writerow(['word', 'freq'])
#
#     # 写入JSON数据
#     for item in data:
#         writer.writerow([item[0], item[1]])


stylecloud.gen_stylecloud(file_path='output/TF_IDF/output_2023_season4.csv',
                          icon_name='fas fa-shield-alt',
                          # icon_name='fas fa-bug',
                          colors='white',
                          background_color='black',
                          output_name='output/wordCloud/season4_shield.png',
                          collocations=False)

# with open('output/output_nltk.json',encoding="utf-8") as file:
#     # 读取文件内容
#     keyword_list = json.load(file)
#
#
# keyword_cloud = dict(keyword_list)
# wordcloud = WordCloud(max_font_size=74, max_words=80,
#                       width=1280, height=640,
#                       background_color="black").generate_from_frequencies(keyword_cloud)
# plt.figure(figsize=(16, 8))
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()