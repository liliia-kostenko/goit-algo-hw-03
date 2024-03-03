import random

list_numbers = [] # порожній список

def get_numbers_ticket(min, max, quantity):
    try:
        for i in range(min, max+1):
            list_numbers.append(i) # створюємо вибірку з переліком всіх можливих цифр із діапазону
            
        lottery_num = sorted(random.sample(list_numbers, quantity))

        return f"Ваші лотерейні числа: {lottery_num}"
        
    except ValueError: 
             print("Аргументи функції повинні відповидати умовам:\n1. 1 <= minimum <= maximum <= 1000\n2. quantity повинно бути більше або дорівнувати довжині відризку [minimum:maximum]\n Будь ласка, введіть коректні дані. ")

# приклад використаннґ функції
lottery_numbers = get_numbers_ticket(1, 9, 11)
print(lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 20, 5)
print(lottery_numbers)
