import requests
from urllib.parse import urljoin


def main():
    base_url = "https://wttr.in/"
    locations = ['Череповец', 'Лондон', 'SVO']
    params = {
        'M': '',
        'n': '',
        'q': '',
        'T': '',
        'lang': 'ru'
    }
    for location in locations: 
        url = urljoin(base_url, location)
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    main()
