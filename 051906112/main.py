
import re
import os
import sys
from cnradical import Radical, RunOption
from pypinyin import lazy_pinyin
import pypinyin
import zhconv
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

radical = Radical(RunOption.Radical)


def get_sensitivewords(path_1):
    sensitiveWordList = []
    with open(path_1, "r", encoding='UTF-8') as f:
        for line in f.readlines():
            sensitiveWordList.append(line.strip())
    return sensitiveWordList


def get_sensitivecontent(path):
    # 文本处理，将我们的文本处理为字符串，并且过滤掉标点符号
    file = open(path, 'r', encoding='UTF-8')
    sentens = []
    for line in file.readlines():
        string = line.strip()
        # 调用标点符号过滤函数
        sentens.append(string)
    file.close()
    return sentens


def forming_re(word: str):
    # 构建正则表达式
    if 'a' <= word <= 'z' or 'A' <= word <= 'Z':
        # 判断是不是英文
        english = []
        for i in word:  # 得到每个字母
            english.append(i)
        return '.{0,20}'.join(english)
    else:
        resl = []
        tyz = []
        # 判断是否同音字
        dagParams = DefaultDagParams()
        pinyin_list = lazy_pinyin(word)
        result = dag(dagParams, pinyin_list, path_num=500, log=True)
        for p in result:
            tyz.append(''.join(p.path))
        # 找出全部的同音字

        for m in range(len(word)):
            i = word[m]
            a = [i, radical.trans_ch(i)]
            # 进行偏旁的处理
            # 拼音
            py = pypinyin.lazy_pinyin(i)[0]
            a.append(py)
            a.append(py[0])
            # 进行繁体字与简体字的处理
            ftz = zhconv.convert(i, 'zh-tw')
            if ftz != i:
                # 判断繁体是否与原中文不同
                a.append(ftz)
            # 同音字
            for h in tyz:
                a.append(h[m])

            resl.append("(?:" + "|".join(a) + ")")
        return '.{0,20}?'.join(resl)


def main_test():
    path_1 = str(sys.argv[1])  # 敏感词库的绝对路径
    path_2 = str(sys.argv[2])  # 待检测文件的绝对路径
    if not os.path.exists(path_1):
        print("文件不存在")
        exit()
    if not os.path.exists(path_2):
        print("文件不存在")
        exit()
    save_path = str(sys.argv[3])  # 输出结果的文件
    words = get_sensitivewords(path_1)
    contents = get_sensitivecontent(path_2)
    re_1 = []
    for i in words:
        re_1.append(forming_re(i))
    # 生成敏感词的所有re表达式
    answer = []
    for index in range(len(contents)):
        # 开始循环print()所有的敏感词
        line = contents[index]
        index = index + 1
        for j in range(len(words)):
            re_2 = re_1[j]
            for p in re.findall(re_2, line, re.IGNORECASE):
                answer.append(f"Line{index}: <{words[j]}> {p}\n")
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(f'Total: {len(answer)}\n')
            for i in answer:
                f.write(i)
            f.close()

def test(path_1, path_2):
    if not os.path.exists(path_1):
        print("文件不存在")
        exit()
    if not os.path.exists(path_2):
        print("文件不存在")
        exit()
    words = get_sensitivewords(path_1)
    contents = get_sensitivecontent(path_2)
    re_1 = []
    for i in words:
        re_1.append(forming_re(i))
    # 生成敏感词的所有re表达式
    answer = []
    for index in range(len(contents)):
        # 开始循环print()所有的敏感词
        line = contents[index]
        index = index + 1
        for j in range(len(words)):
            re_2 = re_1[j]
            for p in re.findall(re_2, line, re.IGNORECASE):
                answer.append(f"Line{index}: <{words[j]}> {p}")
    print(answer)
    return answer

if __name__ == '__main__':
    main_test()
