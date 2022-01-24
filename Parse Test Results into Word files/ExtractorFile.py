from VariableValuesMarks import all_variables_marks
#from DateCheckerFile import DateChecker



class ResultsExtractor():
    def __init__(self, text: str):
        self.__text = text

    def get_text(self):
        return self.__text

    # рабочие методы
    def censor_text(self):
        """
        Служит для получения цензурированного текста (без маски ответов и т.д.)
        :return: его и возвращает в виде строки
        """
        text = self.get_text()
        # 1-ая подстрока для удаления
        startFirst = 'Маска ответов'
        finishFirst = 'Время начала:'
        indexFoundStartFirst = text.find(startFirst)
        indexFoundFinishFirst = text.find(finishFirst)
        remove_substringFirst = text[indexFoundStartFirst:indexFoundFinishFirst]
        # 2-ая подстрока для удаления
        startSecond = 'Файл с тестом'
        finishSecond = 'Всего заданий в тесте'
        indexFoundStartSecond = text.find(startSecond)
        indexFoundFinishSecond = text.find(finishSecond)
        remove_substringSecond = text[indexFoundStartSecond:indexFoundFinishSecond]

        return text.replace(remove_substringFirst, '')\
                   .replace(remove_substringSecond, '')


    def parse_text(self):
        """
        парсит текст и 'распихывает' результаты
        поиска значений каждой переменной по словарю
        :return: словарь с результатами поиска

        """
        text = self.get_text()
        dict_to_fill = {
            'test_time_stamp': [],
            'PC_name': [],
            'PC_username': [],
            'student_fio': [],
            'test_name': [],
            'test_file_full_path': [],
            'test_file_crc': [],
            'entire_test_number': [],
            'test_number_completed': [],
            'test_number_correct': [],
            'test_number_fail': [],
            'performance': [],
            'hints_used_num': [],
            'score_got': [],
            'rate_num': [],
            'result_mask': [],
            'time_mask': [],
            'answer_mask': [],
            'penalty_mask': [],
            'start_time': [],
            'end_time': [],
            'duration_time': []
        }

        for var_name in dict_to_fill:
            print(all_variables_marks[var_name][1])
            start = all_variables_marks[var_name][1]
            finish = all_variables_marks[var_name][2]
            indexFoundStart = text.find(start)
            indexFoundFinish = text.find(finish)
            start_len = len(start)
            var_value = text[indexFoundStart+start_len:indexFoundFinish]
            if var_name == 'student_fio':
                var_value = var_value.upper()
            dict_to_fill[var_name].append(var_value)

        return dict_to_fill