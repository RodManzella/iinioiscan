import myRequests as req
import sys



headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
}





def requestBundle(url, headers=headers):
    url_tratada = url.strip()
    makeRequests(url_tratada, headers)

    
    




def makeRequests(url, headers):
    print(f"Acessando: {url}")

    try:
        req.requestOperations(url, headers)
    except KeyboardInterrupt:
        print("\n[!] Execução interrompida pelo usuário.")
        sys.exit(0)

    
    
    print("============================================================\n")

