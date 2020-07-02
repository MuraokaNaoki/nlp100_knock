def n_gram(text,n):
    return [text[i:i+n] for i in range(len(text) - n + 1)]

str_1 = "paraparaparadise"
str_2 = "paragraph"

X = set(n_gram(str_1, 2))
Y = set(n_gram(str_2, 2))



union = str(X | Y)
intersection = str(X & Y)
difference = str(X - Y)

print("X:", X)
print("Y:", Y)

print("和集合: ",union)
print("積集合: ",intersection)
print("差集合: ",difference)
print("Xにseが含まれるか: ", {('se')} <= X)
print("Yにseが含まれるか: ", {('se')} <= Y)
