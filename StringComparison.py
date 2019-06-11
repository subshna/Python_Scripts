str1 = raw_input('Enter First String: ').lower()
str2 = raw_input('Enter Second String: ').lower()

if len(str1) > 25 or len(str2) > 25:
    print 'String length is more than 25'
else:
    set1 = set(str1.split())
    set2 = set(str2.split())
    if set1 == set2:
        print 'String Matched'
    else:
        print 'String Mismatch'