valor = float(input("Digite o valor da compra: "))
desc = valor*0.1

opc = int(input("1.Parcelado\n2.A vista"))

if opc == 1:
    print("Valor da parcela: ", (valor-desc)/3, "\nComissão: ", valor*0.05)

if opc == 2:
    print("Comissão: ", (valor-desc)*0.05)