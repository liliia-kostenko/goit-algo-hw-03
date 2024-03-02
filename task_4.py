from datetime import datetime, timedelta
def get_upcoming_birthdays(users):

    today = datetime.today().date()
    congratulation_list = []

    for user in users:
            # перетворення дати народження у формат datetime
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            birthday_this_year = birthday.replace(year=today.year)
            # др вже пройшов в цьому році
            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year= birthday_this_year.year + 1)
                print(birthday_this_year)
            # якщо др прибвдає на вихідні
            if birthday_this_year.weekday() == 5:  # Субота
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Неділя                
                birthday_this_year += timedelta(days=1)
            
            days_until_birthday = (birthday_this_year - today).days

            if 0 <= days_until_birthday <= 7:
                congratulation_list.append({
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
                    })

    return congratulation_list


#приклад використання
users = [
    {"name": "1", "birthday": "1985.03.02"},
    {"name": "2", "birthday": "1985.03.01"},
    {"name": "3", "birthday": "1985.03.09"},
    {"name": "3", "birthday": "1985.01.09"},
    {"name": "Jane Smith", "birthday": "1990.03.05"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)