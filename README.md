## Запуск проекта

### 1. Клонирование репозитория
Склонируйте проект из репозитория:
```bash
git clone https://github.com/Aftenius/glossary_project.git
cd glossary_project
```

### 2. Сборка и запуск контейнеров
```
docker-compose up --build
```

### 3. Проверка работы приложения
```
http://localhost:8000/docs
```

### 4. Управление миграциями
```
docker-compose run app alembic upgrade head
```

# Проверка состояния базы данных
```
docker exec -it glossary_project-db-1 psql -U user -d glossary
```# glossary_project