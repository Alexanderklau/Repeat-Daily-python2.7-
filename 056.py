import random

def get_int(msg,minimun,default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimun:
                print("must be >=",minimun)
            else:
                return i
        except ValueError as err:
            print(err)
