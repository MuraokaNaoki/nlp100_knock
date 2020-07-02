import random

def Shuffle(word):
    if len(word) > 4:
        mid_str = "".join(random.sample(word[1: len(word) - 1], len(word) - 2))
        return word[0] + mid_str + word[-1]
    else:
        return word

sentense = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ans = ""
for word in sentense.split():
    ans += Shuffle(word) + " "
print(ans)