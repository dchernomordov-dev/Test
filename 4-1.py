from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - given_date
        return delta.days
    except ValueError:
        return "Помилка: Неправильний формат дати. Використовуйте РРРР-ММ-ДД."
print(f"Днів з 2020-10-09: {get_days_from_today('2020-10-09')}")
