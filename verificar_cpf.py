cpf = input('digite cpf: ')
validos = ("0123456789")
tamanho = len(cpf)
if tamanho != 11:
    print ('erro')
else:
    for posicao in range (0,12):
        numero = cpf[posicao]
        tacerto = validos.find(numero)
    if tacerto != -1:
        print ("erro em ", posicao)
        temero = ("sim")
print ("tem erro")