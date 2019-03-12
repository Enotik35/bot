import requests
import misc
import json
from time import sleep
token = misc.token

#https://api.telegram.org/bot780872217:AAHQ4ISiXbrjlBwqKEsolFevnZah56Ffj7k/sendmessage?chat_id=778461209&text=hi
URL = 'https://api.telegram.org/bot' + token +'/'


global last_update_id
last_update_id = 0

global clas
clas = open('text.txt')
clas = '1.Абдурахманов Р.','2.Ахантьев Д.','3.Буевская А.','4.Веренченко Д.','5.Гусар А.','6.Дудко Д.','7.Гусева М.','8.Занина Е.','9.Онуфриенко М.','10.Османова Н.','11.Писаренко Д.','12.Ремзиева Э.','13.Сагайда О.','14.Синеджук С.','15.Сухоруков Д.','16.Чайковский А.'

def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()


def get_message():


	data = get_updates()

	last_id = data['result'][-1]['update_id']

	global last_update_id
	if last_update_id != last_id:
		last_update_id = last_id
		chat_id = data['result'][-1]['message']['chat']['id']
		message_text = data['result'][-1]['message']['text']

		message = {'chat_id': chat_id,
				   'text': message_text}
		return message
	return None



def send_message(chat_id,text='Wait a second, please...'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)



def main():
	global clas
	d = get_updates()

	with open('updates.json', 'w') as file:
		json.dump(d, file, indent=2, ensure_ascii=False)
	while True:
		answer = get_message()

		if answer != None:
			chat_id = answer['chat_id']
			text = answer['text']

			if 'Мой класс' in text:
				send_message(chat_id, clas)
		else:
			continue
		sleep(2)



if __name__ == '__main__':
	main()