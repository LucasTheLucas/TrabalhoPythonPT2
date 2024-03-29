num = int(input("Digite um número entre 1000 e 9999: "))
if 999 < num < 10000:
    um = num // 1000
    dois = (num % 1000) // 100
    tres = (num % 100)  // 10
    quatro = num % 10
    print(f"{um}\n{dois}\n{tres}\n{quatro}")