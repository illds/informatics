import re

file = open('thursday.xml', 'r', encoding="utf-8")
list = re.findall(r'[^\t]*', file.read())
xml = ''
for i in list:
    xml += str(i)

yaml = "---\n"
depth, i = 0, 0
data = []
while i < len(xml):
    if xml[i:i+2] == '</' or xml[i:i+2] == '/>':
        depth -= 2
    elif xml[i] == '<':
        name = ''
        i += 1
        while xml[i] != ' ' and xml[i] != '>':
            name += xml[i]
            i += 1
        if xml[i] == ' ':
            data.append([depth, name])
            depth += 1
            while xml[i] != '/' and xml[i] != '>':
                if xml[i] == ' ':
                    name = ''
                    i += 1
                    while xml[i] != ' ' and xml[i] != '=' and xml[i] != '/' and xml[i] != '>':
                        name += xml[i]
                        i += 1
                    if xml[i] == '/' or xml[i] == '>':
                        depth -= 1
                        break
                    while xml[i] != '=':
                        i += 1
                    information = ''
                    while xml[i] != '"':
                        i += 1
                    i += 1
                    while xml[i] != '"':
                        information += xml[i]
                        i += 1
                    data.append([depth, name, information])
                else:
                    i += 1
        else:
            i += 1
            information = ''
            while xml[i] != '<':
                information += xml[i]
                i += 1
            if xml[i+1]  == '/':
                i += 1
                data.append([depth, name, information])
            else:
                data.append([depth, name])
                depth += 1
    i += 1

for i in range(len(data)):
    yaml += ('  '*data[i][0])+str(data[i][1])+':'
    if len(data[i]) == 3:
        yaml += ' '+str(data[i][2])+'\n'
    else:
        yaml += '\n'

file = open('thursday.yaml', 'w')
file.write(yaml)
file.close()

