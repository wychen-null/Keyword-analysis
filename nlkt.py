import json
import nltk

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from nltk import pos_tag

# 我觉得咱们的处理逻辑应该是
# 分词 -> 词性还原 -> 合并/停用词过滤 -> 输出
# 输出的顶多是lower处理过的原词，词干还原顶多在处理的时候临时变形，但是不能输出（放在词性还原之后，停用词过滤之前）

def tokenize(text):
    token_list = nltk.word_tokenize(text)
    # tagged_words = pos_tag(token_list)
    return token_list

def stemmer_words(word):
    stemmer = PorterStemmer()
    # 对每个词进行词干还原
    stemmed_word = stemmer.stem(word)
    return stemmed_word

# def lemmatizer_word(tagged_words):
#     lemmatizer = WordNetLemmatizer()
#     lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word, _ in tagged_words]


def load_security_words():
    nltk.download('stopwords')
    stopwords_security_list = stopwords.words('english')
    with open("other_file/glasgow_stop_words.txt", "r") as f:
        stopwords_list = f.read().split('\n')
        stopwords_security_list.extend(stopwords_list)
    with open("other_file/info_security_stopwords.txt", "r") as s:
        info_security_list = s.read().split(', ')
        stopwords_security_list.extend(info_security_list)
    stopwords_security = set(stopwords_security_list)
    return stopwords_security


def remove_stopwords(stopwords_security, word_list):
    cleaned_list = []
    # 利用词干分析过滤掉停用词
    stem_stopwords = [stemmer_words(word) for word in stopwords_security]
    for word in word_list:
        if stemmer_words(word.lower()) not in stem_stopwords:
            cleaned_list.append(word)
    return cleaned_list

# load stopwords
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
    # 只输出前120个高频词
    with open('output/output_nltk.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_data[:120], f, indent=4, ensure_ascii=False)


if __name__ == "__main__":

    data = load_data()
    keyword_list = []
    stopword_list = load_security_words()

    print("start nlkt process")
    for i, content in enumerate(data):
        word_list = tokenize(content)
        word_list_cleaned = remove_stopwords(stopword_list, word_list)
        keyword_list.extend(word_list_cleaned)
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

