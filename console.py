import pyfiglet 
import click 
import time

def colorized(t='==============================================================',c='red'):
    print(click.style(t, fg=c))
    
def refresh():
    print()
    print('Memperbarui Database..')
    print()
    print('..................\n'*10)
    print('.............\n'*10)
    print('................\n'*10)
    print('............\n'*10)


def loker_io():
        print()
        print('Loker IO . . ')
        print() 
        print('1. Update')
        print('2. Read')
        print('3. Delete')

        print()
        b = input()
        if b == '1' :
            refresh()
        colorized() 
        loker_io()


    



if __name__ == "__main__":
    loker_io()
    