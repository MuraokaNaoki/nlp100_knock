# -*- coding: utf-8 -*-
text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words = text.split(' ')
print(words)
list = []
for i in range(len(words)):
    list.append(len(words[i]))

print(list)