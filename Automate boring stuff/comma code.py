spam = ['apples', 'bananas', 'tofu', 'cats']

def pickfromlist (list):
    for item in list:
        return spam[0] + ', ' + spam[1] + ', ' + spam[2]+ ' and ' + spam[3]

print (pickfromlist(spam))


    
def pickfromlist1 (list):
    for item in list:
        return ', '.join(spam[:-1]) + ' and ' + spam[len(list)-1]

print (pickfromlist1(spam))

