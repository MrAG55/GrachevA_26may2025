
# Тестирование функциональности корзины | Интернет-магазин sibdar-spb.ru

Данный проект реализует тестирование **API и UI-функций корзины** интернет-магазина "Дикий Сбор" (https://www.sibdar-spb.ru/).

##  Стек технологий

- Python 3.13
- Pytest
- Selenium (UI)
- Requests (API)
- Allure (отчёты)
- WebDriverManager
- Page Object Pattern

##  Структура проекта

```
certification/
- pages/                  # Page Object классы
- cart_page.py
- tests/                  # UI и API тесты
- test_ui_cart.py
- test_api_cart.py
- utils/                  # Данные
- test_data.py
- requirements.txt        # Зависимости
- README.md               # Документация
- pytest.ini              # Маркеры pytest
- .gitignore              # Исключения для git
```

##  UI-тесты

| Тест                                     | Описание |
|------------------------------------------|----------|
| Добавление товара в корзину              | Проверяет, что товар появляется в корзине |
| Удаление товара из корзины               | Проверяет, что товар удаляется и корзина пуста |
| Изменение количества товара              | Проверяет увеличение количества и суммы |

##  API-тесты

| Тип запроса  | Описание                             |
|--------------|--------------------------------------|
| add          | Добавление товара в корзину через API |
| change       | Изменение количества товара через API |
| delete       | Удаление товара из корзины через API  |

##  Установка зависимостей

```bash
pip install -r requirements.txt
```

##  Запуск тестов

### UI:

```bash
pytest tests/test_ui_cart.py
```

### API:

```bash
pytest tests/test_api_cart.py
```

### Allure:

```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

