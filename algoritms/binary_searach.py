def binary_search(arr, target):
    start = 0
    end = len(arr) -1

    while start <= end:
        middle = (start + end) // 2
        
        # Проверка 1: Если искомое число находиться в середине массива 

        if arr[middle] == target:
            return middle
        
        # Проверка 2: Если число в середине больше цели искомого числа ишем в левой половине

        elif arr[middle] > target:
            end = middle -1

        # Проверка 3: Если число в середине меньше  цели искомого числа ишем в правой половине
        else:
            start  = middle + 1
    # Если искомое число не найдено 
    return -1

array = [i for i in range(1, 1001)]
target = 999

res = binary_search(array, target)
if res != -1 :
    print(f'Элеммент найден н индекск {res}')

else:
    print("Элеммент не найден")



comparisins = 1
for i in range(1, 1001):
    if i == target:
        print(f'Элеммент {i} Найден под индексом {i -1}')
print(comparisins)










