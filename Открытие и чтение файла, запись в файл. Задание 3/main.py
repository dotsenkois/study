from pathlib import *
import os

current_dir = Path.cwd()

count_dict = {}
for file in os.listdir(current_dir):
    if file.endswith(".txt"):
        with open(file, 'r' , encoding = 'UTF8') as f:
            quantity = len(f.readlines())
            count_dict.setdefault(f.name, quantity)

sorterd_cd_temp = sorted(count_dict.items(), key=lambda x: x[1])
sorterd_cd = {k: v for k, v in sorterd_cd_temp}

result_file = open('result.cfg', 'w')
for k, v in sorterd_cd.items():
    result_file.write(k + '\n')
    result_file.write(str(v) + '\n')
    with open(k, 'r', encoding='UTF8') as f:
        result_file.write(f.read() + '\n')