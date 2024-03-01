import random

list_numbers = [] # порожній список
def get_numbers_ticket(min, max, quantity):
    for i in range(min, max+1):
        list_numbers.append(i) # створюємо вибірку з переліком всіх можливих цифр із діапазону
    
    lottery_num = sorted(random.sample(list_numbers, quantity))

    return f"Ваші лотерейні числа: {lottery_num}"

# приклад використаннґ функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print(lottery_numbers)
