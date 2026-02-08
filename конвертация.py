'''
import requests

val = {'U': "CNY", 'D': "USD", 'E': "EUR"}

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
print(data)
print (data['Valute']['CNY']['Value'])
'''

courses = {'D': 77.05, 'E': 91.05, 'U': 11.11, 'R': 1}
names = {'D': 'долларов', 'E': 'евро', 'U': 'юаней', 'R': 'рублей'}

print('конвератция валют')
print('доллар - D')
print('евро - E')
print('рубль - R')
print('юань - U')

v1 = input('Введите какую валюту вы хотите обменять: ').upper()
v2 = input('Введите на какую валюту вы хотите обменять: ').upper()
s = int(input('Какую сумму? '))

in_val = round((s * courses[v1] / courses[v2]), 2)


print(f'За {s} {names[v1]} вы получите {in_val} {names[v2]}')






