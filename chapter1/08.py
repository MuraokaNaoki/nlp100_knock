def cipher (sentense):
    sentenselist = []
    result = ''

    for i in range(0, len(sentense)):
        if sentense[i].islower():
            sentenselist.insert(i, chr(219-ord(sentense[i])))
        else:
            sentenselist.insert(i,sentense[i])
    
    for ii in range(0, len(sentense)):
        result += sentenselist[ii]

    return result
    
message = "My name is Naoki Muraoka"
message = cipher(message)
print("暗号化: ", message)
message = cipher(message)
print("複合化: ", message)
