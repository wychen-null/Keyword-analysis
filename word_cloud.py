import matplotlib.pyplot as plt
import json
from wordcloud import WordCloud

with open('output/output_nltk.json',encoding="utf-8") as file:
    # 读取文件内容
    keyword_list = json.load(file)


keyword_cloud = dict(keyword_list)
wordcloud = WordCloud(max_font_size=74, max_words=80,
                      width=1280, height=640,
                      background_color="black").generate_from_frequencies(keyword_cloud)
plt.figure(figsize=(16, 8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()