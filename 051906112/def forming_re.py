
from cnradical import Radical, RunOption
from pypinyin import lazy_pinyin
import pypinyin
import zhconv
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

radical = Radical(RunOption.Radical)


def forming_re(word: str):  # 生成正则表达式
    if 'a' <= word <= 'z' or 'A' <= word <= 'Z':
        # 判断是不是中文
        english = []
        for i in word:  # 得到每个字母
            english.append(i)
        return '.{0,20}'.join(english)
    else:
        resl = []
        tyz = []
        # 同音字
        dagParams = DefaultDagParams()
        pinyin_list = lazy_pinyin(word)
        result = dag(dagParams, pinyin_list, path_num=500, log=True)
        for p in result:
            tyz.append(''.join(p.path))
        # 找出全部的同音字

        for m in range(len(word)):
            i = word[m]
            a = [i, radical.trans_ch(i)]
            # 偏旁
            # 拼音
            py = pypinyin.lazy_pinyin(i)[0]
            a.append(py)
            a.append(py[0])
            # 繁体字
            ftz = zhconv.convert(i, 'zh-tw')
            if ftz != i:
                # 判断繁体是否与原中文不同
                a.append(ftz)
            # 同音字
            for h in tyz:
                a.append(h[m])

            resl.append("(?:" + "|".join(a) + ")")
        return '.{0,20}?'.join(resl)
