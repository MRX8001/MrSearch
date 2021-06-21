import requests

def fuzz(url, user_agent=None):
	injection = open('payloads.txt', 'r', encoding='UTF-8', errors='ignore').readlines()
	for payload in injection:
		request = requests.get(url + payload, headers=user_agent)
		if request.elapsed.total_seconds() > 5:
			print('\033[1;33mPágina: '+url+payload+' vulnerável\033[m')
		else:
			pass
