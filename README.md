# testDjangoPik

Проект, в рамках тестового задания, на основе Django Rest Framework (backend) и Nuxt.js (frontend).

## Развертывание

### 1. Клонирование репозитория

```bash
git clone https://github.com/EffieSanjer/testDjangoPik.git
cd testDjangoPik
```

### 2. Настройка переменных окружения

Создайте файлы `backend/.env`, `frontend/.env`, а также файл `.env.postgres` в корне проекта по подобию файлов `.env.example` в директориях проекта.

По умолчанию создается пользователь с данными для авторизации:

```bash
email: admin@admin.ru
password: admin
```

### 3. Запуск проекта с помощью Docker

```bash
docker-compose up --build -d
```

Это запустит все необходимые контейнеры.

После успешного запуска сайт будет доступен по адресу: `http://localhost`

Остановить контейнеры:

```bash
docker-compose down
```
