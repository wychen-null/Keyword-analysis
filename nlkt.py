import json
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter


# load stopwords
def load_stopwords():
    stopwords_security = []
    with open("other_file/glasgow_stop_words.txt", "r") as f:
        stopwords_list = f.read()
        stopwords_security.append(stopwords_list)
    with open("other_file/info_security_stopwords.txt","r") as s:
        info_security_list = s.read().split(',')
        stopwords_security.append(info_security_list)
    return stopwords_security


def load_data():
    news_data = []
    with open('output/output.json', 'r', encoding='utf-8') as file:
        news_list = json.load(file)
        for news_json in news_list:
            text = news_json['title'] + '.' + news_json['text']
            news_data.append(text)
        print("Total amount of data is " + str(len(news_data)))
    return news_data

def write_file(keyword_counter):
    word_dict = dict(keyword_counter)
    sorted_data = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    with open('output/output_nltk.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, indent=4, ensure_ascii=False)



if __name__ == "__main__":

    data = load_data()
    stopwords_security = load_stopwords()
    keyword_list = []

    for i, content in enumerate(data):
        word_list = content.split(" ")
        word_list = list(set(word_list))

        word_list_cleaned = []

        for word in word_list:
            word = word.lower()
            # remove stopwords
            if word not in stopwords.words('english') and word not in stopwords_security:
                word_list_cleaned.append(word)

        for k in range(len(word_list_cleaned)):
            keyword_list.append(word_list_cleaned[k])

    print("start nlkt process")
    keyword_counter = Counter(keyword_list)


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
    write_file(keyword_counter)

