num_1 = int(input("Digite o primeiro número..:"))
num_2 = int(input("Digite o segundo número..:"))
soma = num_1 + num_2
subtracao = num_1 - num_2
multiplicacao = num_1 * num_2
divisao = num_1 / num_2
potencia = num_1 ** num_2
div_inteira = num_1 // num_2
rest_divisao = num_1 % num_2
potencia_pow = pow(num_1,num_2)
raiz_num_1 = pow(num_1,(1/2))
raiz_num_2 = pow(num_2,(1/2))
raiz_cubica_1 = pow(num_1,(1/3))
raiz_cubica_2 = pow(num_2,(1/3))

# + Adição, - Subtração, * Multiplicação, / Divisão, ** Potência, // Divisão inteira, % Resto da divisão


print(f"Calculando {num_1:=^10} e {num_2:=^10}") # O termo de alinhamento < a esquerda > a direita = centralizado

print(f"O número anterior a {num_1} é {num_1-1}, seu sucessor é {num_1+1}")

print(f"O número anterior a {num_2} é {num_2-1} e seu sucessor é {num_2+1}")

print(f"A soma entre {num_1} e {num_2} é {soma}") 

print(f"A subtração entre {num_1} e {num_2} é {subtracao}")

print(f"A multiplicacao entre {num_1} e {num_2} é {multiplicacao}")

print(f"A divisão entre {num_1} e {num_2} é {divisao}")

print(f"A potencia entre {num_1} e {num_2} é {potencia}")

print(f"A divisão inteira entre {num_1} e {num_2} é {divisao}")

print(f"O resto da divisão entre {num_1} e {num_2} é {rest_divisao}")

print(f"Potencia usando power (pow()) entre {num_1} e {num_2} é {potencia_pow}")

print(f"A raiz quadrada de {num_1} é {raiz_num_1}")

print(f"A raiz quadrada de {num_2} é {raiz_num_2}")

print(f"A raiz Cúbica de {num_1} é {raiz_cubica_1}")

print(f"A raiz Cúbica de {num_2} é {raiz_cubica_2}")


      
