nome=input('Digite um nome: ')
idade=int(input('Digite sua idade: '))
nota_matematica=float(input('Digite a nota da prova de matemática: '))
nota_fisica=float(input('Digite a nota da prova de física: '))
nota_lportuguesa = float(input('Digite a nota da prova de português: '))

soma_notas = nota_matematica + nota_fisica + nota_lportuguesa

calcula_media = soma_notas / 3 #Quantidade de matérias

print("Olá, ",nome,'! ',"sua média final foi de ",calcula_media)
print("O tipo da nota de matemática é ",type(nota_matematica))
