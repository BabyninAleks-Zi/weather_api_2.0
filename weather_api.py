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

    except requests.exceptions.HTTPError as http_err:
        print('HTTP ошибка: {}'.format(http_err))
        print('Код ошибки: {}'.format(response.status_code))
        print('Ответ сервера: {}'.format(response.text))


if __name__ == '__main__':
    generate_weather()
