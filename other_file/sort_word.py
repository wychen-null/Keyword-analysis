# 打开文件
file_path = "info_security_stopwords.txt"
with open(file_path, "r") as file:
   lines = file.readlines()

# 将每一行的内容分割成单独的词
words = [word for line in lines for word in line.split()]

# 根据首字母对词进行排序
sorted_words = sorted(words)

# 将排序后的词写回到文件中
with open(file_path, "w") as file:
   for word in sorted_words:
       file.write(word + '\n')