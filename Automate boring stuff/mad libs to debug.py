#! python3
# mad libs.py - Reads in text fles and lets the user add
#their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
#appears in the text fle. 

import sys

madlib = open ('C:\\Users\\Mariana Costa\\Desktop\\madlib.txt', 'w')
madlib.write ('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
madlib.close()


madlib = open ('C:\\Users\\Mariana Costa\\Desktop\\madlib.txt', 'r')
newmadlib = madlib.read()
madlib.close()
print (newmadlib)

adjective = input('Enter an adjective: ')
noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
noun2 = input('Enter a noun: ')


madlibreplaced = open ('C:\\Users\\Mariana Costa\\Desktop\\madlibreplaced.txt', 'w')
madlibreplaced.write = newmadlib.replace('ADJECTIVE', adjective) and newmadlib.replace('NOUN', noun) and newmadlib.replace('VERB', verb) and newmadlib.replace('NOUN', noun2) 

madlibreplaced.close()



newmadlib = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

syntax = {'ADJECTIVE': input('Enter an adjective: '),
       'NOUN': input('Enter a noun: '),
       'VERB': input('Enter a verb: '),
        'NOUN': input('Enter a noun: ')}
#def replace_all(text, dic):
    for i, j in dic.items():
        text.replace(i, j)
    print (text)
replace_all(newmadlib,syntax)
