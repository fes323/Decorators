import os
from datetime import datetime

def logger(old_function):

    def new_function(*args, **kwargs):
        print(f'args: {args}, kwargs: {kwargs}')
        print(f'Вызов функции: {old_function.__name__}')

        result_logger = old_function(*args, **kwargs)

        print(f'result: {result_logger}')

        path = 'main.log'

        if os.path.exists(path):
            with open('main.log', 'a+', encoding='utf-8') as f:
                f.write(str(f'Функция: {old_function.__name__} Аргументы: {args} or/and {kwargs}\n'))
                f.write(str(f'Результат: {result_logger}\n\n'))
                f.close()
        else:
            with open('main.log', 'w+', encoding='utf-8') as f:
                f.write(str(f'дата лога: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n\n'))
                f.write(str(f'функция: {old_function.__name__} Аргументы: {args} or/and {kwargs}\n'))
                f.write(str(f'Результат: {result_logger}\n\n'))
                f.close()
        return result_logger

    return new_function


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def summator(a, b=0):
        return a + b

    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()