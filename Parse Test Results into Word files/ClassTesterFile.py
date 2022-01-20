# тестируем класс MyTestResultParser
from ParserModule import MyTestResultParser


# прерка корректности работы проверки формата файла для парсинга!!!
testObj = MyTestResultParser('ksdhfkjsdlfj.txt')

print(testObj.check_format()[0])
print(testObj.check_format()[1])

# проверяем класс проверки дат из строки в русском формате (ДД.ММ.ГГГГ)!!!
from DateCheckerFile import DateChecker

test_dates_lst = [
    'kdfjngkds',
    '01.01.2000',
    '30.02.2001',
    '20.10.2021',
    '  09.10.2022  ',
    '01-7-1990'
]

for date in test_dates_lst:
    result_date_check = DateChecker(date_to_check=date).check_date()
    print(result_date_check)

# пробуем подгружать файл с результатами тестирования из MyTest!!!
file_full_path = r'D:\ФБУЗ_ЦГиЭКО\ТЕСТЫ_ОГВиА\MyTestSavePythonApplication\файл для парсинга\MyTestStudent_Result 19.01.2022.txt'
