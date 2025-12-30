# Auto Congratulate Bot

Скрипт для массовой отправки сообщений в Telegram от имени вашего аккаунта.

## Установка

```bash
pip install -r requirements.txt
```

## Настройка

1. Скопируйте `.env.example` в `.env`:
```bash
copy .env.example .env
```

2. Получите API credentials на https://my.telegram.org/apps

3. Заполните `.env` своими данными

4. Отредактируйте `messages.json` - укажите user_id и текст сообщений

## Запуск

```bash
python send_messages.py
```
ИЛИ
```bash
uv venv
```

При первом запуске введите номер телефона и код подтверждения.

## Формат messages.json

```json
[
  {
    "user_id": 123456789,
    "text": "Текст сообщения"
  }
]
```

## Отчет

После выполнения создается файл `report_YYYYMMDD_HHMMSS.json` с результатами отправки.
