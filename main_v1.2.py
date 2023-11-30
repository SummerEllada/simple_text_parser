import requests
from bs4 import BeautifulSoup

# Отправляем GET-запрос к сайту
url = "https://www.taro.lv/ru/78_dverej/door_4"
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Получаем HTML-код страницы
    html = response.content

    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Извлекаем текст из HTML-кода
    text = soup.get_text()

    # Выводим полученный текст
    print(text)
else:
    print("Ошибка при запросе к сайту")