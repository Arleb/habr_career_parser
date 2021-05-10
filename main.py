import requests
from bs4 import BeautifulSoup
import csv


def main():
    vacs = []
    page_count = int(input("How many pages do you need to parse?:").strip())

    for page in range(1, page_count + 1):
        print(f'page {page}...')
        params = {'p': page}

        url = 'https://career.habr.com'
        result = requests.get('https://career.habr.com/vacancies?page=%s', params=params)
        result_page = result.text
        soup = BeautifulSoup(result_page, 'html.parser')

        vacancy_card = soup.find_all('div', class_='vacancy-card__info')

        for card in vacancy_card:
            vacancy_name = card.find('div', class_='vacancy-card__title').get_text()
            link = url + card.find('div', class_='vacancy-card__title').find('a').get('href')
            city = card.find('span', class_='preserve-line').get_text()
            salary = card.find('div', class_='basic-salary').get_text()
            company_name = card.find('a', class_='link-comp link-comp--appearance-dark').get_text()

            vacs.append([vacancy_name, company_name, city, salary, link])


    with open('vacancies.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for card in vacs:
            writer.writerow(card)


if __name__ == '__main__':
    main()