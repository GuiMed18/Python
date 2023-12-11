nome = input('Digite seu Nome: ')
idade = int(input('Digite sua idade: '))
doador = input('Você é doador de sangue?')

if idade >= 65:
    print('Olá, {}! \n Você tem acesso à fila preferencial'.format(nome))
elif doador != 'Não' and idade >= 16:
    print('Olá, {} \n Você tem acesso à fila preferencial por ser doador de sangue'.format(nome))
else:
    print('Olá, {}! \n Você não possui acesso à fila preferencial'.format(nome))

