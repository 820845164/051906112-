def get_sensitivewords(path_1):
    # 提取敏感词
    sensitiveWordList = []
    with open(path_1, "r", encoding='UTF-8') as f:
        for line in f.readlines():
            sensitiveWordList.append(line.strip())
    return sensitiveWordList
