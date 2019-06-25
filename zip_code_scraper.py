import requests
import random
from time import sleep
from bs4 import BeautifulSoup

states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New%20Hampshire','New%20Jersey','New%20Mexico','New%20York','North%20Carolina','North%20Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode%20Island','South%20Carolina','South%20Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West%20Virginia','Wisconsin','Wyoming']

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

def contains_zip_code(tag):
    return tag.name == "td" and "align" in tag.attrs and tag["align"] == "center"

zip_codes = []
for state in states:
    request = f'https://www.zipcodestogo.com/{state}/'
    html = requests.get(request, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all(contains_zip_code)
    zip_codes += list(map(lambda x: x.text, tags))
    print(f'zip_codes is now {zip_codes}')
    sleep(random.random() * 5)

with open('zip_codes', 'a') as zip_codes_file:
    for zip_code in zip_codes:
        zip_codes_file.write(zip_code)
        zip_codes_file.write('\n')
