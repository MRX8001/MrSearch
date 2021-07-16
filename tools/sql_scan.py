import requests

def fuzz(url, user_agent=None, proxy=None):
	injection = open('payloads.txt', 'r', encoding='UTF-8', errors='ignore').readlines()
	for payload in injection:
		request = requests.get(url + payload, headers=user_agent, proxies=proxy)
		if request.elapsed.total_seconds() > 5:
			return True
		else:
			pass
