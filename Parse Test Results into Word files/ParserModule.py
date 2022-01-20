import os.path

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



    # рабочие методы
    def check_file_exists(self):
        """"
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
        """"
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

    def get_all_attributes(self):
        """"
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
