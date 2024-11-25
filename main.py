import requests


def main():
    url_template = "https://wttr.in/{}"
    locations = ['Череповец', 'Лондон', 'SVO']
    params = {
        'M': '',
        'n': '',
        'q': '',
        'T': '',
        'lang': 'ru'
    }
    for location in locations: 
        url = url_template.format(location)
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    main()
