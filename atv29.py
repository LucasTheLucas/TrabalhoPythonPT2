dias = int(input("Quantos dias o encanador trabalhou? "))
diaria = 30
bruto = dias*diaria
inss = bruto*0.11
ir = bruto*0.08
liquido = bruto - inss - ir
print("O salario liquido desse encanador é de: ", liquido)