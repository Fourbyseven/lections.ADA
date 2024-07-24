while True:
    my_num = int(input("Введите первое число:       "))
    my_num_2 = int(input("Введите второе число:     "))
    operators = input("Введите на что хотите Сложить или вычесть:       (+, -, /, *, //, **, %)")

    if operators == '+':
        my_last_num = my_num + my_num_2
    
    elif operators == '-':
        my_last_num = my_num - my_num_2

    elif operators == '/':
        my_last_num = my_num / my_num_2

    elif operators == '*':
        my_last_num = my_num * my_num_2

    elif operators == '//':
        my_last_num = my_num // my_num_2
    
    elif operators == '**':
        my_last_num = my_num ** my_num_2

    elif operators == '%':
        my_last_num = my_num % my_num_2
        continue
    print(f"Ответ результата:       {my_last_num}")

    my_str = input("Введите хотите ли вы продолжить:        (yes, no)")
    if my_str == 'no':
        break

    