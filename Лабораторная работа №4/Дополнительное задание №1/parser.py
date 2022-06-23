import xmltodict

with open('thursday.xml', encoding="utf-8") as xml_data:
    xml_parsed = xmltodict.parse(xml_data.read())

def pars(cur_depth, list, yaml):
    for j in list:
        if len(str(j)) != len(j):
            for jj in j:
                if jj[0] == '@':
                    yaml += ('\n'+'  '*cur_depth+str(jj[1:])+':')
                else:
                    yaml += ('\n'+'  '*cur_depth+str(jj)+':')
                yaml = pars(cur_depth+1, j[jj], yaml)
            continue
        try:
            list[j]
        except TypeError:
            yaml += ('  '+str(list))
            break
        
        if j[0] == '@':
            yaml += ('\n'+'  '*cur_depth+str(j[1:])+':')
        else:
            yaml += ('\n'+'  '*cur_depth+str(j)+':')
        yaml = pars(cur_depth+1, list[j], yaml)
    return yaml
yaml = pars(0, xml_parsed, '---')

file = open('thursday.yaml', 'w')
file.write(yaml)
file.close()
