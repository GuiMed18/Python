nome_aluno = (input("Digite seu nome: "))
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

media = (nota1 + nota2) / 2

print(f"Olá, {nome_aluno.capitalize()}! \nSua média foi de {media}!")