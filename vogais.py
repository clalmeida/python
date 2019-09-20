vogais = 'aeiou'
nome = input("digite o nome: ")
posicao = 0
tamanho = len(nome)
consoante = 0
cont = 0
while posicao < tamanho:
    letra = nome[posicao]
    temletra = vogais.find(letra)
    if temletra > -1:
        cont = cont+1
    posicao = posicao+1
    if temletra == -1:
        consoante = consoante+1

print("número de vogais é ", cont, " e o número de consoantes é",consoante,".","O total de letras é ", tamanho,".")