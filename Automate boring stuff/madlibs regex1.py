import re

file = open ('C:\\Users\\Mariana Costa\\Desktop\\madlib.txt', 'w')
file.write ('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
file.close()

file = open('C:\\Users\\Mariana Costa\\Desktop\\madlib.txt')
text = file.read()
file.close()

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

for i in regex.findall(text):
    for j in i:
        if j != '':
            reg = re.compile(r'{}'.format(j))
            inp_text = input('Enter the substitute for %s: ' %j)
            text = reg.sub(inp_text, text, 1)

print(text)

file = open('madlibs_ans.txt', 'w')
file.write(text)
file.close()
