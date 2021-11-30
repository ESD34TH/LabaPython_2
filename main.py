import re
import json


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
    def __init__(self, telephone: str, weight: int, snils: str, passport_number: str, occupation: str, age: int,
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
        if (int(self.__weight) < 40) and (int(self.__weight) > 120):
            return True
        return False

    def check_snils(self) -> bool:
        """
        Проверка номера СНИЛС

        Если состоит из 11 цифр, то возвращает True, иначе False

        :return: bool
        Результат проверки в булевом типе данных
        """
        if re.match(r"^\d{11}$", self.__snils):
            return True
        return False

    def check_passport_number(self) -> bool:
        """
        Проверка номера паспорта

        Если состоит из 6 цифр, то возвращает True, иначе False

        :return: bool
        Результат проверки в булевом типе данных
        """
        if re.match(r"^\d{6}$", self.__passport_number):
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
        if re.match(r"^([A-Z]|[А-Я])[\D]+$", self.__occupation) is not None and self.__occupation not in\
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
        if (int(self.__age) < 0) and (int(self.__age) > 100):
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
        if re.match(r"^[\D]+$", self.__political_views) is not None and self.__political_views not in\
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

    