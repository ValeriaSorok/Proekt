import re

try:
    with open('test_schedule.inc',"r",encoding = 'utf-8') as file:
        test_file = file.read()
except FileNotFoundError:
    print('Файл не найден')
    
print(test_file)
print("=======================")

def clean_schedule(file):
    del_comment = list(map((lambda x: re.sub(r'--[\w\s,()]+','',x)),file.split('\n')))
    return '\n'.join(list(filter(lambda x: x, del_comment)))

wihout_comment = clean_schedule(test_file)
