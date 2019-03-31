# Данные пользователя в градусах Цельсия.
# User data in degrees Celsius.

ErrorInput = 'Keep digital data!\n\n'  # Введите цыфровое значение.

try:
    celsius = float(input('Enter degrees Celsius.\n'))  # Введите градусы цельсия.
except:
    print(ErrorInput)
