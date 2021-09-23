#!python3
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip,sys,shelve
def shelvespace(n,*key):
    shelffile = shelve.open('mcb')
    if n == 3:
        if key[0] == 'save':
            shelffile[key[1]]=pyperclip.paste()
            print('Content in clipboard successfully saved at the entered key i.e, %s'%(key[1]))
        elif key[0] == 'delete':
            del shelffile[key[1]]
            print('Key : "%s" successfully deleted.'%(key[1]))
    elif n == 2:
        if key[0] == 'list':
            print(list(shelffile.keys()))
        elif key[0] == 'delete':
            shelffile.clear()
            print('All keys removed')
        else:
            if key[0] in shelffile.keys():
                pyperclip.copy(shelffile[key[0]])
                print('Text of entered key successfully copied on clipboard')
            else:
                print('No such key found.Sorry! Try entering another key.')
    shelffile.close()


def pyperspace():
    if len(sys.argv)<2:
        print('Please write the command line in correct format.\nFormat: "Filename <instruction(you want to perform i.e., save, list, delete key, delete all keys)>".')
        sys.exit()
            
    if len(sys.argv)==3:
        if sys.argv[1].lower() == 'save':
            shelvespace(len(sys.argv),sys.argv[1],sys.argv[2])
        elif sys.argv[1].lower() == 'delete':
            shelvespace(len(sys.argv),sys.argv[1],sys.argv[2])
            
    elif len(sys.argv)==2:
        if sys.argv[1].lower() == 'list':
            shelvespace(len(sys.argv),sys.argv[1].lower())
        elif sys.argv[1].lower() == 'delete':
            shelvespace(len(sys.argv),sys.argv[1].lower())
        else:
            shelvespace(len(sys.argv),sys.argv[1])
pyperspace()
        
        
        
