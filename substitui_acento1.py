tiposdeA = "ãáàâ"
tiposdeE = "èéê"
tiposdeI = "í"
tiposdeO = "ôõóò"
tipoÇ = "c"
posicao = 0
nome= ""
vogais = "aeiou"
espaço = " "
quantidade = 0

nomeusuario = input("Digite se nome completo: ")
tamanho = len(nomeusuario)

#Se o nome for inválido dar erro
if tamanho < 3:
    print("nome inválido!")

while(posicao < tamanho):
    letra = nomeusuario[posicao]
    if(tiposdeA.find(letra)>-1):
        letra = ("a")
    if(tiposdeE.find(letra)>-1):
        letra = ("e")
    if(tiposdeI.find(letra)>-1):
        letra = ("i")
    if(tiposdeO.find(letra)>-1):
        letra = ("o")
    if(tipoÇ.find(letra)>-1):
        letra = ("c")
    if vogais.find(letra) == -1:
        print("As posicoes das consoantes são:", posicao)
    if letra == espaço:
        quantidade = quantidade + 1
    nome = nome + letra    
    posicao = posicao +1
print(nome)
print("A quantidade de palavras:", quantidade +1)