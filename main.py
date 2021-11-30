
class Validator:
    """
    __telephone: номер телефона
    __height: рост
    __snils: номер СНИЛС
    __passport_number: номер паспорта
    __occupation: вид занятости
    __age: возраст
    __political_views: политические взгляды
    __worldview: мировозрение
    __address: адрес
    """
    __telephone: str
    __height: float
    __snils: str
    __passport_number: str
    __occupation: str
    __age: int
    __political_views: str
    __worldview: str
    __address: str

    # инициализация экземпляра класса Validator
    def __init__(self, telephone: str, height: float, snils: str, passport_number: str, occupation: str, age: int,
                 political_views: str, worldview: str, address: str):
        self.__telephone = telephone
        self.__height = height
        self.__snils = snils
        self.__passport_number = passport_number
        self.__occupation = occupation
        self.__age = age
        self.__political_views = political_views
        self.__worldview = worldview
        self.__address = address

    def check_telephone(self) -> bool:
