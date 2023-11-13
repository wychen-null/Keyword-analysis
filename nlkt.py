import json
import nltk

from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from nltk.corpus import wordnet
from nltk import pos_tag

nltk.download('wordnet')


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


def lemmatizer_word(word_list):
    tagged_words = pos_tag(word_list)
    tagged_words = clean_by_pos(tagged_words)
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for tag in tagged_words:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmatized_words.append(lemmatizer.lemmatize(tag[0], pos=wordnet_pos))
    return lemmatized_words


# 根据词性清理词汇
def clean_by_pos(tagged_words):
    cleaned_tagged_word = []
    include_tag = ["EX", "JJ", "JJR", "JJS", "NN", "NNS", "NNP", "NNPS", "PDT", "RB", "RBR", "RBS", "UH", "VB", "VBD",
                   "VBN", "VBP", "VBZ", "NP", "PP", "VP", "ADJP", "ADVP", "PNP", "-SBJ", "-OBJ"]
    for tagged_word in tagged_words:
        if tagged_word[1] in include_tag:
            cleaned_tagged_word.append(tagged_word)
    return cleaned_tagged_word


# 获取单词的词性
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


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
    # 词形还原
    word_list = lemmatizer_word(word_list)
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
    with open('output/output_nltk1.json', 'w', encoding='utf-8') as f:
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
