# Медицинская диагностика — сайт клиники

Современный веб-сайт для компании медицинской диагностики. Реализована запись на приём, личный кабинет пациентов, админ-панель для управления услугами, врачами и записями.

## 🚀 Демо

После запуска проект доступен по адресу: `http://localhost:8000`

- Админ-панель: `http://localhost:8000/admin`
- Личный кабинет: `http://localhost:8000/accounts/profile/`

## 📋 Функционал

- **Главная страница** — описание компании, список популярных услуг, контактная информация, форма обратной связи
- **Страница "О компании"** — история, миссия, команда врачей
- **Страница услуг** — список всех услуг с фильтром по категориям, подробное описание и цена каждой услуги
- **Страница "Контакты"** — адрес, карта проезда, телефоны, email, форма обратной связи
- **Личный кабинет** — регистрация, авторизация, запись на приём с выбором врача, история записей, скачивание результатов диагностики
- **Админ-панель** — управление пользователями, услугами, врачами, записями и контентом

## 🛠 Технологии

- **Backend**: Django 6.0.6
- **База данных**: PostgreSQL 15
- **Frontend**: Bootstrap 5 (адаптивный дизайн)
- **Контейнеризация**: Docker, Docker Compose
- **Тестирование**: coverage.py (покрытие >90%)
- **Дополнительно**: AJAX для динамической подгрузки врачей при записи

## 📁 Структура проекта
```
medical\_diagnostic\_site/
├── apps/ # Все приложения Django
│ ├── accounts/ # Пользователи, регистрация, авторизация, личный кабинет
│ ├── services/ # Услуги (список, категории, цены)
│ ├── appointments/ # Запись на приём, история записей, результаты
│ ├── pages/ # Статические страницы (главная, о компании, контакты)
│ └── feedback/ # Обратная связь, сообщения
├── config/ # Настройки Django (settings, urls)
├── static/ # Статические файлы (CSS, JS, изображения)
├── media/ # Загружаемые файлы (результаты диагностики)
├── templates/ # HTML-шаблоны Bootstrap
├── fixtures/ # Начальные данные для БД (услуги, врачи)
├── .env.docker.example # Пример переменных окружения для Docker
├── docker-compose.yml # Конфигурация Docker Compose
├── Dockerfile # Docker образ для Django
├── entrypoint.sh # Скрипт запуска контейнера
├── requirements.txt # Зависимости Python
└── README.md # Документация
```

## 🐳 Установка и запуск через Docker (рекомендуемый способ)

### Предварительные требования

- Установленный [Docker Desktop](https://www.docker.com/products/docker-desktop/)

- Установленный [Git](https://git-scm.com/)

### Шаг 1. Клонирование репозитория

```
git clone https://github.com/AiboliTaurus/medical\_diagnostic\_site.git

cd medical\_diagnostic\_site
```
### Шаг 2. Настройка переменных окружения

Создайте файл .env.docker на основе примера:

```
cp .env.docker.example .env.docker
```
Отредактируйте .env.docker при необходимости (пароли, ключи).

### Шаг 3. Запуск через Docker Compose

```
docker-compose up --build
```
При первом запуске:

* Автоматически создадутся таблицы в PostgreSQL
* Применятся миграции
* Соберётся статика
* Загрузятся начальные данные (услуги, врачи)

### Шаг 4. Создание суперпользователя (администратора)

В новом терминале выполните:

```
docker-compose exec web python manage.py createsuperuser
```
### Шаг 5. Доступ к сайту

* **Сайт**: <http://localhost:8000>
* **Админ-панель**: <http://localhost:8000/admin>

## 🖥 Локальный запуск (без Docker)

### Предварительные требования

* Python 3.13+
* PostgreSQL 15+
* Установленный PostgreSQL и созданная база данных

### Шаг 1. Клонирование репозитория

```
git clone https://github.com/AiboliTaurus/medical\_diagnostic\_site.git

cd medical\_diagnostic\_site
```
### Шаг 2. Создание виртуального окружения

```
python -m venv venv
```
```
source venv/bin/activate *# Для Linux/macOS*

venv\Scripts\activate *# Для Windows*
```
### Шаг 3. Установка зависимостей

```
pip install -r requirements.txt
```
### Шаг 4. Настройка базы данных

Создайте базу данных PostgreSQL:

```
CREATE DATABASE medical\_db;

CREATE USER medical\_user WITH PASSWORD 'your\_password';

GRANT ALL PRIVILEGES ON DATABASE medical\_db TO medical\_user;
```
Создайте файл .env в корне проекта:

```
DB\_NAME=medical\_db

DB\_USER=medical\_user

DB\_PASSWORD=your\_password

DB\_HOST=localhost

DB\_PORT=5432

DEBUG=1

SECRET\_KEY=your-secret-key-here

ALLOWED\_HOSTS=localhost,127.0.0.1
```
### Шаг 5. Миграции и загрузка данных

```
python manage.py migrate

python manage.py loaddata fixtures/services.json

python manage.py loaddata fixtures/pages.json

python manage.py createsuperuser
```
### Шаг 6. Запуск сервера

```
python manage.py runserver
```
## 🧪 Запуск тестов


*Запуск всех тестов*
```
python manage.py test apps
```
*Запуск с замером покрытия*
```
coverage run --source='apps' manage.py test apps

coverage report

coverage html *# для просмотра HTML-отчёта*
```
Покрытие тестами: **93%** (выше требуемых 75%)

## 👥 Тестовые данные

После запуска через Docker автоматически загружаются:

**Услуги (5 шт):**

* МРТ головного мозга — 3500 ₽
* КТ лёгких — 2800 ₽
* Общий анализ крови — 800 ₽
* УЗИ брюшной полости — 1800 ₽
* Рентген грудной клетки — 1200 ₽

**Врачи (5 шт):**

* Александр Сергеевич Ветров (МРТ)
* Дмитрий Владимирович Крылов (КТ)
* Мария Викторовна Тихонова (Анализы)
* Анна Сергеевна Романова (УЗИ)
* Пётр Николаевич Зайцев (Рентген)

## 🔐 Учётные записи

**Суперпользователь (админ):**

* Логин: admin
* Пароль: admin123
* Админ-панель: <http://localhost:8000/admin>

**Обычный пользователь:**

* Зарегистрируйтесь через форму регистрации на сайте

**© 2026 Медицинская диагностика – сайт клиники. Все права защищены.**