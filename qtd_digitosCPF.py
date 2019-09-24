cpf = input("informe CPF: ")
tamanho = len(cpf)
validos = "0123456789"
if tamanho != 11:
    print("erro na quantidade de dígitos")
else: 
    for posicao in range(0,11):
        numero = cpf[posicao]
        tacerto = validos.find(numero)
        if tacerto == -1:
            print ("dígito com erro na posição ", posicao+1)
        else:
            print("dígito válido")
