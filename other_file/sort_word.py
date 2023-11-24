# 打开文件
file_path = "data.txt"
file = open(file_path, "r")
# 使用read()函数读取整个文件内容
content = file.read()
# 关闭文件
file.close()

# 将内容分割成单词
words = content.split()

# 根据首字母对单词进行排序
sorted_words = sorted(words, key=lambda word: word[0])
# 将排序后的单词连接成一个字符串
sorted_content = " ".join(sorted_words)
# 打开文件并写入排序后的内容
file = open(file_path, "w")
file.write(sorted_content)
# 关闭文件
file.close()