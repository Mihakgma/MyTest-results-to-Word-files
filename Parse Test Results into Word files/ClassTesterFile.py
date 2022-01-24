from ParserModule import MyTestResultParser
from DateCheckerFile import DateChecker
from pandas import DataFrame
import os

#from VariableValuesMarks import all_variables_marks
#print(all_variables_marks['PC_name'][1])



# тестируем класс MyTestResultParser

# прерка корректности работы проверки формата файла для парсинга!!!
testObj = MyTestResultParser('ksdhfkjsdlfj.txt', 'ksdhfkjsdlfj.txt')

print(testObj.check_format()[0])
print(testObj.check_format()[1])

# проверяем класс проверки дат из строки в русском формате (ДД.ММ.ГГГГ)!!!


test_dates_lst = [
    'kdfjngkds',  # не дата
    '01.01.2000',
    '30.02.2001',
    '20.10.2021',
    '  09.10.2022  ',
    '01-7-1990',  # неправильный формат (разделители)
    '01.02.2019 13:12:00',
    '01.02.2019 13:12:60', # дата с ошибкой во времени
    '01.17.2019 03:33:60'  # дата с ошибкой в месяце
]

for date in test_dates_lst:
    if len(date.strip()) > 10:
        result_date_check = DateChecker(date_to_check=date).check_date(date_format='long')
    else:
        result_date_check = DateChecker(date_to_check=date).check_date()
    print(result_date_check)

# пробуем подгружать файл с результатами тестирования из MyTest!!!
file_full_path = r'D:\ФБУЗ_ЦГиЭКО\ТЕСТЫ_ОГВиА\MyTestSavePythonApplication\файл для парсинга\MyTestStudent_Result 19.01.2022.txt'

print(file_full_path)
testObjRealPath = MyTestResultParser(file_full_path, file_full_path)
print(testObjRealPath.check_format()[0])
print(testObjRealPath.check_format()[1])
# проверяем правильность считывания содержимого файла!!!
file_cont = testObjRealPath.read_file()
#print(file_cont)
print('\n', testObjRealPath.get_all_attributes())
# проверяем правильность считывания содержимого файла!!!
testObjRealPath.content_slicer('manual', 'Текст для разделения!!!')
#testObjRealPath.content_slicer()
# пробник слайсера
slice_results = testObjRealPath.content_slicer()
#print([elem for elem in sorted(file_cont.split(),key=len) if 'n' in elem])
#print(f'\n\nСодержимое оставшегося текста, в котором не было найдено результатов тестирования: \n{slice_results[1]}')
print(slice_results[0])
# сохраняем результаты тестирования в виде эксель-файла!
#df_temp = DataFrame(slice_results[0]).T # транспонированный ДФ!!!
df_temp = DataFrame(slice_results[0])
print(df_temp.head())
excel_filename = 'test_output_MyTestProgramSliced.xlsx'
df_temp.to_excel(excel_filename, index=False)
print(os.getcwd())
fileLstCWD = os.listdir()
if excel_filename in fileLstCWD:
    print('Указанный эксель-файл успешно сохранен в текущую рабочую директорию.')
else:

    print('Указанный эксель-файл НЕ БЫЛ СОХРАНЕН в текущую рабочую директорию!?')