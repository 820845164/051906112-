def get_sensitivecontent(path):
    # 文本处理，将我们的文本处理为字符串
    file = open(path, 'r', encoding='UTF-8')
    sentens = []
    for line in file.readlines():
        string = line.strip()
        sentens.append(string)
    file.close()
    return sentens
