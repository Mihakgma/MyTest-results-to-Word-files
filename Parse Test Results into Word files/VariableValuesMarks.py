
all_variables_marks = {

    'test_time_stamp': [1, ('-'*10) + ' ', ' ' + ('-'*10)],
    'PC_name': [3, 'Имя компьютера: "', '"\nИмя пользователя компьютера'],
    'PC_username': [4, 'Имя пользователя компьютера: "', '"\nИмя пользователя (тестируемого)'],
    'student_fio': [5, 'Имя пользователя (тестируемого): "', '"\nНазвание теста'],
    'test_name': [6, 'Название теста: "', '"\nФайл с тестом:'],
    'test_file_full_path': [7, 'Файл с тестом: "', '"\nCRC Файла с тестом:'],
    'test_file_crc': [8, 'CRC Файла с тестом: "', '"\nВсего заданий в тесте:'],
    'entire_test_number': [9, 'Всего заданий в тесте: ', '.\nВыполнено заданий:'],
    'test_number_completed': [10, 'Выполнено заданий: ', '.\nИз них правильно:'],
    'test_number_correct': [11, 'Из них правильно: ', '\nИз них ошибок:'],
    'test_number_fail': [12, 'Из них ошибок: ', '\nРезультативность:'],
    'performance': [13, 'Результативность: ', '.\nИспользовано подсказок:'],
    'hints_used_num': [14, 'Использовано подсказок: ', '.\nНабрано баллов: '],
    'score_got': [15, 'Набрано баллов: ', '.\nОценка:'],
    'rate_num': [16, 'Оценка: ', '.\nМаска результата:'],
    'result_mask': [17, 'Маска результата: "', '".\nМаска времени обдумывания'],
    'time_mask': [18, 'Маска времени обдумывания (в секундах): "', '".\nМаска ответов:'],
    'answer_mask': [19, 'Маска ответов: "', '".\nМаска штрафов за подсказку:'],
    'penalty_mask': [20, 'Маска штрафов за подсказку: "', '".\nВремя начала:'],
    'start_time': [21, 'Время начала: ', '.\nВремя завершения:'],
    'end_time': [22, 'Время завершения: ', '.\nПродолжительность:'],
    'duration_time': [23, 'Продолжительность: ', '.\n'+('-'*48)]
}

if __name__ == '__main__':
    info_text = """
       Этот словарь предназначен для
       поиска границ значений извлекаемых из
       ПОЛНОЙ (ИЗНАЧАЛЬНОЙ) ВЕРСИИ текста
       с результатами тестов.
       Значение каждого ключа в словаре - список.
       Элементы списка (в соответствии с индексом):
           0) номер строки текста с результатом
           1) начальная (левая) граница искомого значения
           2) конечная (правая) граница искомого значения
    """
    print(info_text)
    print('\n', 'Содержимое самого словаря: \n')
    [print(f"Ключ: <{key}>; Значение: <{all_variables_marks[key]}>") for key in all_variables_marks]
    input()
