import string

alphs = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test?')

if len(myInput) > 1:
    if myInput[0] not in alphs:
        print '''Invalid:first symbol must be alphabetic'''
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphs + nums:
                print '''Invalid:remaining symbol must be alphanumeric'''
                break
            else:
                print 'Okay as an identiffzer'