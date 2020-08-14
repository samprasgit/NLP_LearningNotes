# Task1 

## **1.0 学习资源**

[TENSORFLOW从入门到精通之——TENSORFLOW基本操作](http://www.tensorflownews.com/2018/03/28/tensorflow_base/)

[tensorflow简介 ](http://wiki.jikexueyuan.com/project/tensorflow-zh/get_started/introduction.html)

[tensorflow基本使用 ](http://wiki.jikexueyuan.com/project/tensorflowzh/get_started/basic_usage.html)

[莫凡tensorflow](https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/)

[史上最全的Tensorflow学习资源汇总]( https://zhuanlan.zhihu.com/p/35515805)

[微软周明：自然语言处理的历史与未来]( http://zhigu.news.cn/2017-06/08/c_129628590.htm)

## **1.1 数据集探索**

### 1.数据集

数据集：中、英文数据集各一份

中文数据集：THUCNews

THUCNews数据子集：https://pan.baidu.com/s/1hugrfRu 密码：qfud

英文数据集：IMDB数据集 Sentiment Analysis



### 2.IMDB数据集下载和探索

参考TensorFlow官方教程：

影评文本分类  |  TensorFlow

科赛 - Kesci.com



### 3.THUCNews数据集下载和探索

参考博客中的数据集部分和预处理部分：

CNN字符级中文文本分类-基于TensorFlow实现 - 一蓑烟雨 - CSDN博客

参考代码：text-classification-cnn-rnn/cnews_loader.py at mas...



### 4.学习召回率、准确率、ROC曲线、AUC、PR曲线这些基本概念

参考1：机器学习之类别不平衡问题 (2) —— ROC和PR曲线_慕课手记

# **Task 2**



## **2.1 文本表示：从one-hot到word2vec **

- 词袋模型：离散、高维、稀疏。
- 分布式表示：连续、低维、稠密。word2vec词向量原理并实践，用来表示文本。
- [word2vec1](https://blog.csdn.net/itplus/article/details/37969519) [word2vec2](http://www.hankcs.com/nlp/word2vec.html)

[参考答案](https://github.com/datawhalechina/Datawhale_Learning/blob/master/doc/理论应用/自然语言处理(进阶篇)/参考答案)

# **Task 3**

## **神经网络基础 **

- 前馈神经网络、网络层数、输入层、隐藏层、输出层、隐藏单元、激活函数的概念。
- 感知机相关；定义简单的几层网络（激活函数sigmoid），递归使用链式法则来实现反向传播。
- 激活函数的种类以及各自的提出背景、优缺点。（和线性模型对比，线性模型的局限性，去线性化）
- 深度学习中的正则化（参数范数惩罚：L1正则化、L2正则化；数据集增强；噪声添加；early stop；**Dropout层**）、正则化的介绍。
- 深度模型中的优化：参数初始化策略；自适应学习率算法（梯度下降、AdaGrad、RMSProp、Adam；优化算法的选择）；**batch norm层**（提出背景、解决什么问题、层在训练和测试阶段的计算公式）；layer norm层。
- FastText的原理。
- 利用FastText模型进行文本分类。
- [fasttext1](https://github.com/facebookresearch/fastText#building-fasttext-for-python) [fasttext2](https://github.com/salestock/fastText.py) [fasttext3 其中的参考](https://jepsonwong.github.io/2018/05/02/fastText/)

[参考答案](https://github.com/datawhalechina/Datawhale_Learning/blob/master/doc/理论应用/自然语言处理(进阶篇)/参考答案)

# **Task 4**

## **卷积神经网络**

- 卷积运算的定义、动机（稀疏权重、参数共享、等变表示）。一维卷积运算和二维卷积运算。
- 池化运算的定义、种类（最大池化、平均池化等）、动机。
- Text-CNN的原理。
- 利用Text-CNN模型来进行文本分类。 [参考答案](https://github.com/datawhalechina/Datawhale_Learning/blob/master/doc/理论应用/自然语言处理(进阶篇)/参考答案)

# **Task 5 **

## **循环和递归神经网络**

- RNN的结构。循环神经网络的提出背景、优缺点。着重学习RNN的反向传播、RNN出现的问题（梯度问题、长期依赖问题）、BPTT算法。
- 双向RNN
- 递归神经网络
- LSTM、GRU的结构、提出背景、优缺点。
- 针对梯度消失（LSTM等其他门控RNN）、梯度爆炸（梯度截断）的解决方案。
- Memory Network（自选）
- Text-RNN的原理。
- 利用Text-RNN模型来进行文本分类。
- Recurrent Convolutional Neural Networks（RCNN）原理。
- 利用RCNN模型来进行文本分类。

[参考答案](https://github.com/datawhalechina/Datawhale_Learning/blob/master/doc/理论应用/自然语言处理(进阶篇)/参考答案)

# **Task 6**

## **Attention原理 **

- 基本的Attention原理。
- HAN的原理（Hierarchical Attention Networks）。
- 利用Attention模型进行文本分类。

[参考答案](https://github.com/datawhalechina/Datawhale_Learning/blob/master/doc/理论应用/自然语言处理(进阶篇)/参考答案)



# **Task 7**

## **BERT**

1. Transformer的原理

2. BERT的原理

3. 利用预训练的BERT模型将句子转换为句向量，进行文本分类1

   



