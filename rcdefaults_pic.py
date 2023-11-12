import matplotlib.pyplot as plt
import json
import numpy as np
from collections import Counter

with open('output/output_nltk.json',encoding="utf-8") as file:
    # 读取文件内容
    keyword_list = json.load(file)

keyword_counter = Counter(dict(keyword_list))
# Show N most common keywords and their frequencies
num_keyowrd = 80 #FIXME
keywords_counter_vis = keyword_counter.most_common(num_keyowrd)

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(8, 18))

key = [k[0] for k in keywords_counter_vis]
value = [k[1] for k in keywords_counter_vis]
y_pos = np.arange(len(key))
ax.barh(y_pos, value, align='center', color='green', ecolor='black', log=True)
ax.set_yticks(y_pos)
ax.set_yticklabels(key, rotation=0, fontsize=10)
ax.invert_yaxis()
for i, v in enumerate(value):
    ax.text(v + 3, i + .25, str(v), color='black', fontsize=10)
ax.set_xlabel('Frequency')
ax.set_title('NeurIPS 2020 Submission Top {} Keywords'.format(num_keyowrd))

plt.show()