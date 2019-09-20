vogais = "aeiou"
nome = input("insira nome: ")
cont = 0
tamanho = len(nome)
posicao = 0
while posicao < tamanho:
    letra = nome[posicao]
    temletra = vogais.find(letra)
    if temletra > -1:
        cont = cont+1
    posicao = posicao+1
print(cont)