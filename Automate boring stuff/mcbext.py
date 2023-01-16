
#! python3
# mcbext.pyw - Saves and loads pieces of text to the clipboard, and deletes keywords from the shelf.
# Usage: py.exe mcbext.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcbext.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcbext.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys
mcbextShelf = shelve.open('mcb')

# Save clipboard content.

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste() #the value of sys.argv[2] is the .past
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete' and sys.argv[2].lower() in mcbextShelf.keys():
    del  mcbextShelf[sys.argv[2]]
elif len(sys.argv) == 2 and sys.argv[1]== 'DELETEALL':
    for i in list(mcbShelf.keys()):
        del mcbShelf[i]
mcbShelf.close()
