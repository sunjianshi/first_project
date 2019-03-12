



# coding = utf -8
import re
from collections import Counter
from IPython import embed
def demo1():
    with open("off.txt", "r") as fd:
        texts = fd.read()  # 将文件的内容全部读取成一个字符串
        count = Counter(re.split(r"\W+", texts))  # 以单词为分隔

    result = count.most_common(10)  # 统计最常使用的前10个
    print(result)

def demo2():
    with open("off.txt", "r") as fd:
        word_list = []  # 存放所有单词，全部小写，并去除,.!等后缀，并去除空格字符串
        word_dict = {}  # 保留{word: count}键值对
        for line in fd.readlines():
            for word in line.strip().split(" "):
                word_list.append(re.sub(r"[.|!|,]", "", word.lower()))
        word_sets = list(set(word_list))  # 确保唯一
        word_dict = {word: word_list.count(word) for word in word_sets if word}
    result = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)[:10]

    print(result)


def reverse_word(string):
    return ' '.join(string.split(' ')[::-1])

def count_extnames(files):
    file_count = Counter([x.split('.')[-1] for x in files])
    print(max(file_count, key=file_count.get))
    suffix_max = [f for f in files if max(file_count, key=file_count.get) in f]
    return suffix_max

# 统计文件出现的次数，打印出出现最多的后缀，做多数量一样都输出
def count_extnames2(files):
    L = [('.' + file_name.split('.')[-1]) for file_name in files]
    suffix_max = [x for x in set(L) if L.count(x) == max([L.count(b) for b in set(L)])]
    return suffix_max

files = ['a.txt', 'b.txt','c.jpg', 'd.jpg','f.txt','g.jpg']
word = 'I an sunjianshi'

# 列表实现栈
def text(str):
    l = str.split('/')
    path = []
    for i in l:
        if i == '.':
            pass
        elif i == '..':
            path.pop()
        else:
            path.append(i)
    print(path)
    return '/'.join(path)

str = 'a/../b/d/./cd/xx.txt'
# print(text(str))
