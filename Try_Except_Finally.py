# Try except and finally block

def ask_for_int():
    while True:
        try:
            number = int(input('Enter the Numbers to add: '))
        except NameError, Argument:
            print Argument
            continue
        else:
            print ('Number given is: ', number)
            break
        finally:
            print ('Done')

if __name__ == '__main__':
    ask_for_int()
