import re


madlib = open ('C:\\Users\\Mariana Costa\\Desktop\\madlib.txt', 'w')
madlib.write ('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
madlib.close()

#Open the Madlibs File
madlib = open('C:\\Users\\Mariana Costa\\Desktop\\madLib.txt')
#Save the contents so you can modify it
content = madlib.read()
madlib.close()
check = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
#Loop to check for the words to replace
while True:
    result = check.search(content)
#end the Loop if there is nothing left to replace
    if result == None:
        break

#Get user input as soon as one is found (this if statement is just for
#grammatical correctness, and could probably be done better
    if result.group() == "ADJECTIVE" or result.group() == "ADVERB" or result.group() == "NOUN" or result.group() == "VERB":
        print("Enter an %s:" % (result.group().lower()))
    
    i = input()
#substitute the word as soon as you come across it
#then Python only needs to search for one word at once, and automatically
#knows when it's done
    content = check.sub(i, content, 1)
print(content)
#Choose how to name the file you save and then save the file

name = input("Name your file: ")
newFile = open("C:\\Users\\Mariana Costa\\Desktop\\%s.txt" % (name), "w")
#newFile = open("C:\\Users\\Mariana Costa\\Desktop\\newFile.txt", "w")
newFile.write(content)
newFile.close()

