# coding:utf-8
import random
import csv


class Tedage(object):
    def __init__(self, lang=1):
        self.lang = lang
        self.name_cn_file = 'data/name_cn.csv'
        self.name_en_file = 'data/name_en.csv'
        self.email_domain_file = 'data/email_domain.csv'

    # generate a person's name
    def name(self, count=2):
        # 姓名不能小于2和大于个字
        if count < 2 or count > 4:
            return None

        name_list = []

        # 中文
        if self.lang == 1:
            with open(self.name_cn_file, 'r', encoding='utf-8') as f:
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
            idx = random.randint(0, len(name_list) - 1)

            if self.lang == 1:
                ret_name += name_list[idx][0]
            elif self.lang == 2:
                ret_name += name_list[idx][0] + ' '

        return ret_name.rstrip(' ')

    # generate a user name
    def username(self, length=5):
        name_list = []
        matched_name_list = []

        with open(self.name_en_file, 'r', encoding='utf-8') as cn:
            content = csv.reader(cn)

            for item in content:
                name_list.append(item[0])

        for item in name_list:
            if len(item) == length:
                matched_name_list.append(item)

        if len(matched_name_list) == 0:
            return None

        nn = random.sample(matched_name_list, 1)[0]
        return str(nn).lower()

    # generate email address
    def email(self, username):
        domain_list = []

        with open(self.email_domain_file, 'r', encoding='utf-8') as f:
            content = csv.reader(f)

            for item in content:
                domain_list.append(item[0])

        domain = random.sample(domain_list, 1)[0]

        return '%s@%s' % (username, domain)


if __name__ == '__main__':
    tdg = Tedage(lang=2)
    for i in range(50):
        usrname = tdg.username(length=7)
        email = tdg.email(usrname)
        print(email)
