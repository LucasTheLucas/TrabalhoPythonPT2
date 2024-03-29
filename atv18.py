G1 = float(input("Digite a primeira nota do aluno: "))
G2 = float(input("Digite a segunda nota do aluno: "))

media = (G1+(G2*2))/3

if media >= 7:
    print(f"Aluno aprovado! Media de {media}")

else:
    print(f"Aluno reprovado! Media de {media}")