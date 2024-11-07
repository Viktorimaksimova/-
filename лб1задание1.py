numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
summa1 = sum(numbers[0:4])
summa2 = sum(numbers[5:])
summa = summa1+summa2
kol = len(numbers)
sr = summa/kol
numbers[numbers.index(None)] = sr
# TODO заменить значение пропущенного элемента средним арифметическим
print("Измененный список:", numbers)
