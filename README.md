# 🌸 Цветочный Рай — Деплой на Railway

## 🚀 Быстрый деплой (5 минут)

### 1. Загрузите код на GitHub
1. Создайте новый репозиторий на [github.com](https://github.com/new)
2. Загрузите все файлы из этой папки в репозиторий

### 2. Задеплойте на Railway
1. Зайдите на [railway.app](https://railway.app) → **New Project**
2. Выберите **Deploy from GitHub repo**
3. Выберите ваш репозиторий
4. Railway автоматически найдёт `railway.toml` и задеплоит

### 3. Получите публичный адрес
1. В Railway: **Settings → Networking → Generate Domain**
2. Нажмите **Generate** — получите ссылку вида `ваш-проект.up.railway.app`
3. Эту ссылку можно отправлять кому угодно 🎉

---

## ⚙️ Переменные среды (Variables)

В Railway: **Variables → Add Variable**

| Переменная | Значение | Обязательно |
|---|---|---|
| `SECRET_KEY` | случайная строка 50+ символов | ✅ |
| `TELEGRAM_BOT_TOKEN` | токен от @BotFather | если нужен TG вход |
| `TELEGRAM_BOT_USERNAME` | имя бота без @ | если нужен TG вход |
| `ANTHROPIC_API_KEY` | sk-ant-... | для умного AI |

**Сгенерировать SECRET_KEY:**
```
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

---

## 🔑 Создать администратора

После деплоя в Railway: **Deploy → Railway Shell**
```bash
python manage.py createsuperuser
```

---

## 📝 Добавить цветы в каталог

1. Войдите на `/admin/` как superuser
2. Добавьте категории: Розы, Тюльпаны, Букеты...
3. Добавьте цветы с фото и ценами

Или используйте скрипт тестовых данных:
```bash
python manage.py create_test_data
```

---

## ❓ Частые вопросы

**Сайт открывается, но нет CSS/картинок?**
→ В Railway: добавьте переменную `DEBUG=False` и передеплойте

**Ошибка CSRF при входе?**
→ Добавьте переменную `SITE_URL=https://ваш-домен.up.railway.app`

**Фото цветов не отображаются?**
→ Railway сбрасывает файлы при каждом деплое. Загружайте фото через `/admin/` после деплоя.
