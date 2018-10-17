names = []
with open('data/name.cn', 'r', encoding='utf-8') as f:
    line = f.read()

    for i in range(len(line)):
        names.append(line[i])

    print(names)

with open('data/name1.cn', 'w', encoding='utf-8') as ff:
    for name in names:
        ff.writelines(name + ',\n')
