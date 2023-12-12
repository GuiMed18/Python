##Proposta: Criar um script que leia o dobro, o triplo e a raiz quadrada de um número

numero = int(input("Digite um número..:"))

dobro = numero * 2
triplo = numero * 3
raiz = numero**(1/2)

print(f"Calculando o número {numero:-^6}")
print(f"Seu dobro é {dobro}, \nSeu triplo é {triplo} \nSua Raiz é {raiz}")