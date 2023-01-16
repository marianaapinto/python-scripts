
def collatz(number):
    if number%2==0:
        number = number//2
    else:
        number = 3*number +1
    return number

my_number = int(input('Enter a number: \n'))
try:
    while my_number !=1:
        my_number = collatz(my_number)
        print (my_number)
except ValueError:
    print ('Please enter an integer.')
