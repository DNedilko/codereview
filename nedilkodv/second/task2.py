'''
Скільки цифр у заданій стрічці
'''

text="dsfibfy1223hj4jh546j6k69hgjf9fh5nj50"
n=0
check=["0", "1","2", "3", "4","5","6", "7","8", "9"]
for index in range(0, len(text)):
    for numb in check:
        if text[index] == numb:
            n=n+1
print(n)