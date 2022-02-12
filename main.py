import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse


dotenv_path = 'dot.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')

    return parser


namespace = create_parser().parse_args()
PARSER_INPUT = namespace.url

BITLY_TOKEN = os.getenv('BITLY_TOKEN')


HEADERS_TOKEN = {'Authorization': f'Bearer {BITLY_TOKEN}'}
ADDRESS_BITLY = 'https://api-ssl.bitly.com/v4/'


def url_parser():
    parsed_link = urlparse(f'{PARSER_INPUT}')
    link = parsed_link.netloc + parsed_link.path
    return link


def is_bitlink():
    link = url_parser()
    response = requests.get(f'{ADDRESS_BITLY}bitlinks/{link}', headers=HEADERS_TOKEN)
    return response.ok


def count_clicks():
    link = url_parser()
    response = requests.get(f'{ADDRESS_BITLY}bitlinks/{link}/clicks/summary', headers=HEADERS_TOKEN)
    response.raise_for_status()
    total_clicks = response.json()['total_clicks']
    result = f'Количество кликов: {total_clicks}'
    return result


def url_shortener():
    long_url = {'long_url': f'{PARSER_INPUT}'}
    response = requests.post(f'{ADDRESS_BITLY}bitlinks', headers=HEADERS_TOKEN, json=long_url)
    response.raise_for_status()
    bitlink = response.json()['link']
    result = f'Ваш битлинк готов: {bitlink}'
    return result


if __name__ == '__main__':

    try:
        if is_bitlink():
            result = count_clicks()
        else:
            result = url_shortener()
        print(result)
    except requests.exceptions.HTTPError as error:
        exit(f'Случилась ошибка. Код ошибки: {error}')