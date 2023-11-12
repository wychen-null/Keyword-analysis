import json
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

#设计stopwords
print(stopwords.words('english'))
stopwords_security = ['-', 'new', '|', 'sc', 'use', 'user', 'say', 'could', '2023',
                      'also', 'used', 'using', 'one', 'may', "", "number", "said",
                      "include", "first", "include", "two", "like", "make", "via",
                      "known", "found", "would", "without", "right", "S", "Menu"]


data = []
with open('output/output.json', 'r', encoding='utf-8') as f:
    news_list = json.load(f)
    for news_json in news_list:
        text = news_json['title'] + '.' + news_json['text']
        data.append(text)

keyword_list = []
print(len(data))

for i, title in enumerate(data):

    word_list = title.split(" ")
    word_list = list(set(word_list))

    word_list_cleaned = []
    for word in word_list:
        word = word.lower()
        if word not in stopwords.words('english') and word not in stopwords_security:  # remove stopwords
            word_list_cleaned.append(word)

    for k in range(len(word_list_cleaned)):
        keyword_list.append(word_list_cleaned[k])

keyword_counter = Counter(keyword_list)
print(keyword_counter)

print('{} different keywords before merging'.format(len(keyword_counter)))

# Merge duplicates: CNNs and CNN
duplicates = []
for k in keyword_counter:
    if k + 's' in keyword_counter:
        duplicates.append(k)
for k in duplicates:
    keyword_counter[k] += keyword_counter[k + 's']
    del keyword_counter[k + 's']
print('{} different keywords after merging'.format(len(keyword_counter)))

word_dict = dict(keyword_counter)
sorted_data = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)
with open('output/output_nltk.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_data, f, indent=4, ensure_ascii=False)
# Show N most common keywords and their frequencies
# num_keyowrd = 80 #FIXME
# keywords_counter_vis = keyword_counter.most_common(num_keyowrd)
#
# plt.rcdefaults()
# fig, ax = plt.subplots(figsize=(8, 18))
#
# key = [k[0] for k in keywords_counter_vis]
# value = [k[1] for k in keywords_counter_vis]
# y_pos = np.arange(len(key))
# ax.barh(y_pos, value, align='center', color='green', ecolor='black', log=True)
# ax.set_yticks(y_pos)
# ax.set_yticklabels(key, rotation=0, fontsize=10)
# ax.invert_yaxis()
# for i, v in enumerate(value):
#     ax.text(v + 3, i + .25, str(v), color='black', fontsize=10)
# ax.set_xlabel('Frequency')
# ax.set_title('NeurIPS 2020 Submission Top {} Keywords'.format(num_keyowrd))
#
# plt.show()