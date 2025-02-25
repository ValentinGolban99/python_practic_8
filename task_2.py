# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать. 
# Он захотел написать функцию, которая будет находить максимум из перечисленных чисел. 
# Функция для нахождения максимума из двух чисел у него уже есть. 
# Юра задумался: может быть, её можно использовать для нахождения максимума уже от трёх чисел?

# Помогите Юре написать программу, которая находит максимум из трёх чисел. 
# Для этого используйте только функцию нахождения максимума из двух чисел.

# По итогу в программе должны быть реализованы две функции:

# maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх); при этом она должна использовать для сравнений первую функцию maximum_of_two.
# Пример

# Введите число: 5
# Введите число: 1
# Введите число: 23
# Самое большое число: 23

def maximum_of_two(first_argument, second_argumrnt):
    result = 0
    
    if first_argument > second_argumrnt:
        result = first_argument
    elif first_argument < second_argumrnt:
        result = second_argumrnt

    return result

def maximum_of_three(first_argument, second_argumrnt):
    result = 0
    
    if first_argument > second_argumrnt:
        result = first_argument
    elif first_argument < second_argumrnt:
        result = second_argumrnt

    return result


first_number = int(input("Введите число: "))
second_number = int(input("Введите число: "))
third_number = int(input("Введите число: "))

print("Самое большое число: ", end = "")
print(maximum_of_three(maximum_of_two(first_number, second_number), third_number))
