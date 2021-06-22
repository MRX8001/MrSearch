try:
	import os
	import argparse
	import random
	import pyfiglet
except ModuleNotFoundError:
	print("\033[1;31mMódulo não encontrado\033[m\n")
	os.system('python3 -m pip install -r requirements.txt')
os.system('clear')
pyfiglet.print_figlet('MRX800', '3D-ASCII')
uagents = random.choice(open('user-agents.txt', 'r', encoding='UTF-8', errors='ignore').readlines())
class MrSearch:
	def __init__(self, query, num, user_agent=uagents):
		self.query = query
		self.num = num
		self.user_agent = user_agent
	def Mrsearch(self):
		import time
		from tools import blinder
		from tools import sql_scan
		from tools import dsss
		try:
			import googlesearch
		except ModuleNotFoundError:
			print("\033[1;31mMódulo 'google' não encontrado")
			os.system('python3 -m pip install google')
		for result in googlesearch.search(query=self.query, tld='co.in', lang='pt', num=self.num, stop=self.num, pause=2):
			print(f'\n\033[1;37m-> {result}\033[m')
			sorn = str(input('Deseja fazer testes de SQLI na URL [S/N]: ')).upper()
			time.sleep(.1)
			if sorn == 'S':
				print('\033[1;34mSearching for vulns........')
				blind = blinder.blinder(result, sleep=5, ua=self.user_agent)
				scan = blind.check_injection()
				sql_scan.fuzz(url=result, user_agent=self.user_agent)
				scan_page = dsss.scan_page(url=result)
				if scan == True or scan_page == True:
					if scan == True:
						print('\033[1;4;33mO alvo possui a vuln Time-based Blind SQLI\033[m')
					elif scan_page == True:
						print('\033[1;4;33mO alvo está vulnerável a ataques de SQLI\033[m')
				else:
					pass
			else:
				pass
if __name__ == '__main__':
	try:
		parser = argparse.ArgumentParser(description='Protótipo para fazer buscas com o Google')
		parser.add_argument('--search', type=str, help='Setar o parâmetro de busca', required=True)
		parser.add_argument('--num', type=int, help='Definir a quantidade de links para buscar', required=True)
		parser.add_argument('--user-agent', type=str, help='Definir um User-Agent (Recomendado) (Padrão: Randomico)', required=False)
		args = parser.parse_args()
		busca = MrSearch(query=args.search, num=args.num, user_agent=args.user_agent)
		busca.Mrsearch()
	except KeyboardInterrupt:
		exit()
