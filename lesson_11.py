# 1. Разобраться в коде unit_test_framework.py
# 2. Напишете интерактивный калькулятор. Предполагается, что
# пользовательский ввод представляет собой формулу, состоящую из
# числа, оператора (как минимум + и -) и другого числа, разделенных
# пробелом (например, 1 + 1). Используйте str.split ()
# a. Если входные данные не состоят из 3 элементов, генерируйте эксепшн FormulaError.
# b. Попробуйте преобразовать первый и третий элемент в float ( float_value =
# float(str_value)). Поймайте любую возникающую ValueError и сгенерируйте вместо него
# FormulaError
# c. Если второй элемент не является «+» или «-», киньте эксепшн FormulaError
# 3. Напишите минимум 5 тестов для каждой созданной функции используя
# unit_test_framework.py подключенный как отдельный модуль
# 4. Пришлите ссылку на github с решением

# Для генерации исключения используется ключевое слово raise
# Пример:
# raise FormulaError('Input does not consist of three
# elements')
#
# Добавьте следующую строку в начале своего скрипта (main.py) для создания
# пользовательского исключения FormulaError
# class FormulaError(Exception): pass





class FormulaError(Exception):
    """
    'Input does not consist of 3 elements'
    """

    def init(self, message='Must be a number', *args):
        super().init(message, *args)
        pass


def parse_input(user_input):
    """
    conv. to float.
    :param user_input: str
    :return:  float, str, float
    """
    input_list = user_input.split()
    if len(input_list) != 3:
        raise FormulaError('Input does not consist of 3 elements')
    number_1, operator, number_2 = input_list
    try:
        number_1, number_2 = float(number_1), float(number_2)
    except ValueError:
        raise FormulaError()
    return number_1, operator, number_2


def summ(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number1 or number2 == 0:
        raise FormulaError(ZeroDivisionError)
    return number1 // number2


operations = {
    '+': summ,
    "-": subtraction,
    "*": multiply,
    "//": divide
}


def calculate(number1, operator, number2):
    """

    :param number1: first number
    :param operator: operator "+, - , *, //"
    :param number2: second number
    :return: res of calculate, if oper is not supported Error
    """
    operation = operations.get(operator)
    if operation:
        return operation(number1, number2)
    raise FormulaError(f'{operator} is not a valid operator!')


user_input = input("Enter what do you want to count. \nExample : 2 + 1\n>>>>>>")
number1, operator, number2 = parse_input(user_input)
result = calculate(number1, operator, number2)
print(result)
