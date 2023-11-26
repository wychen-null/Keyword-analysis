import stylecloud

def draw(input,icon,output):
    stylecloud.gen_stylecloud(file_path=input,
                          icon_name=icon,
                          colors='white',
                          background_color='black',
                          output_name=output,
                          collocations=False)

if __name__ == "__main__":
    draw('output/TF_IDF/output_2022_season3.csv','fas fa-shield-alt','output/wordCloud/2022_season3_shield.png')
    draw('output/TF_IDF/output_2022_season3.csv','fas fa-bug','output/wordCloud/2022_season3.png')
    draw('output/TF_IDF/output_2022_season4.csv','fas fa-shield-alt','output/wordCloud/2022_season4_shield.png')
    draw('output/TF_IDF/output_2022_season4.csv','fas fa-bug','output/wordCloud/2022_season4.png')
    draw('output/TF_IDF/output_2023_season1.csv','fas fa-shield-alt','output/wordCloud/2023_season1_shield.png')
    draw('output/TF_IDF/output_2023_season1.csv','fas fa-bug','output/wordCloud/2023_season1.png')
    draw('output/TF_IDF/output_2023_season2.csv','fas fa-shield-alt','output/wordCloud/2023_season2_shield.png')
    draw('output/TF_IDF/output_2023_season2.csv','fas fa-bug','output/wordCloud/2023_season2.png')
    draw('output/TF_IDF/output_2023_season2.csv','fas fa-dragon','output/wordCloud/2023_season2_snake.png')
    draw('output/TF_IDF/output_2023_season3.csv','fas fa-shield-alt','output/wordCloud/2023_season3_shield.png')
    draw('output/TF_IDF/output_2023_season3.csv','fas fa-bug','output/wordCloud/2023_season3.png')
    draw('output/TF_IDF/output_2023_season4.csv','fas fa-shield-alt','output/wordCloud/2023_season4_shield.png')
    draw('output/TF_IDF/output_2023_season4.csv','fas fa-bug','output/wordCloud/2023_season4.png')
# keyword_cloud = {}
# with open('output/TF_IDF/output_2023_season2.csv', encoding="utf-8") as file:
#     # 读取文件内容
#     keyword_list = csv.reader(file)
#     for row in keyword_list:
#         keyword_cloud[row[0]] = row[1]
# for key in keyword_cloud:
#     value = float(keyword_cloud[key])
#     keyword_cloud[key] = value
# # my_mask = np.array(Image.open('OIP.jpeg'))
# # my_mask = plt.imread("OIP.jpeg")
# image = Image.open("snake.webp")
# mask = np.array(image)
# wordcloud = WordCloud(mask=mask, max_font_size=74,
#                       width=1280, height=640,
#                       background_color="white").generate_from_frequencies(keyword_cloud)
# plt.figure(figsize=(16, 8))
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()