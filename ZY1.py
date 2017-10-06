
import string
import re #正则表达处理模块
from collections import Counter
import nltk
from zhon.hanzi import punctuation

#文本存放路径，要改为你本地存储路径
file_path = "D:\\projects\\deep learning\\happiness_seg.txt"

with open(file_path, encoding='utf-8') as f:
    #读取文本内容
    buf = f.read() 
    #通过正则表达过滤文本中的特殊字符
    filterBuf = re.sub("[%s%s\n\s]+" % (punctuation, string.punctuation), " ", buf)
    #使用ntlk处理文本进行分词
    words = nltk.wordpunct_tokenize(filterBuf)
    #生成二元词组
    wordsList = nltk.bigrams(words)
    wordsList
    #计算二元词组频率
    counter = Counter(wordsList).most_common(10)
    for a in counter:
        print("%s出现的频率是：%s" % (a[0], a[1]))
    
    f.close()





