from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'/Users/dingyi/Downloads/stanford-corenlp-4.5.5')
# 输入文本
text = "I love playing football with my friends."

# 执行句法分析
result = nlp.parse(text)

# 解析结果，提取短语和词组
phrases = []
for line in result.split('\n'):
    if line.startswith('('):
        words = line.split(' ')
        if len(words) > 1:
            phrase = words[1]
            phrases.append(phrase)

# 输出结果
for phrase in phrases:
    print(phrase)

# 关闭StanfordCoreNLP对象
nlp.close()
# # 示例文本
# text = "Natural language processing is fascinating. It involves the development of algorithms and models that allow computers to understand, interpret, and generate human-like text."
#
# # 进行句法分析
# result = nlp.annotate(text, properties={
#     'annotators': 'tokenize,ssplit,pos,parse',
#     'outputFormat': 'json'
# })
#
# # 将结果解析为 JSON 格式
# result_json = json.loads(result)
#
# # 提取短语结构
# phrases = []
# for sentence in result_json['sentences']:
#     tree = sentence['parse']
#     # 在这里你可以根据树的结构提取短语
#     phrases.append(tree)
#
# # 打印短语
# for phrase in phrases:
#     print(phrase)
#
# # 关闭 StanfordCoreNLP 服务
# nlp.close()
# import nltk
#
# nltk.download('averaged_perceptron_tagger')
# # 输入句子
# text = "A new report shows that hackers are selling access to 576 corporate networks worldwide for a total cumulative sales price of $4,000,000, fueling attacks on the enterprise.The research comes from Israeli cyber-intelligence firm KELA which published its Q3 2022 ransomware report, reflecting stable activity in the sector of initial access sales but a steep rise in the value of the offerings.Although the number of sales for network access remained about the same as in the previous two quarters, the cumulative requested price has now reached $4,000,000.Initial access brokers (IABs) are hackers who sell access to corporate networks, usually achieved through credential theft, webshells, or exploiting vulnerabilities in publicly exposed hardware.After establishing a foothold on the network, the threat actors sell this corporate access to other hackers who use it to steal valuable data, deploy ransomware, or conduct other malicious activity.The reasons IABs choose not to leverage network access vary, ranging from lacking diverse intrusion skills to preferring not to risk increased legal trouble.IABs still play a crucial role in the ransomware infection chain, even if they got sidelined last year when big ransomware gangs that operated as crime syndicates operated their own IAB departments.The average selling price of these listings was $2,800, while the median selling price reached a record figure of $1,350.KELA also saw a case of a single access being offered for purchase at the astronomical price of $3,000,000. However, this listing was not included in the Q3 '22 stats and totals due to doubts about its authenticity.The top three IABs operated a large-scale business, offering between 40 and 100 accesses for sale in Q3 2022.Based on hacking forum discussions and marketplace listing removal events, the average time to sell corporate access was just 1.6 days, while most were of RDP and VPN types.This quarter's most targeted country was the United States, accounting for 30.4% of all IAB offerings. This stat is close to the 39.1% share of ransomware attacks in Q3 targeting U.S. companies.When looking at the targeted sectors, professional services, manufacturing, and technology topped the list with 13.4%, 10.8%, and 9.4%, respectively. Again, ransomware attacks feature a similar ranking,  emphasizing the connection between the two.As initial access brokers have become an integral part of the ransomware attack chain, properly securing your network from intrusion is crucial.This includes placing remote access servers behind VPNs, restricting access to publicly exposed devices, enabling MFA, and conducting phishing training to prevent the theft of corporate credentials."
#
# # 分词
# tokens = nltk.word_tokenize(text)
#
# # 词性标注
# pos_tags = nltk.pos_tag(tokens)
#
# # 使用正则表达式定义短语的语法规则
# grammar = r"""
#     NP: {<DT|JJ|NN.*>+} # 名词短语
#     PP: {<IN><NP>} # 介词短语
#     VP: {<VB.*><NP|PP|CLAUSE>+$} # 动词短语
#     CLAUSE: {<NP><VP>} # 主语和谓语组成的子句
# """
#
# # 创建ChunkParser
# chunk_parser = nltk.RegexpParser(grammar)
#
# # 应用短语抽取规则
# result = chunk_parser.parse(pos_tags)
#
# # 遍历抽取结果，获取短语和词组
# for subtree in result.subtrees():
#     if subtree.label() in ['NP', 'PP', 'VP', 'CLAUSE']:
#         phrase = " ".join(word for word, tag in subtree.leaves())
#         print(phrase)