import inspect
import lesson_11

if __name__ == '__main__':



    def get_parametr(param_name):
        assert param_name != "test_name" or "param_name" != "test_line"
        if param_name == "test_name":
            return lambda: str(inspect.stack()[2][3])
        elif param_name == "test_line":
            return lambda: str(inspect.stack()[2][2])


    def ExpectEcual(actual, expected):
        line_number = get_parametr("test_line")
        test_name = get_parametr("test_name")
        message = test_name() + f"(line:{line_number()})-\t"
        if actual == expected:
            message += "SUCCESS"
        else:
            message += f"FAILED: actual: {actual}, expected: {expected}"
        print(message)


    def test_my_summ():
        ExpectEcual(lesson_11.summ(5, 5), 10)
        ExpectEcual(lesson_11.summ(-1, 2), 1)
        ExpectEcual(lesson_11.summ(0, 0), 0)
        ExpectEcual(lesson_11.summ(120, 80), 200)
        ExpectEcual(lesson_11.summ(-8, -20), -28)


    def test_my_subtraction():
        ExpectEcual(lesson_11.subtraction(5, 5), 0)
        ExpectEcual(lesson_11.subtraction(-1, 2), -3)
        ExpectEcual(lesson_11.subtraction(0, 0), 0)
        ExpectEcual(lesson_11.subtraction(120, 80), 40)
        ExpectEcual(lesson_11.subtraction(-8, -20), 12)


    def test_my_multiply():
        ExpectEcual(lesson_11.multiply(5, 5), 25)
        ExpectEcual(lesson_11.multiply(-1, 2), -2)
        ExpectEcual(lesson_11.multiply(0, 0), 0)
        ExpectEcual(lesson_11.multiply(120, 80), 9600)
        ExpectEcual(lesson_11.multiply(-8, -20), 160)


    def test_my_divide():
        ExpectEcual(lesson_11.divide(5, 5), 1)
        ExpectEcual(lesson_11.divide(-1, 2), -1)
        ExpectEcual(lesson_11.divide(1, 1), 1)
        ExpectEcual(lesson_11.divide(120, 80), 1)
        ExpectEcual(lesson_11.divide(-8, -20), 0)


    test_my_summ()
    test_my_subtraction()
    test_my_multiply()
    test_my_divide()
