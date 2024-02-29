from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')   # перетворення рядка у об'єкт datetime
        current_date = datetime.today()    # поточна дата
        dif = current_date.toordinal() - input_date.toordinal()  # різниці між поточною датою та заданою датою
        print(dif)
        return dif

    except ValueError:
        # Обробка помилок у форматі дати
        print("Формат датиповинен відповідним до формату 'РРРР-ММ-ДД'.")

# test case
input_date = "2029-03-28"  # Поточна дата для прикладу
days = get_days_from_today(input_date)
print(days)  










