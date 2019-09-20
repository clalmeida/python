fruta = input("digite nome: ")
contador = 0
for letra in fruta:
    if letra in list("aeiou"):
        contador = contador+1
print(contador)