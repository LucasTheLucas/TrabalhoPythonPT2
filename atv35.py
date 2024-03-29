numero = int(input("Digite um número de 100 a 999: "))
if 99 < numero < 1000:
    um = numero // 100
    dois = (numero % 100) // 10
    tres = numero % 10
    print(f"{tres}{dois}{um}")

else:
    print("numero diferente do intervalo:")