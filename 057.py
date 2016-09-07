class FoundException(Exception):pass

try:
    for row,record in enumerate(table):
        for column,field in enumerate(record):
            for index,item in enumerate(field):
                if item == target:
                    raise FoundException()
except FoundException:
    print("found at ({0},{1},{2},)".format(row,column,index))
else:
    print("not found")
    