comp = 2 * float(input("Digite o comprimento do terreno (em M): "))
larg = 2 * float(input("Digite a largura do terreno (em M): "))
telapreco = 15
tamanho = comp + larg
vtotal = tamanho * telapreco
print("Vai precisar de ", tamanho, " M de tela. R$ ", vtotal)