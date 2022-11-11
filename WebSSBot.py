#!/usr/bin/env python3

try: # pip3 install httpx bs4
	from httpx import get, ReadTimeout, ConnectError
	from bs4 import BeautifulSoup
except Exception as err:
	exit(err)

from urllib.parse import urlparse
from sys import argv

if __name__ == "__main__":
	if len(argv) < 2:
		print("="*50)
		print("[ Web ScreenShot Coded By R0b327		 ]")
		print("<"+"="*48+">")
		print("[ Github: https://github.com/R0b327		 ]\n[ Facebook: https://facebook.com/R0b327		 ]")
		print("="*50)
		exit("Command Usage:\n python3 WebSS.py <URL>\n")

	URL = argv[1]
	if urlparse(URL).scheme == "":
		URL = f"http://{URL}"

	try:
		print("[*] Request sent to website...")

		UA = {
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) BC3 iOS/3.12.7 (build 538; iPhone 11 Pro Max; iOS 14.7.1)'
		}
		url = get(f"https://api.screenshotmachine.com/?key=68408d&url={URL}&device=desktop&dimension=1024x768&cacheLimit=0&delay=0", headers=UA, timeout=30)

		soup = BeautifulSoup(get(URL).text, 'html.parser')
		file_name = f"{urlparse(URL).netloc}.jpg"

		if url.status_code == 200:
			with open(file_name, "wb") as file:
				file.write(url.content)
			for title in soup.find_all('title'):
				print(f"[+] Title: {title.get_text()}")
				print(f"[+] Website: {URL}")
				print(f"[+] Time of processing: { round(url.elapsed.total_seconds(), 3)} Seconds")
				print(f"[+] Image saved: {file_name}\n")

	except ReadTimeout:
		exit("[!] Request Timeout")
	except ConnectError:
		exit("[!] Connection Error")
	except KeyboardInterrupt:
		pass
