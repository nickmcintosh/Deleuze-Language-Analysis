import re
import json

# v1_1 = open('Deleuze_First_Five_Lectures_Good_Encoding.csv', encoding='utf-8-sig').read()
# v1_2 = open('DLGE2.txt', 'w', encoding='utf-8-sig')
# v1_2.write(v1_1)


# v1_2 = open('DLGE_v1.2.txt', 'w', encoding='utf-8-sig')

# with open('twenty_lectures.txt', 'r', encoding='utf-8-sig') as v1_1:
#     with open('20_lectures_1.1.txt', 'w', encoding='utf-8-sig') as v1_2:
#         for line in v1_1:
# y = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", line)
# y = re.sub("[\(\[].*?[\)\]]", "", y)
# y = re.sub(r'\[.*?\]', '', y)
# y = y.replace('"', '')
# y = y.replace('  ', ' ')
#             v1_2.write(y)

# with open('20_lectures_1.1.txt', 'r', encoding='utf-8-sig') as v1_2:
#     lines = v1_2.readlines()
#     filtered_lines = [line for line in lines if not line.startswith("Question:") and not line.startswith("Pinhas") and not line.startswith("A woman student") and not line.startswith("A student") and not line.startswith("Another student") and not line.startswith("Georges Comtesse") and not line.startswith("Isabelle") and not line.startswith("Marek") and not line.startswith("Part") and not line.startswith(
#         "Lecture") and not line.startswith("Hidenobu") and not line.startswith("Claire") and not line.startswith("Richard") and not line.startswith("Session") and not line.startswith("Parnet") and not line.startswith("Suzuki") and not line.startswith("Kirsten") and not line.startswith("The student") and not line.startswith("Stengers") and not line.startswith("Question") and not line.startswith("A second student") and not line.startswith("The second student") and not line.startswith("PC") and not line.startswith("RP")]

# with open('20_lectures_1.3.txt', 'w', encoding='utf-8-sig') as output:
#     output = output.writelines(filtered_lines)

# with open('20_lectures_1.3.txt', 'r', encoding='utf-8-sig') as v1_2:
#     with open('20_L_1.4.txt', 'w', encoding='utf-8-sig') as v1_4:
#         for line in v1_2:
#             y = line.replace('Deleuze:', '')
#             y = y.replace('Deleuze', '')
#             y = y.replace('...', '')
#             y = y.replace('. . . ', '')
#             y = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", y)
#             y = re.sub("[\(\[].*?[\)\]]", "", y)
#             y = re.sub(r'\[.*?\]', '', y)
#             y = y.replace('"', '')
#             y = y.replace('  ', ' ')
#             v1_4.write(y)


with open('20_lectures.json', 'r') as file:
    json_data = json.load(file)

cleaned_data = [[entry for entry in sublist if entry != "Deleuze"]
                for sublist in json_data]
with open('20_lectures_1_2.json', 'w') as outfile:
    json.dump(cleaned_data, outfile, indent=4)
