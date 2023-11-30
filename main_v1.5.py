import requests
from bs4 import BeautifulSoup

# Функция для парсинга страницы и перехода по ссылкам
def parse_page(url):
    response = requests.get(url)

    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        print(text)

        # Ищем все ссылки на странице
        links = soup.find_all('a')
        for link in links:
            # Получаем атрибут href ссылки
            href = link.get('href')

            # Проверяем, что ссылка является относительной
            if href and href.startswith('/'):
                # Создаем новый URL, добавляя относительную ссылку к базовому URL
                new_url = url + href

                # Рекурсивно вызываем функцию для нового URL
                parse_page(new_url)

# Основное тело программы
url = "https://www.taro.lv/ru/78_dverej/"
parse_page(url)
