x, y = int(input()), int(input())
a1 = x + y
a2 = x - y
a3 = x * y
a4 = x / y
a5 = x // y
result = [a1, a2, a3, a4, a5]
res1 = a1
res2 = 0

if a2 >= res1:
    res2 = res1
    res1 = a2
    if a3 >= res1:
        res2 = res1
        res1 = a3
        if a4 >= res1:
            res2 = res1
            res1 = a4
            if a5 >= res1:
                res2 = res1
                res1 = a5
        elif a5 >= res1:
            res2 = res1
            res1 = a5
    elif a4 >= res1:
        res2 = res1
        res1 = a4
        if a5 >= res1:
            res2 = res1
            res1 = a5
elif a3 >= res1:
    res2 = res1
    res1 = a3
    if a4 >= res1:
        res2 = res1
        res1 = a4
        if a5 >= res1:
            res2 = res1
            res1 = a5

print(f'Максимум: {res1}, второй максимум: {res2}')
print(f'Список чисел для удобства проверки: {result}')
