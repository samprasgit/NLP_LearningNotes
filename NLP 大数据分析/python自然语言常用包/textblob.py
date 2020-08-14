import textblob
text="Beautiful is better than ugly." \
     " Explicit is better than implicit. " \
     "Simple is better than complex."
# 1 利用textblob实现分句
blob=textblob.TextBlob(text)
sentences=blob.sentences
print("1分句：",sentences)
#2 根据分句实现分词
words_list=[]#声明一个list 存储所有的分词结果
for sentence in sentences:
    words_list.append(sentence.words)
    print(sentence.words)
print("2 分词：",words_list)
#3 统计单词/短语词频
counts=blob.word_counts['is']
print("3 is 出现的次数",counts)
noun_counts=blob.noun_phrases.count('Simple',case_sensitive=False)

print("4 Simple 出现的次数",noun_counts)

#4 词性标注
tags=blob.tags
print("5 词性标注",tags)

text="I think KFC is not good ."
#5 情感分析
#（1）积极/消极
#（2）主观/客观
blob=textblob.TextBlob(text)
result=blob.sentiment
print(result)
#6 机器翻译

en_text="I think KFC is not good ."
en_blob=textblob.TextBlob(en_text)

#zh_text=en_blob.translate(from_lang='en',to='zh-CN')

zh_text="美丽优于丑陋"
zh_blob=textblob.TextBlob(zh_text)
en_text=zh_blob.translate(from_lang='zh-CN',to='en')
#from_lang='en' 英语 ,to='zh-CN' 中文
print(en_text)