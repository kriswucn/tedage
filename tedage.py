# coding:utf-8
import random
import csv


class Tedage(object):
    def __init__(self, lang=1):
        self.lang = lang
        self.name_cn_file = 'data/name_cn.csv'
        self.name_en_file = 'data/name_en.csv'

    # generate a person's name
    def name(self, count=2):
        # 姓名不能小于2和大于个字
        if count < 2 or count > 4:
            return None

        name_list = []

        # 中文
        if self.lang == 1:
            with open(self.name_file, 'r', encoding='utf-8') as f:
                content = csv.reader(f)
                for item in content:
                    name_list.append(item)
        # English
        elif self.lang == 2:
            with open(self.name_en_file, 'r', encoding='utf-8') as f:
                content = csv.reader(f)
                for item in content:
                    name_list.append(item)

        # generate name
        ret_name = '';
        for i in range(count):
            idx = random.randint(0, len(name_list))

            if self.lang == 1:
                ret_name += name_list[idx][0]
            elif self.lang == 2:
                ret_name += name_list[idx][0] + ' '

        return ret_name.rstrip(' ')


if __name__ == '__main__':
    tdg = Tedage(lang=2)
    name = tdg.name(count=2)
    print(name)
