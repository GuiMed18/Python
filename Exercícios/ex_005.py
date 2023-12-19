print("=====Tabuada=====")

valor = int(input("Digite o número a ser calculado: "))

multiplicadores = [1,2,3,4,5,6,7,8,9,10]

for mult in multiplicadores:
    resultado = valor * mult
    
    print(f"{valor} x {mult} = {resultado}")
