def n_gram(text):
    return [text[i:i+2] for i in range(len(text))]

str_nlp = "I am an NLPer"

print (n_gram(str_nlp.replace(' ','')),2)