
import os
import re

from main import forming_re
from main import get_sensitivecontent
from main import get_sensitivewords


def main_test():
    path_1 = input("敏感词库的绝对路径：")  # 敏感词库的绝对路径
    path_2 = input("待检测文件的绝对路径：")  # 待检测文件的绝对路径
    if not os.path.exists(path_1):
        print("文件不存在")
        exit()
    if not os.path.exists(path_2):
        print("文件不存在")
        exit()
    save_path = input("输出结果的文件：")
    words = get_sensitivewords(path_1)  # 调用敏感词库函数
    contents = get_sensitivecontent(path_2)  # 调用提取待检测文本函数
    re_1 = []
    for i in words:
        re_1.append(forming_re(i))
    # 生成敏感词的所有re表达式
    answer = []
    for index in range(len(contents)):
        # 循环查找
        line = contents[index]
        index = index + 1
        for j in range(len(words)):
            re_2 = re_1[j]
            for p in re.findall(re_2, line, re.IGNORECASE):
                answer.append(f"Line{index}: <{words[j]}> {p}\n")
        file = open(save_path, 'r', encoding='UTF-8')

        file.write(f'Total: {len(answer)}\n')
        for i in answer:
            file.write(i)
        file.close()


if __name__ == '__main__':
    main_test()
