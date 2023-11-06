import re

IN_FILE = "./new_papers.md"
OUT_FILE = "./new_papers2.md"

with open(IN_FILE, 'r') as f_in:
    data = f_in.read()

name = ""
section = ""

table_of_content = ""
for line in data.split('\n'):
    added = False

    if line.startswith('## '):
        section = line[3:].rstrip()
        table_of_content += f"\n- # [[{section}|{section}]]\n"

    if '### ' in line:
        name = line[4:].rstrip()
        table_of_content += f"\t- [[{section}#{name}|{name}]]\n"

print(table_of_content)
with open(OUT_FILE, 'w') as f_out:
    print(table_of_content, file=f_out)



