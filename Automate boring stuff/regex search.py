import re, os, glob


#for file in os.listdir(os.getcwd()):
#for file in os.listdir('C:\\Users\\Mariana Costa\\Desktop'):
                       
#for file in glob.glob("*.txt"):
for file in glob.glob(os.path.join('C:\\Users\\Mariana Costa\\Desktop', '*.txt')):

    content = open (file)
    text = content.read()
    for i in text:
        check = re.compile(r'Hello|bacon|outcast|walked')
        found = check.findall(text)
    print (found)
