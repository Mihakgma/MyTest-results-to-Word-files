import os.path
from re import search as re_search
from ExtractorFile import ResultsExtractor
from tqdm import tqdm
from sys import getsizeof as sys_getsizeof


class MyTestResultParser():
    def __init__(self,
                 filename: str,
                 full_path: str,
                 file_exists: str = 'no'):
        """
        filename - имя txt-файла для парсинга (извлечения) данных
        :type filename: str
        """
        self.__filename = filename
        self.__full_path = full_path
        self.__file_exists = file_exists


    # задать атрибуты

    def set_filename(self, filename):
        self.__filename = filename

    def set_full_path(self, full_path):
        self.__full_path = full_path

    def set_file_exists(self, file_exists):
        self.__file_exists = file_exists

    # получить атрибуты

    def get_filename(self):
        return self.__filename

    def get_full_path(self):
        return self.__full_path

    def get_file_exists(self):
        return self.__file_exists

    def get_all_attributes(self):
        """
        Возвращает все атрибуты объекта класса MyTestResultParser
        в виде словаря, где ключом является строка с именем переменной,
        а значением - ее значение
        """
        attribute_dict = {}

        filename = self.get_filename()
        attribute_dict['filename'] = filename
        full_path = self.get_full_path()
        attribute_dict['full_path'] = full_path
        file_exists = self.get_file_exists()
        attribute_dict['file_exists'] = file_exists

        return attribute_dict



    # рабочие методы - а точнее, их конвейр...
    def check_file_exists(self):
        """
        Проверить - существует ли файл?
        Да -> 'yes'
        Нет -> 'no'
        При вызове данного метода меняется один из
        аттрибутов объекта класса!!!
        """
        full_path = self.get_full_path()
        if os.path.exists(full_path):
            file_exists = 'yes'
        else:
            file_exists = 'no'
        self.set_file_exists(file_exists)

    # проверка на правильность формата подаваемого файла
    def check_format(self, format_type: str = '.txt'):
        filename = self.get_filename()
        format_ok = False
        if filename.endswith(format_type):
            out_text: str = 'Наименование файла - OK! \n'
            out_text += f'Наименование файла для парсинга заканчивается на <{format_type}>'
            format_ok = True
        else:
            out_text: str = 'Проверьте наименование файла для парсинга! \n'
            out_text += f'Фактическое имя файла: <{filename}>'
        return out_text, format_ok

    def read_file(self):
        """
        Проверяет формат и существование файла.
        Если все ок - возвращает содержимое файла в формате строки
        """
        file_fullpath = self.get_full_path()
        format_ok = self.check_format()[1]
        # обновить аттрибут!
        self.check_file_exists()
        file_exists = self.get_file_exists()
        file_content: str = ''
        if format_ok and file_exists == 'yes':
            print('Процесс считывания файла успешно инициализирован')
            file_to_read = open(file_fullpath)
            file_content = file_to_read.read()
            file_to_read.close()
        elif not(format_ok):
            print('Неправильный формат файла!')
        elif file_exists == 'no':
            print('Полный путь к файлу - не правильный!')
            print('Проверьте путь к файлу!')
        return file_content

    def content_slicer(self, regime='auto', str_parse=''):
        """
        Данный метод 'разрезает' строку с содержимым
        файла результатов тестирования из программы My Test
        И извлекает только нужную информацию.
        Возвращает кортеж:
        1) словарь, где ключи дата и время тестирования (ДД.ММ.ГГГГ ЧЧ:ММ:СС)
        + ФИО тестируемого в виде строки.
        Значения - строки с результатом от верхней границы до нижней
        Все, что отделено черточками...
        2) остаточный текст, в котором не найден искомый шаблон
        """
        if regime == 'auto':
            file_content = self.read_file()
        elif regime == 'manual':
            file_content = str_parse[:]

        file_content = file_content.replace('выполненых', 'выполненных')

        # print(file_content)

        full_mask_end = r'\n'
        main_content_mask = r'(\-+ \d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}.' \
                            r'\-+\n.*\n.*.*\n.*.*\n.*.*\n.*.*\n.*.*\n.*.*\n.*.*' \
                            r'\n.*.*\n.*.*\n.*.*\n.*.*\n.*.*\n.*.*\n.*' \
                            r'\n.*.*\n.*.*\n.*.*\n.*.*\n.*.*\n.*.*\n.*\d{2}:\d{2}:\d{2}\.\n\-+)'
        full_mask = main_content_mask + full_mask_end

        need_search = True
        counter = 0
        results_text_dict = {}
        result_dicts_lst = []
        txt_filename_dict_size = 'results_dict_size.txt'
        txt_filename_results = 'student_results_processed.txt'

        with open(txt_filename_dict_size, 'w') as f:
            f.write('Dict physical size log!')

        with open(txt_filename_results, 'w') as f:
            f.write('Students results processed during this session log!')

        max_counter_size = 10000

        for i in tqdm(range(max_counter_size)):
            dict_size_bytes = sys_getsizeof(results_text_dict)
            with open(txt_filename_dict_size, 'a') as f:
                f.write(f'\n{dict_size_bytes}')
            counter += 1
            if counter == int(max_counter_size / 2):
                answer = input('Для прекращения процедуры введите x|X ')
                if 'x' in answer.lower().strip() or 'х' in answer.lower().strip():
                    need_search = False
            # print(len(file_content))
            # print(counter)
            m = re_search(full_mask, file_content)
            # found = ''
            try:
                found = m.group(1)
                my_extractor = ResultsExtractor(found)
                censored_text = my_extractor.censor_text()
                all_var_values = my_extractor.parse_text()
                # ключ для словаря на выход -
                # время тестирования + ФИО тестируемого!!!
                key_time = found[10:30].strip()
                # необходимо добавить проверку - является ли найденная строка датой и временем?!
                key_student_fio = all_var_values['student_fio'][0]
                full_key = key_time + '{-}' + key_student_fio
                # сохраняем в лог спарсенных результатов
                with open(txt_filename_results, 'a') as f:
                    f.write(f'\n{full_key}')
                results_text_dict[full_key] = [found, censored_text]
                # добавляем найденные значения переменных в лист (значение по текущему ключу!!!)
                [results_text_dict[full_key].append(all_var_values[key][0]) for key in all_var_values]
                file_content = file_content.replace(found, '')  # удаление из исходного НАЙДЕННОГО текста
                # размер словаря достиг максимально допустимого
                # добавляем сформированный словарь в список и обнуляем данный словарь
                if dict_size_bytes >= 4696:
                    result_dicts_lst.append(results_text_dict)
                    results_text_dict = {}
            except AttributeError:
                print('Текст по заданному шаблону - не найден!!!')
                print('Процедура поиска шаблона в тексте прекращена!')
                need_search = False
                # последняя итерация по поиску шаблона в тексте
                result_dicts_lst.append(results_text_dict)
            except:
                print(f'error on <{counter}>-th iteration occurred!')
            # print(found)
            if need_search == False:
                break
        print(all_var_values)
        print(f'Общее количество итераций составило: <{counter}>')
        return result_dicts_lst, file_content
