# Пользователь вводит два числа: N и K.
# Напишите программу, которая переворачивает каждое из введённых чисел, то есть записывает эти числа в обратном порядке.

# Пример
# Введите первое число: 102
# Введите второе число: 123
# Первое число наоборот: 201
# Второе число наоборот: 321

def flip_number(argument):
    
    result = 0
    while argument > 0:
        
        result = result * 10 + argument % 10
        argument = argument // 10
    
    return result

first_number = int(input("Введите число: "))
second_number = int(input("Введите число: "))

print("Первое число наоборот: ", flip_number(first_number))
print("Второе число наоборот: ", flip_number(second_number))