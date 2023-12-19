import requests
import pprint

print("Calculadora de dólares")

link_api = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='12-19-2023'&$top=100&$format=json&$select=cotacaoVenda"
conecta = requests.get(link_api)
puxa_api = conecta.json()
vlr_dolar = puxa_api['value'][0]['cotacaoVenda']
vlr_carteira = float(input("Digite o valor em carteira: "))
calculo = vlr_carteira / vlr_dolar

print(f"Hoje, o dólar está {vlr_dolar:.2f}")
print(f"Você pode comprar {calculo:.2f} dólares com {vlr_carteira} Reais!")