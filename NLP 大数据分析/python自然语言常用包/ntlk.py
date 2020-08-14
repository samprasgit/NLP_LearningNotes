import nltk

# print(nltk.__version__)

# 下载基本数据
# nltk.download()
# 实现基本段落的分句
text = 'I love TZ.COM . I want to study NLP. I want to improve myself'
sens=nltk.sent_tokenize(text,language='english')
# 实现分词
words=[]
for sent in sens:
    words.append(nltk.word_tokenize(sent))
print(words)

# 词性标注
tags=[]
for token in words:
    tags.append(nltk.pos_tag(token))
print(tags)


