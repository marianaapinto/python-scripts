import time
import webbrowser

print ("This program started on "+time.ctime ())

def take_break ():
    for i in range (1,4):
        time.sleep(10)
        webbrowser.open("https://www.youtube.com/watch?v=PWgvGjAhvIw")
    
take_break ()
