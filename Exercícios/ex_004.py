medida = "Metros"
print(f" Conversor de {medida:=^10}")

metros = float(input("Digite o valor desejado: "))

metro_p_cm = metros * 100

metro_p_mm = metros * 1000

print(f"Convertendo {metros} metros")
print(f"{metros} metros são {metro_p_cm} centimetros")
print(f"{metros} metros são {metro_p_mm} milímetros")
