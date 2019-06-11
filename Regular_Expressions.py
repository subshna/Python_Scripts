import re

patterns = ['term1', 'term2']
text = 'This sentence contains term1 but not the other term'

for pattern in patterns:
    print ('Searching the string --> {}'.format(pattern))
    if re.search(pattern, text):
        print ('Match Found')
    else:
        print ('No Match found')

# Different objects with re
match = re.search(patterns[0], text)
print (match.start())
print (match.end())
print (match.string)

# Using split with regular expression
split_term = '@'
phrase = 'What is your email id, is it helloworld@gmail.com'
print (re.split(split_term, phrase))


# Find the pattern using re pattern syntax
def multi_re_exp(patterns, text):
    for pat in patterns:
        print ('Searching the phrase using re check {}'.format(pat))
        print (re.findall(pat, text))

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_parttern = ['sd*',     # s followed by zero or more d's
                 'sd+',     # s followed by one or more d's
                 'sd?',     # s followed by zero or more d's
                 'sd{2}',   # s followed by two d's
                 'sd{2,3}', # s followed by 2 or 2 d's
                 ]
multi_re_exp(test_parttern, test_phrase)