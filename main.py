import argparse
import re
import json


from tqdm import tqdm


class Validator:
    """
    Класс Validator используется для валидации данных

    Attributes:
    __telephone: номер телефона
    __weight: рост
    __snils: номер СНИЛС
    __passport_number: номер паспорта
    __occupation: вид занятости
    __age: возраст
    __political_views: политические взгляды
    __worldview: мировозрение
    __address: адрес
    """
    __telephone: str
    __weight: int
    __snils: str
    __passport_number: str
    __occupation: str
    __age: int
    __political_views: str
    __worldview: str
    __address: str
    __occupation_invalid = []
    __political_views_invalid = []
    __worldview_invalid = []

    # инициализация экземпляра класса Validator, параметры - объекты класса
    def __init__(self, telephone: str, weight: int, snils: str, passport_number: str, age: int, occupation: str,
                 political_views: str, worldview: str, address: str):
        self.__telephone = telephone
        self.__weight = weight
        self.__snils = snils
        self.__passport_number = passport_number
        self.__occupation = occupation
        self.__age = age
        self.__political_views = political_views
        self.__worldview = worldview
        self.__address = address

    def check_telephone(self) -> bool:
        """
        Проверка номера телефона

        Если номер телефона соответсвует валидному значению: +?-(???)-???-??-??,
        то возвращает True, иначе False
        ^/& -> start/end str ; \d -> any number ; \+ -> + ; \( \) -> ( ) ;

        :return: bool
        Результат проверки в булевом типе данных
        """
        if re.match(r"^\+(\d)-\((\d{3})\)-(\d{3})-(\d{2})-(\d{2})$", self.__telephone) is not None:
            return True
        return False

    def check_weight(self) -> bool:
        """
        Проверка веса

        Если вес в диапозоне [40, 120], то возвращает True, иначе False

        :return: bool
        Результат проверки в булевом типе данных
        """
        if re.match(r"^\d{2}$", str(self.__age)) is not None and (int(self.__weight) > 40) and (int(self.__weight) < 120):
            return True
        return False
    print("check1")
    def check_snils(self) -> bool:
        """
        Проверка номера СНИЛС

        Если состоит из 11 цифр, то возвращает True, иначе False

        :return: bool
        Результат проверки в булевом типе данных
        """
        if re.match(r"^\d{11}$", self.__snils) is not None:
            return True
        return False

    def check_passport_number(self) -> bool:
        """
        Проверка номера паспорта

        Если состоит из 6 цифр, то возвращает True, иначе False

        :return: bool
        Результат проверки в булевом типе данных
        """
        if re.match(r"^\d{6}$", str(self.__passport_number)) is not None:
            return True
        return False

    def check_occupation(self) -> bool:
        """
        Проверка вида занятости

        Если строка состоит только из букв [А-Я][A-Z] без цифр и не в невалидных значениях,
        то возвращает True, иначе False

        :return: bool
        Результат проверки в булевом типе данных
        """
        if re.match(r"^([A-Z]|[А-Я])[\D]+$", str(self.__occupation)) is not None and self.__occupation not in \
                self.__occupation_invalid:
            return True
        return False

    def check_age(self) -> bool:
        """
        Проверка возраста

        Если возраст в диапозоне [0, 100], то возвращает True, иначе False

        :return: bool
        Результат проверки в булевом типе данных
        """
        if re.match(r"^\d{2}$", str(self.__age)) is not None and (int(self.__age) < 0) and (int(self.__age) > 100):
            return True
        return False

    def check_political_views(self) -> bool:
        """
        Проверка валидности политического взгяда

        Если не содержит цифр  и не в невалидных значениях, то возвращает True, иначе False
        \D -> любой символ кроме цифры ; + -> неограниченное количество повторов

        :return: bool
        Результат проверки в булевом типе данных
        """
        if re.match(r"^[\D]+$", self.__political_views) is not None and self.__political_views not in \
                self.__political_views_invalid:
            return True
        return False

    def check_worldview(self) -> bool:
        """
        Проверка валидности мировозрения

        Если не содержит цифр  и не в невалидных значениях, то возвращает True, иначе False

        :return: bool
        Результат проверки в булевом типе данных
        """
        if re.match(r"^[\D]+$", self.__worldview) is not None and self.__worldview not in self.__worldview_invalid:
            return True
        return False

    def check_address(self) -> bool:
        """
        Проверка адреса

        Если строка начинается с ул. или не начинается с Алллея, то возвращает True, иначе False

        :return: bool
        Результат проверки в булевом типе данных
        """
        if re.match(r"^(ул\.)?(Аллея)?\s[\w\.\s-]+\d+$", self.__address) is not None:
            return True
        return False

    def check_all(self) -> int:
        """
        Проверяет все условия сразу

        Если все условия выполнины, то на return будет 9-ое
        Каждому несоответсвию предписана своя буква

        :return: int
        Результат проверки
        """
        if not self.check_telephone():
            return 0
        elif not self.check_weight():
            return 1
        elif not self.check_snils():
            return 2
        elif not self.check_passport_number():
            return 3
        elif not self.check_occupation():
            return 4
        elif not self.check_age():
            return 5
        elif not self.check_political_views():
            return 6
        elif not self.check_worldview():
            return 7
        elif not self.check_address():
            return 8
        else:
            return 9


class ReadFile:
    """
    Класс ReadFile считывает и хранит данные из выбранного файла.
    Attributes:

      __data - считанные данные из файла
    """

    __data: object

    # инициализация экземпляра класса ReadFromFile, параметры - объекты класса
    def __init__(self, path: str):
        """
        __init__ - инициализация экземпляра класса ReadFromFile
        Parameters

        path : str  -  Путь до выбранного файла
        """
        self.__data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self) -> object:
        """
        data - метод получения данных файла

        :return: object
        Возвращает тип object
        """
        return self.__data


parser = argparse.ArgumentParser(description='main')
parser.add_argument('-input', dest="file_input", default='90.txt', type=str)
parser.add_argument('-output', dest="file_output", default='90_output.txt', type=str)
args = parser.parse_args()
output = open(args.file_output, 'w')
file = ReadFile(args.file_input)
checkers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
number_of_valid_records = 0
with tqdm(file.data, desc='Валидация файла', colour="#FFFFFF") as progressbar:
    for elem in file.data:
        check_element = Validator(elem['telephone'], elem['weight'], elem['snils'], elem['passport_number'],
                                  elem['occupation'], elem['age'], elem['political_views'], elem['worldview'],
                                  elem['address'])
        valid_values = check_element.check_all()
        if valid_values == 9:
            output.write("telephone: " + elem["telephone"] + "\n" + "weight:" + str(elem["weight"]) + "\n" +
                         "snils: " + elem["snils"] + "\n" + "passport_number:" + str(
                elem["passport_number"]) + "\n" +
                         "occupation: " + str(elem["occupation"]) + "\n" + "age: " + elem["age"] + "\n" +
                         "political_views: " + elem["political_views"] + "\n" + "worldview: " + elem["worldview"] +
                         "\n" + "address: " + elem["address"] + "\n" + "__________________________________________\n")
            number_of_valid_records += 1
        else:
            checkers[valid_values] += 1
        progressbar.update(1)
number_of_invalid_records = checkers[0] + checkers[1] + checkers[2] + checkers[3] + checkers[4] + checkers[5] + \
                            checkers[6] + checkers[7] + checkers[8]
print("Общее число корректных записей:", number_of_valid_records, )
print("Общее число некорректных записей:", number_of_invalid_records)
print("Ошибки в telephone:", checkers[0])
print("Ошибки в weight:", checkers[1])
print("Ошибки в snils:", checkers[2])
print("Ошибки в passport_number:", checkers[3])
print("Ошибки в occupation:", checkers[4])
print("Ошибки в age:", checkers[5])
print("Ошибки в address:", checkers[6])
print("Ошибки в political_views:", checkers[7])
print("Ошибки в worldview:", checkers[8])
output.close()
