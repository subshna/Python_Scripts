from collections import Counter

l = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
print (Counter(l))

s = 'aasdsfsdfsdhfjwemwierufsdnvas'
print (Counter(s))

sentence = 'How many times each words would show up in this sentence count and update the words'
print (Counter(sentence))

words_cnt = sentence.split()
C = Counter(words_cnt)
print (C)
print (C.most_common(2))
print (sum(C.values()))