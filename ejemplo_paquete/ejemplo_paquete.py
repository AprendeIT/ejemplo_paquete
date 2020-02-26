import requests
import json

def get_my_ip():
    url = 'https://api.ipify.org?format=json'
    r = requests.get(url)
    dato = json.loads(r.text)
    return dato['ip']

def main():
    print(get_my_ip())


if __name__ == "__main__":
    main()
