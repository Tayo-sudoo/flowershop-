# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowershop.settings')
django.setup()

from django.contrib.auth.models import User

# Проверяем, есть ли уже admin
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('=====================')
    print('СУПЕРПОЛЬЗОВАТЕЛЬ СОЗДАН!')
    print('Логин: admin')
    print('Пароль: admin123')
    print('=====================')
else:
    print('=====================')
    print('Пользователь admin уже существует')
    print('=====================')

# Показываем всех пользователей
print('Существующие пользователи:')
for user in User.objects.all():
    if user.is_superuser:
        print(f'✅ {user.username} (админ)')
    else:
        print(f'👤 {user.username}')