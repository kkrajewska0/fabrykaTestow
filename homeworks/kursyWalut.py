import requests
from datetime import datetime
import time

r = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/NOK')

def decor_date(function):
    def wrapper():
        function()
        print ('Data i godzina: ' + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        print('Czas trwania zapytania: ' + str(r.elapsed.total_seconds()))
        print('_____________________')
    return wrapper

@decor_date
def exchange_rates():
    try:
        r_dict = r.json()
        print('Kurs NOK: ' + str(r_dict.get('rates')[0].get('mid')))
    except requests.exceptions.Timeout:
        print('Spróbuj ponownie za chwilę')
    except requests.exceptions.RequestException as err04:
        print('Error: ', err04)
    except requests.exceptions.ConnectionError as err02:
        print('Error connecting: ', err02)
while True:
    exchange_rates()
    time.sleep(15)