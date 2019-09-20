cpf = input("informe cpf: ")
tamanho = len(cpf)
validos = "0123456789"
list(validos)
novos = list(validos)
print (novos)
if tamanho !=11:
    print("não tem 11 dígitos")
else:
    for posicao in range(0,11):
        numero = cpf[posicao]
        if numero in novos:
            print("digito no index " + str(posicao) + "está valido")
        else:
            print("digito no index " + str(posicao) + "está inválido")