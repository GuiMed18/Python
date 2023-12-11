tabuada = int(input('Digite o valor para calcular a tabuada: '))

print('Iniciando a tabuada de {}'.format(tabuada))

for valor in range(1,11,1): #Valor vale 1, enquanto valor for menor que 11, adicione 1 a valor

 print('{} X {} = '.format(tabuada,valor),str(tabuada*valor))