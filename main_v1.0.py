import requests
from bs4 import BeautifulSoup

# Отправляем GET-запрос к сайту
url = "https://www.taro.lv/ru/78_dverej/"
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Получаем HTML-код страницы
    html = response.content

    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Находим все текстовые элементы на странице
    text_elements = soup.find_all(text=True)

    # Извлекаем текст из элементов
    text = ' '.join([element.strip() for element in text_elements])

    # Выводим полученный текст
    print(text)
else:
    print("Ошибка при запросе к сайту")
