# **Кулинарная книга API**

Кулинарная книга API — это простое приложение для управления рецептами, разработанное с использованием FastAPI, SQLAlchemy и SQLite. Оно позволяет пользователям эффективно создавать, получать и управлять рецептами.
## Возможности
### Создание рецептов: 
Пользователи могут добавлять новые рецепты с деталями, такими как название, время приготовления, ингредиенты и инструкции.
### Получение рецептов: 
Пользователи могут получить список всех рецептов или конкретный рецепт по его ID.
### Счетчик просмотров: 
Каждый рецепт отслеживает количество просмотров, которое увеличивается при каждом просмотре.
## Используемые технологии
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
## Установка
Клонируйте репозиторий:
```bash
git clone https://github.com/Caroline_1707/Cookbook.git && cd Cookbook/
```
Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
```
Установите необходимые пакеты:
```bash
pip install -r requirements.txt
```
## Запуск приложения
Чтобы запустить приложение, используйте следующую команду:
```bash
uvicorn main:app --reload
```
Это запустит сервер по адресу http://127.0.0.1:8000. Вы можете получить доступ к интерактивной документации API по адресу http://127.0.0.1:8000/docs.
## Эндпоинты API
1. **Получить все рецепты**
   - URL: /recipes/
   - Метод: GET
   - Ответ: Список рецептов в формате JSON.
2. **Получить рецепт по ID**
   - URL: /recipes/{recipe_id}
   - Метод: GET
   - Ответ: Подробности указанного рецепта.
3. **Создать новый рецепт**
   - URL: /recipes/
   - Метод: POST
   - Тело запроса:
```json
{
    "title": "Название рецепта",
    "cooking_time": 30,
    "ingredients": "Ингредиент 1, Ингредиент 2",
    "instructions": "Шаг 1, Шаг 2"
}
```
   - Ответ: Подробности созданного рецепта.
## Запуск тестов
Чтобы запустить тесты для приложения, убедитесь, что у вас установлены pytest и httpx. Затем выполните:
```bash
pytest test_main.py
```
## Известные проблемы и предупреждения
Убедитесь, что вы используете совместимые версии библиотек, указанные в requirements.txt.
Обратите внимание на предупреждения об устаревании в вашей среде разработки; они могут указывать на необходимость обновления вашего кода для будущей совместимости.
