# count_numbers — получает число и возвращает количество цифр в числе;
# change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
# main — функция ничего не получает на вход, внутри запрашивает нужные данные от пользователя, 
# выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).

def count_numbers(argument):
    count = 0
    while argument > 0:
        count += 1
        argument = argument // 10
    return count
    
    
def change_number(argument, second_argument):

    last_digit = argument % 10
    first_digit = argument // 10 ** (second_argument - 1)
    between_digits = argument % 10 ** (second_argument - 1) // 10
    argument = last_digit * 10 ** (second_argument - 1) + between_digits * 10 + first_digit
    return argument
    
def main():
    first_n = int(input("Введите первое число: "))
    second_n = int(input("\nВведите второе число: "))

    if count_numbers(first_n) < 3:
        print("В первом числе меньше трёх цифр.")

    elif count_numbers(second_n) < 4:
        print("Во втором числе меньше четырёх цифр.")
    
    else:
        
        print('\nИзменённое первое число:', change_number(first_n, count_numbers(first_n)))
        print('Изменённое второе число:', change_number(second_n, count_numbers(second_n)))
        print('\nСумма чисел:', change_number(first_n, count_numbers(first_n)) + change_number(second_n, count_numbers(second_n)))

main()