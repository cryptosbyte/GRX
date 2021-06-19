from lib.system import system
from lib.sleep import sleep
from colorama import Fore
from lib.requests import request
from lib.monitors import languages

def main():
	try:
		while True:

			gists = request.get_all_gists()

			for gist in gists:

				for file in gist["files"]:

					raw_url = gist["files"][file]["raw_url"]

					print(f"{Fore.YELLOW}{system.terminal_width()*'='}")
					print(f"${Fore.GREEN}[X] Hounding{Fore.MAGENTA} {file}")

					_res = request.get(raw_url)

					print(f"{Fore.YELLOW}${Fore.RED}[X]{Fore.MAGENTA} SENDING REQUEST TO \"{raw_url}\"")

					if str(file).endswith(".js"):
						languages.javascript(file)

					print(Fore.RESET)
			
			sleep._sleep(60.0)
			clear()

	except KeyboardInterrupt:


		exit(0)

if __name__:

	main()