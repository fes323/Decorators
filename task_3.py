import os
import types
#from pprint import pprint
from datetime import datetime

def logger(old_function):
  foo_start_time = datetime.now().strftime("%Y-%m-%d %H:%M")
  if os.path.exists('log_task_3.log'):
      os.remove('log_task_3.log')
  def new_function(list_of_lists):
      print(f'Вызов функции: {old_function.__name__}')

      result_logger = old_function(list_of_lists)

      print(f'result: {result_logger}')

      with open('log_task_3.log', 'a', encoding='utf-8') as f:
        f.write(f'Дата запуска функции: {foo_start_time}\n'
                f'Название функции: {str(old_function.__name__)}.\n'
                f'Переданный тип: {result_logger}\n\n')
        f.close()
      return result_logger

  return new_function

@logger
def flat_generator(list_of_lists):
    for _list in list_of_lists:
        for item in _list:
            yield item

def test():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        #pprint(flat_iterator_item)
        #pprint(check_item)
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test()
