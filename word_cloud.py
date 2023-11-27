import stylecloud

def draw(input,icon,output,palette):
    stylecloud.gen_stylecloud(file_path=input,
                          icon_name=icon,
                          background_color='black',
                          palette = palette,
                          gradient = True,
                          output_name=output,
                          max_words=150,
                          collocations=False)

if __name__ == "__main__":
  palette1 = "matplotlib.Viridis_10"
  palette2 = "colorbrewer.qualitative.Paired_12"
  palette3 = "colorbrewer.diverging.RdBu_6"
  palette4 = "colorbrewer.qualitative.Set3_12"
  draw('output/TF_IDF/output_all.csv','fas fa-shield-alt','output/wordCloud/all_1.png',palette1)
  draw('output/TF_IDF/output_all.csv','fas fa-shield-alt','output/wordCloud/all_2.png',palette2)
  draw('output/TF_IDF/output_all.csv','fas fa-shield-alt','output/wordCloud/all_3.png',palette3)
  draw('output/TF_IDF/output_all.csv','fas fa-shield-alt','output/wordCloud/all_4.png',palette4)
  draw('output/TF_IDF/output_2022_season3.csv','fas fa-shield-alt','output/wordCloud/2022_season3_shield_1.png',palette1)
  draw('output/TF_IDF/output_2022_season3.csv','fas fa-shield-alt','output/wordCloud/2022_season3_shield_2.png',palette2)
  draw('output/TF_IDF/output_2022_season3.csv','fas fa-shield-alt','output/wordCloud/2022_season3_shield_3.png',palette3)
  draw('output/TF_IDF/output_2022_season3.csv','fas fa-shield-alt','output/wordCloud/2022_season3_shield_4.png',palette4)
  draw('output/TF_IDF/output_2022_season4.csv','fas fa-shield-alt','output/wordCloud/2022_season4_shield_1.png',palette1)
  draw('output/TF_IDF/output_2022_season4.csv','fas fa-shield-alt','output/wordCloud/2022_season4_shield_2.png',palette2)
  draw('output/TF_IDF/output_2022_season4.csv','fas fa-shield-alt','output/wordCloud/2022_season4_shield_3.png',palette3)
  draw('output/TF_IDF/output_2022_season4.csv','fas fa-shield-alt','output/wordCloud/2022_season4_shield_4.png',palette4)
  draw('output/TF_IDF/output_2023_season1.csv','fas fa-shield-alt','output/wordCloud/2023_season1_shield_1.png',palette1)
  draw('output/TF_IDF/output_2023_season1.csv','fas fa-shield-alt','output/wordCloud/2023_season1_shield_2.png',palette2)
  draw('output/TF_IDF/output_2023_season1.csv','fas fa-shield-alt','output/wordCloud/2023_season1_shield_3.png',palette3)
  draw('output/TF_IDF/output_2023_season1.csv','fas fa-shield-alt','output/wordCloud/2023_season1_shield_4.png',palette4)
  draw('output/TF_IDF/output_2023_season2.csv','fas fa-dragon','output/wordCloud/2023_season2_snake_1.png',palette1)
  draw('output/TF_IDF/output_2023_season2.csv','fas fa-dragon','output/wordCloud/2023_season2_snake_2.png',palette2)
  draw('output/TF_IDF/output_2023_season2.csv','fas fa-dragon','output/wordCloud/2023_season2_snake_3.png',palette3)
  draw('output/TF_IDF/output_2023_season2.csv','fas fa-dragon','output/wordCloud/2023_season2_snake_4.png',palette4)
  draw('output/TF_IDF/output_2023_season3.csv','fas fa-shield-alt','output/wordCloud/2023_season3_shield_1.png',palette1)
  draw('output/TF_IDF/output_2023_season3.csv','fas fa-shield-alt','output/wordCloud/2023_season3_shield_2.png',palette2)
  draw('output/TF_IDF/output_2023_season3.csv','fas fa-shield-alt','output/wordCloud/2023_season3_shield_3.png',palette3)
  draw('output/TF_IDF/output_2023_season3.csv','fas fa-shield-alt','output/wordCloud/2023_season3_shield_4.png',palette4)
  draw('output/TF_IDF/output_2023_season4.csv','fas fa-shield-alt','output/wordCloud/2023_season4_shield_1.png',palette1)
  draw('output/TF_IDF/output_2023_season4.csv','fas fa-shield-alt','output/wordCloud/2023_season4_shield_2.png',palette2)
  draw('output/TF_IDF/output_2023_season4.csv','fas fa-shield-alt','output/wordCloud/2023_season4_shield_3.png',palette3)
  draw('output/TF_IDF/output_2023_season4.csv','fas fa-shield-alt','output/wordCloud/2023_season4_shield_4.png',palette4)