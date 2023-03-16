import requests
import time

#токет бота drop sms
token = '67e8e9ad-9ac9-48bf-888d-f2cf9d21418b'
#номера стараны
id_number = '73'
#название сервиса
service = "vk"

response = requests.get(f'https://api.dropsms.ru/stubs/handler_api.php?action=getBalance&api_key={token}')

balance = response.text
print(balance)


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

#получения кода в течении 10 минут
for i in range(120):
    sms_code = requests.get(f'https://api.dropsms.ru/stubs/handler_api.php?action=getStatus&api_key={token}&id=(number_token)')
    sms = sms_code.text
    print(sms)
    time.sleep(5)
    if sms != "NO_ACTIVATION":
        exit()
        print('ваш код' + sms)
 



