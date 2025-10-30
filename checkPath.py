import os
import sys
from requestsLoop import requestBundle

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
}


def iterateFile(arg):
    try:
        if(os.path.exists(arg)):
            with open(str(arg), "r") as file:
                for line in file:
                    requestBundle(line, headers)
        else:
            showUsage()
    except KeyboardInterrupt:
        print("\n[!] Execução interrompida pelo usuário.")
        sys.exit(0)