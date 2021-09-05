# Salario brasilero traduzido para outras moedas pelo mundo 
import requests
import json
import pandas

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacoes_dolar = cotacoes['USDBRL']["bid"]
cotacoes_euro = cotacoes['EURBRL']["bid"]
cotacoes_bitcoin = cotacoes['BTCBRL']["bid"]

salario = int(input("Seu salario em R$: "))

salario_dolar = salario / float(cotacoes_dolar)
salario_euro = salario / float(cotacoes_euro)
salario_bitcoin = salario / float(cotacoes_bitcoin)

print(f'O seu salario e:{salario}')
print(f'Salario em dolar: {salario_dolar}')
print(f'Salario em euro: {salario_euro}')
print(f'Salario em bitcoin: {salario_bitcoin}')