import string
val = string.ascii_letters

def count_char(text, char):
    cnt = 0
    for c in text:
        if c == char:
            cnt += 1
    return cnt

filename = 'E:\Subash\Test_file.txt'
f = open(filename, 'r')
text = f.read()

for char in val:
    perc  = 100 * count_char(text, char) / len(text)
    print ('{0} - {1}%'.format(char, round(perc, 3)))