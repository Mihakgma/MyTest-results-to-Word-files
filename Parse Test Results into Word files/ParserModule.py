
class MyTestResultParser():
    def __init__(self,
                 filename: str):
        """
        filename - имя txt-файла для парсинга (извлечения) данных
        :type filename: str
        """
        self.__filename = filename


    # задать атрибуты

    def set_filename(self, filename):
        self.__filename = filename

    # получить атрибуты

    def get_filename(self):
        return self.__filename

    # проверка на правильность формата подаваемого файла
    def check_format(self, format_type: str = '.txt'):
        filename = self.get_filename()
        format_ok = False
        if filename.endswith(format_type):
            out_text: str = 'OK! \n'
            out_text += f'Наименование файла для парсинга заканчивается на <{format_type}>'
            format_ok = True
        else:
            out_text: str = 'Проверьте наименование файла для парсинга! \n'
            out_text += f'Фактическое имя файла: <{filename}>'
        return out_text, format_ok

    def get_all_attributes(self):
        """"
        Возвращает все атрибуты объекта класса MyTestResultParser
        в виде словаря, где ключом является строка с именем переменной,
        а значением - ее значение
        """
        attribute_dict = {}
        filename = self.get_filename()
        attribute_dict['filename'] = filename
        return attribute_dict
