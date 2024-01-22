with open('Data_Cleaning/DLGE_v1.2.txt', 'r', encoding='utf-8-sig') as original_file:
    lines = original_file.readlines()

filtered_lines = [line for line in lines if not line.startswith(
    "Question:") and not line.startswith("Pinhas") and not line.startswith("A woman student") and not line.startswith("A student") and not line.startswith("Another student") and not line.startswith("Georges Comtesse") and not line.startswith("Isabelle") and not line.startswith("Marek") and not line.startswith("Part") and not line.startswith("Lecture") and not line.startswith("Hidenobu") and not line.startswith("Suzuki") and not line.startswith("Kirsten") and not line.startswith("The student") and not line.startswith("Stengers") and not line.startswith("Question") and not line.startswith("A second student") and not line.startswith("The second student") and not line.startswith("PC") and not line.startswith("RP")]

with open("Data_Cleaning/DLGE_v1.3.txt", 'w', encoding='utf-8-sig') as output:
    output = output.writelines(filtered_lines)
