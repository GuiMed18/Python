inventario = []
resposta = 'S'

while resposta =="S":
    inventario.append(input("Digite um equipamento: ")) #Append adiciona o conteúdo na lista
    inventario.append(float(input("Digite o valor do produto: ")))
    inventario.append(int(input("Quantidade de caixas no estoque: ")))
    resposta = input('Digite "S" ou "N" para continuar: ').upper()

if resposta == 'N':
    for inv in inventario:
        print(inv)
