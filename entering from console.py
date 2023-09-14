stolb = int(input("Ваедите количесто столбцов: "))
stroka = int(input("Введите количество строк: "))
values_all = []
for _ in range(stroka):
    values_all += [int(x) for x in input().split()]
print(values_all)

