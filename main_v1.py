import scrapy


class TextSpider(scrapy.Spider):
    name = 'text_spider'
    
    start_urls = ['https://www.taro.lv/ru/78_dverej']  # Замените URL на нужный
    
    def parse(self, response):
        # Извлекаем текст с текущей страницы
        text = response.xpath('normalize-space(//body//text())').get()
        
        # Выводим текст без кода в аккуратной форме
        cleaned_text = ' '.join(text.split())
        print(cleaned_text)