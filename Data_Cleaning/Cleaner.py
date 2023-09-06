import re

v1_1 = open('Deleuze_First_Five_Lectures_Good_Encoding.csv', encoding='utf-8-sig').read()
v1_2 = open('DLGE2.txt', 'w', encoding='utf-8-sig')
v1_2.write(v1_1)


# v1_2 = open('DLGE_v1.2.txt', 'w', encoding='utf-8-sig')


# for line in v1_1:
#   y = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", line)
#   y = re.sub("[\(\[].*?[\)\]]", "", y)
#   y = y.replace('"', '')
#   y = y.replace('  ', ' ')
#   v1_2.write(y)
