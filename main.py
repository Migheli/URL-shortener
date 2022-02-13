import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse


dotenv_path = 'dot.env'
load_dotenv(dotenv_path)
BITLY_TOKEN = os.getenv('BITLY_TOKEN')


def url_parser(parser_input):
    parsed_link = urlparse(parser_input)
    link = parsed_link.netloc + parsed_link.path
    return link


def is_bitlink(address_bitly, headers_token, parser_input):
    link = url_parser(parser_input)
    response = requests.get(f'{address_bitly}bitlinks/{link}', headers=headers_token)
    return response.ok


def count_clicks(address_bitly, headers_token, parser_input):
    link = url_parser(parser_input)
    response = requests.get(f'{address_bitly}bitlinks/{link}/clicks/summary', headers=headers_token)
    response.raise_for_status()
    total_clicks = response.json()['total_clicks']
    result = f'Количество кликов: {total_clicks}'
    return result


def url_shortener(address_bitly, headers_token, parser_input):
    long_url = {'long_url': parser_input}
    response = requests.post(f'{address_bitly}bitlinks', headers=headers_token, json=long_url)
    response.raise_for_status()
    bitlink = response.json()['link']
    result = f'Ваш битлинк готов: {bitlink}'
    return result


def main():
    try:
        address = 'https://api-ssl.bitly.com/v4/'
        headers = {'Authorization': f'Bearer {BITLY_TOKEN}'}
        parser = argparse.ArgumentParser()
        parser.add_argument('url')
        namespace = parser.parse_args()
        parser_input = namespace.url

        if is_bitlink(address, headers, parser_input):
            result = count_clicks(address, headers, parser_input)
        else:
            result = url_shortener(address, headers, parser_input)
        print(result)
    except requests.exceptions.HTTPError as error:
        exit(f'Случилась ошибка. Код ошибки: {error}')


if __name__ == '__main__':
    main()
