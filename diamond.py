asterisco = "xxxxxxxxxx"
espaco = "         "
num_aster = -1
num_branco = 5
for n in range(9):
    if n < 5:
        num_branco = num_branco-1
        num_aster = num_aster+2
    else:
        num_branco = num_branco+1
        num_aster = num_aster-2
    print(espaco[0:num_branco]+asterisco[0:num_aster])