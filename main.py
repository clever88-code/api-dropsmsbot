import requests
import time

#токет бота drop sms
token = '67e8e9ad-9ac9-48bf-888d-f2cf9d21418b'
#номера страны, можно взять тут https://dropsms.ru/api.html
id_number = '1'
#название сервиса, можно взять тут https://dropsms.ru/api.html
service = "vk"

#делаем get запрос для получения баланса
response = requests.get(f'https://api.dropsms.ru/stubs/handler_api.php?action=getBalance&api_key={token}')

#получаем текуший баланс
balance = response.text
print(balance)

#делаем get запрос для получение номера
number = requests.get(f'https://api.dropsms.ru/stubs/handler_api.php?action=getNumber&api_key={token}&service={service}&country={id_number}')

list_number = number.text

#разделяем текст
number_client = list_number.split(':')
#делаем список из token(номер запроса для номера), номера сервиса
number_client = list(number_client)

print(number_client)


#разделяем данные, token и номера
number_token = number_client[1]
number_first = number_client[2]

print(number_token)
print(number_first)


print('подтвердите когда вы впишите номер телефона(нажмите enter)')
text = input()


#получения кода в течении 10 минут
for i in range(120):
    #делаем get запрос для получение кода
    sms_code = requests.get(f'https://api.dropsms.ru/stubs/handler_api.php?action=getStatus&api_key={token}&id=(number_token)')
    sms = sms_code.text
    print(i, 'запрос кода')
    time.sleep(5)
    if sms != "NO_ACTIVATION":
        exit()
        print('ваш код' + sms)
 



