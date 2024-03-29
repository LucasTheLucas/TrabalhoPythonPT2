amigo1 = float(input("Valor da aposta do amigo 1: "))
amigo2 = float(input("Valor da aposta do amigo 2: "))
amigo3 = float(input("Valor da aposta do amigo 3: "))
apostaTotal = amigo1 + amigo2 + amigo3

valorDoPremio = float(input("Valor do premio: "))

porcao1 = valorDoPremio*(amigo1/apostaTotal)
porcao2 = valorDoPremio*(amigo2/apostaTotal)
porcao3 = valorDoPremio*(amigo3/apostaTotal)

print("O primeiro ganha: ", porcao1)
print("O segundo ganha: ", porcao2)
print("O terceiro ganha: ", porcao3)