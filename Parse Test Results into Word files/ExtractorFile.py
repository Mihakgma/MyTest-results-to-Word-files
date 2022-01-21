from DateCheckerFile import DateChecker



class ResultsExtractor():
    def __init__(self, text: str):
        self.__text = text

    def get_text(self):
        return self.__text

    # рабочие методы
    def censor_text(self, start: str, finish: str):
        """
        Служит для получения цензурированного текста (без маски ответов)
        :return: его и возвращает в виде строки
        """
        text = self.get_text()
        indexFoundStart = text.find(start)
        indexFoundFinish = text.find(finish)
        remove_sustring = text[indexFoundStart:indexFoundFinish]
        return text.replace(remove_sustring, '')


    def parse_text(self):
        """
        парсит текст и 'распихывает' результаты поиска по словарю
        :return: словарь с результами

        """
        text = self.get_text()
        dict_out = {
            'PC_name': '',
            'PC_username': '',
            'student_fio': '',
            'test_name': '',
            'file_full_path': '',
            'file_crc': '',
            'entire_test_number': 0,
            'test_number_completed': 0,
            'test_number_correct': 0,
            'test_number_fail': 0,
            'performance': '',
            'hints_used_num': 0,
            'score_got': '',
            'score_num': 0,
            'result_mask': '',
            'time_mask': '',
            'answer_mask': '',
            'penalty_mask': '',
            'start_time': '',
            'end_time': '',
            'duration_time': ''
        }
        return dict_out