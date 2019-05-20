import re
example="hello world this is 2019"
print(re.findall("\w\w",example))
print(re.findall("\w(\w)",example))
print(re.findall("(\w)\w",example))
print(re.findall("(\w)(\w)",example))

'''
['he', 'll', 'wo', 'rl', 'th', 'is', 'is', '20', '19']
['e', 'l', 'o', 'l', 'h', 's', 's', '0', '9']
['h', 'l', 'w', 'r', 't', 'i', 'i', '2', '1']
[('h', 'e'), ('l', 'l'), ('w', 'o'), ('r', 'l'), ('t', 'h'), ('i', 's'), ('i', 's'), ('2', '0'), ('1', '9')]
'''


print(re.findall(".*",example))
print(re.findall(".*?",example))
print(re.findall(".*",example))
'''
re.M 每一行当作一个新的字符

'''