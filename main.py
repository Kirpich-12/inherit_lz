#Kirpich aka Deros. All rights reserved.
#======================================


from dr import left, right


def main():
    usr_inp = input('1 or 2')
    if usr_inp == 1:
        left()
    elif usr_inp == 2:
        right()

if __name__ == '__main__':
    main()