import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
data['Valute']['RUB']['Value'] = 1
#print (data['Valute']['RUB']['Value'])

class Currency:
    def __init__(self, data, name): 
        self.name = name
        self.data = data['Valute'][name]
      
    def convector(self, curr_2, sum):
        
        res = round((sum * self.data['Value'] / curr_2.data['Value']), 2)
        print(f'За {sum} {self.name} вы получите {res} {curr_2.name}')



print('конвератция валют')
print('доллар - USD')
print('евро - EUR')
print('юань - CNY')
print('рубль - RUB')

v1 = input('Введите какую валюту вы хотите обменять: ').upper()
v2 = input('Введите на какую валюту вы хотите обменять: ').upper()
sum = int(input('Какую сумму? '))

val_1 = Currency(data, v1)
val_2 = Currency(data, v2)

res = val_1.convector(val_2, sum)




