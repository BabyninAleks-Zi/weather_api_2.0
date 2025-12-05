import requests


def generate_weather():
    location = input('Введите город: ')
    url = 'https://wttr.in/{}'.format(location)
    params = {
        'pnqmMT': '',
        'lang': 'ru'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.text)

    except requests.HTTPError:
        print('Вы ввели некорректное название города.')


if __name__ == '__main__':
    generate_weather()
